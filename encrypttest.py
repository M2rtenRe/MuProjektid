import hashlib
import sys
import getpass
import base64
import paramiko
import pysftp
import os
import random
import string

writeHost = base64.b64decode("MTkyLjE2OC4xLjE3NiBzc2gtcnNhIEFBQUFCM056YUMxeWMyRUFBQUFEQVFBQkFBQUJBUURaN21tNHlRbnhab0ljR1AyYldEQUMySWEzTGEwcmRDTzZnZkpDOVlSOXlQN2t3UXBvM3FBY1JtTWNZb0xNd1NJMGg2NnZjdzJVUkEvWU5pNEFqTFFhenVHcDhpcTZKUkpmMU1YNUdwUXVmKytFK3pwNEhKeWk3V0VYd2hiV2RmT0FYR2UrS1B5eVRCVC85ZU5kemVLRlJKdnBQZm5LNldmN2JtcWROcjc0em9MNWhucGpYYjRuYTRVYXZhb29qbGpxbmdxMlk2VGNMZzJSOHptR1kxb1JrY1pXRlpZYXZmc3VMN0tZZDFRMFozbXNmc0owaVlHTGx3d0xGd05pdVMxKytFYk02dlRjekVQdFVXVnpLMU9LdDR4VHhVa0JzQzhnTFdrTjJBZ0g0MkFzVnA1UDdONXllYnROUkorZWN5ZkJEQS9PVHdZTzlFNURTVHgxWWhrdg==")
if os.path.isdir(os.environ["USERPROFILE"]+"\\.ssh") == False:
    os.makedirs(os.environ["USERPROFILE"]+"\\.ssh")
    f = open(os.environ["USERPROFILE"]+"\\.ssh\\known_hosts", "w")
    f.write(writeHost.decode("UTF-8"))
    f.close()

password = base64.b64decode("M2l0ZWFtaWRhcGFubmE/")
ip = base64.b64decode("OTAuMTkxLjE0Mi43Mw==")
keydata= b"""AAAAB3NzaC1yc2EAAAADAQABAAABAQDZ7mm4yQnxZoIcGP2bWDAC2Ia3La0rdCO6gfJC9YR9yP7kwQpo3qAcRmMcYoLMwSI0h66vcw2URA/YNi4AjLQazuGp8iq6JRJf1MX5GpQuf++E+zp4HJyi7WEXwhbWdfOAXGe+KPyyTBT/9eNdzeKFRJvpPfnK6Wf7bmqdNr74zoL5hnpjXb4na4Uavaoojljqngq2Y6TcLg2R8zmGY1oRkcZWFZYavfsuL7KYd1Q0Z3msfsJ0iYGLlwwLFwNiuS1++EbM6vTczEPtUWVzK1OKt4xTxUkBsC8gLWkN2AgH42AsVp5P7N5yebtNRJ+ecyfBDA/OTwYO9E5DSTx1Yhkv"""
key = paramiko.RSAKey(data=base64.decodebytes(keydata))
cnopts = pysftp.CnOpts()
cnopts.hostkeys.add(ip, "ssh-rsa", key)
ftp = pysftp.Connection(host=ip, username="root", password=password, cnopts=cnopts)

def createUser():
    f = ftp.open("paroolid.txt", "r")
    passListDecode = f.read().decode("UTF-8")
    passList = passListDecode.splitlines()
    newName = input("Uus kasutajanimi: ")
    if len(newName) <= 0:
        print("Nimi peab olema vähemalt 1 täht!")
        createUser()
    for line in passList:
        pp = ""
        pp += line.split(",")[1].strip().split("-")[0].strip()
        pp += newName
        userInFile = hashlib.md5(pp.strip().encode()).hexdigest()
        if userInFile == line.split(":")[0].strip():
            print("Nimi juba kasutusel!")
            createUser()
    newPass = getpass.getpass("Uus parool: ")
    if len(newPass) <= 0:
        print("Parool peab olema vähemalt 1 täht!")
        createUser()
    f.close()
    f = ftp.open("paroolid.txt", "a")
    saltName = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(12)])
    saltPass = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(12)])
    newNamee = ""
    newPasss = ""
    newNamee += saltName
    newNamee += newName
    newPasss += saltPass
    newPasss += newPass
    newUserHash = hashlib.md5(newNamee.strip().encode()).hexdigest()
    newPassHash = hashlib.md5(newPasss.strip().encode()).hexdigest()
    f.write(newUserHash+":"+newPassHash+","+saltName+"-"+saltPass+"\n")
    f.close()
    print("Kasutaja tehtud!")
    checkUser()

def checkUser():
    global userInHash
    userIn = input("Kasutajanimi: ")
    f = ftp.open("paroolid.txt", "r")
    passListDecode = f.read().decode("UTF-8")
    passList = passListDecode.splitlines()
    for line in passList:
        pp = ""
        pp += line.split(",")[1].strip().split("-")[0].strip()
        pp += userIn
        userInHash = hashlib.md5(pp.strip().encode()).hexdigest()
        if line.split(":")[0].strip() == userInHash:
            checkPass()
    print("Sellist kasutajanime pole!")
    checkUser()
    f.close()

def checkPass():
    passwordIn = getpass.getpass("Parool: ")
    #passInHash = hashlib.md5(passwordIn.strip().encode()).hexdigest()
    f = ftp.open("paroolid.txt", "r")
    passListDecode = f.read().decode("UTF-8")
    passList = passListDecode.splitlines()
    for line in passList:
        pp = ""
        pp += line.split(",")[1].strip().split("-")[1].strip()
        pp += passwordIn
        passInHash = hashlib.md5(pp.strip().encode()).hexdigest()
        if line.split(":")[1].strip().split(",")[0].strip() == passInHash :
            print("Õige!")
            input("Vajuta Enterit, et jätkata.")
            sys.exit()
    print("Vale parool!")
    checkPass()
    f.close()

def menu():
    logAsk = input("Kas tahad logida voi kasutaja teha?[L, N] ")
    if logAsk in ("L", "l"):
        checkUser()
    elif logAsk in ("N", "n"):
        createUser()
    else:
        menu()

menu()
ftp.close()

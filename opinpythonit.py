#Parooli muukija, mida ei tohiks kasutada kurjaks eesmärgiks ;)
#Programm muugib 1,000,000 parooli 5 sekundiga

import hashlib
import threading
from queue import Queue
import time
#Kasutaja input hashi ja parooli faili jaoks
passIn = input("Hash: ")
pwFile = input("Parooli fail: ")
#Proovib leida parooli faili
try:
    pwFile = open(pwFile, "r")
except:
    print("\n Faili ei leitud")
    quit()
#Peamine muukimisfunktsioon
def passCrack():
    for password in pwFile:
        filehash = hashlib.md5(password.strip().encode()).hexdigest() #Teeb hashi igast paroolist mis on paroolide failis
        #Kui parooli failist saadud hash on sama mis algul antud hash, siis programm annab sõnumi ja lõpeb
        if passIn == filehash:
            print("\n Parool leitud.\n Parool on {}".format(password))
            break
    else:   #Kui ei leia, siis fail lõpeb
        pass
#Threadimis funktsioon
def threader():
    while True:
        worker = q.get()
        passCrack()
        q.task_done()

q = Queue()
#Kasutab 500 threadi
for i in range(500):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

startTime = time.time()
#Iga thread teeb 10,000 parooli hashiks ja kui tehtud, siis alustab otsast peale
for worker in range(1,10000):
    q.put(worker)

q.join()
endTime = time.time()

print("\nAega võttis {}".format(endTime-startTime))



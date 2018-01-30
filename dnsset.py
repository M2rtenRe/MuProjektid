import os

def dnsAsk():
    userIn = input("DNS sisse[Y] või välja[N]?")
    if userIn == "Y" or userIn == "y":
        setDnsOn()

    if userIn == "N" or userIn == "n":
        setDnsOff()

    else:
        exit()

def interfaceAsk():
    global interface
    interface = input("Mis interface?[1,2] ")

    if interface == '1':
        interface = '"Wi-Fi"'
        dnsAsk()
    elif interface == '2':
        interface = '"Wi-Fi 2"'
        dnsAsk()
    else:
        interfaceAsk()

def setDnsOn():
    os.system('netsh interface ip set dnsservers '+interface+' static 82.196.13.196')
    os.system('netsh interface ip add dnsservers '+interface+' 87.117.205.136 index=2')

def setDnsOff():
    os.system('netsh interface ip set dnsservers '+interface+' dhcp')

interfaceAsk()



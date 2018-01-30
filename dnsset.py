#See on minu DNS vahetamise programm, mida läheb mul vaja välisma meedia teenuste vaatamiseks (nt Hulu)

import os
#Küsib kas tahab DNS lülitada sisse või välja
def dnsAsk():
    userIn = input("DNS sisse[Y] või välja[N]?")
    if userIn == "Y" or userIn == "y":
        setDnsOn()

    if userIn == "N" or userIn == "n":
        setDnsOff()

    else:
        exit()
#Küsib kas Wi-Fi või Wi-Fi2 interface, sest mul on 2 wifi kaarti
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
#Paneb DNSi sisse
def setDnsOn():
    os.system('netsh interface ip set dnsservers '+interface+' static 82.196.13.196')
    os.system('netsh interface ip add dnsservers '+interface+' 87.117.205.136 index=2')
#Võtab DNSi välja
def setDnsOff():
    os.system('netsh interface ip set dnsservers '+interface+' dhcp')
#Käivitab kõik funktsioonid
interfaceAsk()



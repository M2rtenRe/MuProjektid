import hashlib
import threading
from queue import Queue
import time

passIn = input("Hash: ")
pwFile = input("Parooli fail: ")

try:
    pwFile = open(pwFile, "r")
except:
    print("\n Faili ei leitud")
    quit()

def passCrack():
    for password in pwFile:
        filehash = hashlib.md5(password.strip().encode()).hexdigest()

        if passIn == filehash:
            print("\n Parool leitud.\n Parool on {}".format(password))
            break
    else:
        pass

def threader():
    while True:
        worker = q.get()
        passCrack()
        q.task_done()

q = Queue()

for i in range(500):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

startTime = time.time()

for worker in range(1,10000):
    q.put(worker)

q.join()
endTime = time.time()

print("\nAega võttis {}".format(endTime-startTime))



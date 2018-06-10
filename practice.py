import datetime
import threading
import os
import time

from os.path import isfile


def getLogcat(filename):
    print("Run logcat on daemon thread")
    os.system('adb logcat > ' + filename)


def waitFile(filename):
    while not isfile(filename):
        print("Wait for creating file " + filename)
        time.sleep(1)


def printLog(filename):
    print("Print logs in " + filename)
    f = open(file=filename, mode='r')
    while True:
        line = f.readline()
        if not line: break
        print(line)
    f.close()


if __name__ == '__main__':
    filename = 'logcat_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S') + '.txt'
    tLogcat = threading.Thread(target=getLogcat, daemon=True, args=(filename,))
    tLogcat.start()
    waitFile(filename)
    printLog(filename)

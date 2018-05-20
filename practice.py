import subprocess
import datetime


def getLogcat():
    filename = 'logcat_' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    subprocess.call('adb logcat > ' + filename + '.txt', shell=True)

if __name__ == '__main__':
    getLogcat()

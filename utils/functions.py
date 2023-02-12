import time
from utils.logger import Logger

def sleep_sec(sec = 2, msg = ''):
    Logger.log("seep_sec("+str(sec)+") " + msg)
    time.sleep(sec)

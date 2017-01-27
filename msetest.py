# -------------------------------------------------------
# msetest.py -- program to test mousereader.py
#
# 01/27/17 DLB Created
# -------------------------------------------------------

import mousereader
import time

def run():
    mousereader.initMseTrack()
    while True:
        x, y = mousereader.getMousePosition()
        print("%08dx %08dy" % (x, y))
        time.sleep(1)


if __name__ == "__main__":
    run()

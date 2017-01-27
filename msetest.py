# -------------------------------------------------------
# msetest.py -- program to test mousereader.py
#
# 01/27/17 DLB Created
# -------------------------------------------------------

import mousereader
import time

def run():
    mousereader.initMouseTrack()
    while True:
        x, y = mousereader.getMousePosition()
        print("%8.3f %8.3f" % (x, y))
        time.sleep(1)


if __name__ == "__main__":
    run()

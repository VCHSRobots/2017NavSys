# -------------------------------------------------------
# mousereader.py -- program to read mouse locations
#
# 01/27/17 DLB Created
# -------------------------------------------------------

import threading

xloc = 0
yloc = 0
fmsefile = 0

def sumMovement(x, y):
    global xloc, yloc
    if x >= 128:
        x = x - 256
    if y >= 128:
        y = y - 256
    xloc += x
    yloc += y

def readMsePosition():
    global fmsefile, xloc, yloc
    c = fmsefile.read(3)
    n = len(c)
    if n != 3:
        print("Mouse Read Error! Missed Bytes.")
        return locx, locy
    #print(c[0], c[1], c[2])
    if c[0] & 0x08 == 0:
        print("Mouse Read Error! Bad Data.")
        return locx, locy
    sumMovement(c[1], c[2])

def runmseread():
    while True:
        readMsePosition()

def initMouseTrack():
    global fmsefile, locx, locy
    xloc = 0
    yloc = 0
    fmsefile = open("/dev/input/mouse0", "rb", buffering=0)
    t = threading.Thread(target=runmseread)
    t.start()

def getMousePosition():
    global xloc, yloc
    return xloc, yloc


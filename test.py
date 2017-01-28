import socket
import math
import mousereader
import time

mousereader.initMouseTrack()
xm1 = 2
ym1 = 4
#alpha = 90 - theta - math.degrees(math.atan((xm1 - xm0) / (ym1 - ym0)))
#print ((math.sqrt((xm1-xm0) * (ym1 - ym0)) * math.cos(alpha))
while 1:
	xf0 = float(0.0000000000000000000000000000000000000000000000000000000001)
	yf0 = float(0.0000000000000000000000000000000000000000000000000000000001)
	xf1 = float(0.0)
	yf1 = float(0.0)
	xm0 = float(0.0000000000000000000000000000000000000000000000000000000001)
	ym0 = float(0.0000000000000000000000000000000000000000000000000000000001)
	theta = float(45.0)
	xm1, ym1 = mousereader.getMousePosition()
	alpha = float(90 - theta - math.atan((xm1 - xm0) / (ym1 - ym0)))
	
	#print ("%8.3f %8.3f" % (xm1, ym1))
	#print (alpha)
	time.sleep(1)
	print ("The Y coordinate is:")
	print (math.sqrt((xm1 - xm0)**2 * (ym1 - ym0)**2) * math.cos(alpha))
	time.sleep(1)
	print ("The X coordinate is:")
	print (math.sqrt((xm1 - xm0)**2 * (ym1 - ym0)**2) * math.sin(alpha))


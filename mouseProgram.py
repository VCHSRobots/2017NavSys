import socket
import math
import mousereader
import time

mousereader.initMouseTrack()
xm1 = 0.0
ym1 = 0.0
xf0 = 0.0
yf0 = 0.0
xf1 = 0.0
yf1 = 0.0

host = '10.44.15.32'
port = 5801

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket created")
time.sleep(.1)
server_socket.bind((host, port))
server_socket.listen(1)
print ("Listening in socket")
conn, addr = server_socket.accept()
print ("Connected with " + addr[0] + ":" + str(addr[1]))

#alpha = 90 - theta - math.degrees(math.atan((xm1 - xm0) / (ym1 - ym0)))
#print ((math.sqrt((xm1-xm0) * (ym1 - ym0)) * math.cos(alpha))
while 1:

	xm0 = xm1
	ym0 = ym1
	xf0 = xf1
	yf0 = yf1
	theta = float(conn.recv(1024))
	xm1, ym1 = mousereader.getMousePosition()
	print ("Recieved data from client:" + theta)
	if not data: break
	#xm1 = 5.0
	#ym1 = 0.0
	deltaXm = xm1 - xm0
	deltaYm = ym1 - ym0
	if (deltaYm < 0):
		theta = theta + 180
		deltaYm = deltaYm * -1.0
		deltaXm = deltaXm * -1.0
	if (deltaYm == 0):
		alpha = -1.0 * theta
	else:
		alpha = 90.0 - theta - math.degrees(math.atan((deltaXm) / (deltaYm)))
		
	
	# is atan returning in radians or degrees?
	if (deltaYm == 0.0 and deltaXm < 0.0):
		xf1 = xf0 - math.sqrt((deltaXm)**2 + (deltaYm)**2) * math.cos(math.radians(alpha))
	else:
		xf1 = xf0 + math.sqrt((deltaXm)**2 + (deltaYm)**2) * math.cos(math.radians(alpha))
	yf1 = yf0 + math.sqrt((deltaXm)**2 + (deltaYm)**2) * math.sin(math.radians(alpha))

        conn.send(xf1)
        conn.recv(1024)
        conn.send(yf1)
        
	print ("alpha = " + str(alpha) + "   xf1 = " + str(xf1) + "   yf1 = " + str(yf1))

	#time.sleep(5)

	#print ("%8.3f %8.3f" % (xm1, ym1))
	#print (alpha)
	#time.sleep(.1)
	#print ("The Y coordinate is:")
	#print (math.sqrt((xm1 - xm0)**2 + (ym1 - ym0)**2) * math.cos(alpha))
	#time.sleep(.1)
	#print ("The X coordinate is:")
	#print (math.sqrt((xm1 - xm0)**2 + (ym1 - ym0)**2) * math.sin(alpha))


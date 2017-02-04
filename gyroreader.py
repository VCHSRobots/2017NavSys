from sense_hat import SenseHat
import time
import socket
import gyrodata
import sys

host = '10.44.15.35'
port = 5802

gyrodata.initGetGyroAngle()

gyro_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
gyro_socket.bind((host, port))
print('Socket created')
print('Listening...')
gyro_socket.listen(1)
conn, addr = gyro_socket.accept()
print ("Connected with " + addr[0] + ":" + str(addr[1]))

while 1:
	data = conn.recv(1024)
	print (str(data))
	if data == (b'Requesting Gyro\r\n'):
		gyrodata.sendGyroData(conn)

conn.close
	

#while 1:
#	data = conn.recv(1024)
#
#	robotAngle = bytes(gyroAngle, 'utf-8')
#	conn.send(robotAngle)
#	print('data sent: ' + gyroAngle)
#	if not data:
#		break

#conn.close
	

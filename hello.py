import socket
import time

host = '10.44.15.32'
port = 5801

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket created"
time.sleep(1)
server_socket.bind((host, port))
server_socket.listen(1)
print "Listening in socket"
conn, addr = server_socket.accept()
print "Connected with " + addr[0] + ":" + str(addr[1])
while 1:
	data = conn.recv(1024)
	theta = float(data)
	print "Recieved data from client:" + data
#	reply "OK..." + data
#	server_socket.send(data)
	if not data: break
	conn.send(data)
conn.close()
server_socket.close()

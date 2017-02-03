# -----------------------------------------------------------------
# servermanager.py -- program to accept clients on separate threads
#
# 01/31/17 NG Created
# -----------------------------------------------------------------

import socket
import threading
import time

def echo(conn):
	string = conn.recv(1024)
	conn.send(string)
	threadMessage(string)


def mouse_program():
	threadMessage("Mouse Program called.")
	# ....

def target_program():
	threadMessage("Target Program called.")
	# ....

def threadMessage(message):
	#prints "THREAD_NAME: message"
	print(threading.current_thread().name + ": " + str(message))

class ClientManager(threading.Thread):
	
	def __init__(self, conn, addr):
		threading.Thread.__init__(self)
		self.conn = conn
		self.addr = addr

	def run(self):
		threadMessage("New thread made for Client!")
		while 1:
			echo(self.conn)
		# read string from client
		# if sting == "MouseProgram":
			# mouse_program()
		# else if string == "targetProgram"
			# target_program()
		# etc....
		

host = '10.44.15.35'	# IP Address of the server-side processor
port = 5801		# Port Address of server-side processor

server_manager = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
time.sleep(.1)
server_manager.bind((host, port))
threadMessage("Server manager socket created")

while 1:	
	server_manager.listen(25)
	conn, addr = server_manager.accept()
	new_client = ClientManager(conn, addr)
	new_client.start()
	threadMessage("New thread created")
	

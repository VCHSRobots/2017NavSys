from sense_hat import SenseHat
import threading
import time

sense = SenseHat()

def runGyroRead():
	global gyroAngle
	while True:
		sense.set_imu_config(False, True, False)
		orientation = sense.get_orientation()
		gyroAngle = orientation['yaw']
		time.sleep(.005)
		

def initGetGyroAngle():
	t = threading.Thread(target=runGyroRead)
	t.start()

def getGyroData():
	global gyroAngle
	return gyroAngle

def sendGyroData(conn):
	global gyroAngle
	str_gyroAngle = str(gyroAngle) + '\n'
	byteAngle = bytes(str_gyroAngle, 'utf-8')
	print(byteAngle)
	conn.send(byteAngle)
	print('data sent')
	

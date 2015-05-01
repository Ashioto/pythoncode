#!/usr/bin/env python
#server.py

import socket, traceback, time
from threading import *


def generatedata(index):
	glb_condition.acquire()
	glb_condition.wait()
	glb_condition.release()
	# TODO:
	return data

def recvdata(address,port):
	print 'The thread for receiving data is running.'
	global glb_client_data
	index=glb_client_address.index(address)
	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.bind(('',port))
	while 1:
		data=s.recvfrom(8192)[0]
		glb_client_data[index]=data


def senddata(address,port):
	print 'The thread for sending data is running.'
	s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	s.connect((address,51000))
	index=glb_client_address(address)
	while 1:
		data=generatedata(index)
		s.sendall(data)


def handlechild(clientsock):
	global glb_client_name
	global glb_client_data
	global glb_client_address
	address=clientsock.getpeername()[0]
	port=10000+len(glb_client_address)

	print 'Got connection from', address
	# Save its information
	glb_client_name.append('')
	glb_client_data.append('')
	glb_client_address.append(address)

	t=Thread(target=recvdata,args=[address,port])
	t.setDaemon(1)
	t.start()
	t=Thread(target=senddata,args=[address,port])
	t.setDaemon(1)
	t.start()

	while 1:
		# Send the client list, per 2 seconds.
		data=','.join(glb_client_address)
		try:
			clientsock.sendall(data)
		except:
			traceback.print_exc()
			continue
		time.sleep(2)

	clientsock.close()
	

def checkandorder():
	# Only when all the clients' data are updated, will this function wake the other threads.
	data=[]
	while 1:
		if data==glb_client_data:
			continue
		else:
			glb_condition.acquire()
			glb_condition.notifyAll()
			glb_condition.release()	
			data=glb_client_data



host=''
port=51222
glb_client_name=[]
glb_client_data=[]
glb_client_address=[]
glb_condition=Condition()

print 'Initialize server...'

# Set up a socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(3)
# Start a new thread to synchronize other threads
t=Thread(target=checkandorder)
t.setDaemon(1)
t.start()

print 'Done.'

while 1:
	try:
		print 'Waiting for the clients...'
		clientsock, clientaddr=s.accept()
		print 'A client has been accepted.'
	except KeyboardInterrupt:
		raise
	except:
		traceback.print_exc()
		continue

	# Start a new thread to handle it
	t=Thread(target=handlechild, args=[clientsock], name=clientsock.getpeername()[0])
	t.setDaemon(1)
	t.start()	
	print 'Start a new thread for it.'
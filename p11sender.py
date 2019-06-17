#!/usr/bin/python2
import socket,sys 
 
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
 
ip="127.0.0.1" 
port= 8888 
TIMEOUT=100
 
s.bind((ip,port)) 
s.settimeout(TIMEOUT) 

while True: 
	r = s.recvfrom(500) 
	print(r)
	print("receive from client : " + r[0]) 
	reply = raw_input('server : ') 
	client_address = r[1] 
	s.sendto(reply, client_address) 


s.close()

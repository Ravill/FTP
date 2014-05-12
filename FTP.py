import socket
import sys
import os
import time

from os import walk

s = socket.socket()



def send(mes=''):
	CRLF=True
	s.send(bytes(mes + ("\r\n"), "UTF-8"))

def recieve():
	rec = s.recv(1024)
	print (rec)
	    
def action(mes=''):
	send(mes)
	return recieve()
def browse_local(path=''):
	for (dirpath, dirnames, filenames) in walk(path):
		print (dirpath)
		print ('Files in directory')
		print (dirnames)
		print (filenames)
		print ('\n')
		break
def pasv():
	mes = ('PASV')
	send(mes)
	mes = (s.recv(1024))
	print (mes)
	mes = mes.decode()
	nmsg = mes.split('(')
	print (nmsg)
	nmsg = nmsg[-1].split(')')
	p = nmsg[0].split(',')
	print(p)
	newip = '.'.join(p[:4])
	newport = int(p[4])*256 + int(p[5])
	print (newip)
	print (newport)
	return (newip,newport)

def listar():
	newip, newport= pasv()
	p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	p.connect((newip, newport))
	mes = ('NLST')
	action (mes)
	rec = p.recv(1024)
	rec = rec.decode()
	rec.split('\r\n')
	print (rec)
	rec = p.recv(1024)
	print (rec)	
	p.close


#s.connect((input("Enter FTP Address: "), 21))
s.connect(("192.100.230.21", 21))
s.recv(1024)		
		
#usern = input("Enter user: ")
#action('USER '+usern)
action('USER '+'userftp')

#passw = input("Enter password: ")
#action('PASS '+passw)
action('PASS '+'r3d3sf1s1c@s')

listar()

print("Remote Directory")
mes = ('PWD')
action(mes)

print('Change remote directory')
mes = ('CWD Pikachu')
action(mes)

print("Remote Directory")
mes = ('PWD')
action(mes)

listar()

print("Local Directory")
path = ('/home/ec2-user/')
browse_local(path)

print('Change local directory')
path = (path+input("Directorio: ")+'/')
browse_local(path)

mes = ('TYPE I')
action(mes)

mes = ('TYPE A')
action(mes)

mes = ('MODE S')
action(mes)



s.close                     # Close the socket when done
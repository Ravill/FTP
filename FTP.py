import socket
import sys
import os
import time

from os import walk

s = socket.socket()

def send(mes=''):
	s.send(bytes(mes + ("\r\n"), "UTF-8"))

def recieve():
	rec = s.recv(1024)
	    
def action(mes=''):
	send(mes)
	return recieve()
def local_dir(path=''):
	for (dirpath, dirnames, filenames) in walk(path):
		print ('"'+dirpath+'"')
		break
def browse_local(path=''):
	for (dirpath, dirnames, filenames) in walk(path):
		print (dirnames)
		print (filenames)
		print ('\n')
		break
def pasv():
	while True:
		vali = ''
		mes = ('PASV')
		send(mes)
		mes = (s.recv(1024))
		mes = mes.decode()
		nmsg = mes.split('(')
		nmsg = nmsg[-1].split(')')
		p = nmsg[0].split(',')
		newip = '.'.join(p[:4])
		newport = int(p[4])*256 + int(p[5])
		return (newip,newport)
		break
		
	

def listar():
	newip, newport = pasv()
	p = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	p.connect((newip, newport))
	mes = ('NLST')
	action (mes)
	rec = p.recv(1024)
	rec = rec.decode()
	rec.split('\r\n')
	print (rec)
	mes = ('ABOR')
	p.send(bytes(mes + ("\r\n"), "UTF-8"))
	p.close
	recieve()

#s.connect((input("Enter FTP Address: "), 21))
s.connect(("192.100.230.21", 21))
s.recv(1024)		
		
#usern = input("Enter user: ")
#action('USER '+usern)
action('USER '+'userftp')

#passw = input("Enter password: ")
#action('PASS '+passw)
action('PASS '+'r3d3sf1s1c@s')

while True:
	os.system('cls' if os.name == 'nt' else 'clear')
	print ('1 - Print Local and Remote Directory')
	print ('2 - Change Directory')
	print ('3 - Send Files')
	print ('4 - Recieve Files')
	print ('5 - Cambiar Permisos')
	print ('6 - Salir')
	opc = input('Seleccione una opcion: ')
	if opc == '1':
		while True:
			directory = ''
			os.system('cls' if os.name == 'nt' else 'clear')
			print('Remote Directory')
			mes = ('PWD')
			send(mes)
			directory = s.recv(1024)
			directory = directory.decode()
			vali = directory.split('i')
			vali = vali[0].split(' ')
			vali = vali[0]
			if vali == '257':
				directory = directory.split('"')
				directory = directory[1]
				print('"'+directory+'"')
			else:
				print('"'+directory+'"')
			listar()
			print('Local Directory')
			path = ('/home/ec2-user/')
			local_dir(path)
			browse_local(path)
			print(input('Hit Return'))
			break
	if opc == '2':
		while True:
			os.system('cls' if os.name == 'nt' else 'clear')
			print ('1 - Change Local Directory')
			print ('2 - Change Remote Directory')
			print ('3 - Regresar')
			opc2 = input('Seleccione una opcion: ')
			if opc2 == '1':
				print('Change local directory')
				path = (path+input("Directorio: ")+'/')
				browse_local(path)
				print(input('Hit Return'))
			if opc2 == '2':
				print('Change remote directory')
				rd = input("Enter directory: ")
				action('CWD '+rd)
				print(input('Hit Return'))
			if opc2 == '3':
				break
	if opc == '3':
		while True:
			os.system('cls' if os.name == 'nt' else 'clear')
			print ('File type')
			print ('1 - ASCII')
			print ('2 - Image')
			print ('3 - Return')
			opc2 = input('Seleccione una opcion: ')
			if opc2 == '1':
				print('')
			if opc2 == '3':
				break
	if opc == '4':
		while True:
			print ('Hola')
			break
	if opc == '5':
		action('SITE CHMOD '+input_var + ' ' + pof)
	if opc == '6':
		break
		
	

listar()

print("Remote Directory")
mes = ('PWD')
action(mes)

print('Change remote directory')
mes = ('CWD Tecu')
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
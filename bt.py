import time
import serial
import os
os.chdir("/root/revolution")
usbport='/dev/ttyAMA0'
por = serial.Serial(usbport,115200,timeout=3.0)
por.flushInput()

temp = ""
por.write("Hi")
temp = por.read(5)

if temp == "Hi PI":
	board=1
else:
	board=0

set_file =  open("settings.txt","r")
set = set_file.read()
set_file.close()

if set.strip() == "g":
	myset=1
else:
	myset=0



#************if condition for the start up process **********************

if board==0 and  myset==0:
	pass
elif board==0 and  myset==1:
	set_file =  open("settings.txt","w")
	set_file.write("n")
	set_file.close()
	os.system("sudo python usermode.py")
elif board==1 and  myset==0:
	set_file =  open("settings.txt","w")
	set_file.write("g")
	set_file.close()
	os.system("sudo python mymode.py")
elif board==1 and  myset==1:
	os.system("sudo python _maincode.py")

#*************************************************************************

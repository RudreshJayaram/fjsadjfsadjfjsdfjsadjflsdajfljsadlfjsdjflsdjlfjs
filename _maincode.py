from multiprocessing import Process,Queue
import threading
import time
import sys
import socket
import os
import RPi.GPIO as GPIO
import re
from urllib2 import urlopen, Request
from time import mktime, sleep
from datetime import datetime
from json import dumps
yureka_str = ""
oldmax=0
curmax = 0


wifi_ok=0
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
WiFi_mode = 7
WiFi_status = 8
WiFi_switch = 25

GPIO.setup(WiFi_mode,GPIO.OUT)
GPIO.setup(WiFi_switch,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(WiFi_status,GPIO.OUT)

class Client (object):
    api_url = "http://api.carriots.com/streams"

    def __init__(self, api_key=None, client_type='json'):
        self.client_type = client_type
        self.api_key = api_key
        self.content_type = "application/vnd.carriots.api.v2+%s" % self.client_type
        self.headers = {'User-Agent': 'Raspberry-Carriots',
                        'Content-Type': self.content_type,
                        'Accept': self.content_type,
                        'Carriots.apikey': self.api_key}
        self.data = None
        self.response = None

    def send(self, data):
        self.data = dumps(data)
        request = Request(Client.api_url, self.data, self.headers)
        self.response = urlopen(request)
        return self.response

def iotsend(ack):
    #device = "RPI@BOTRIO.BOTRIO"
    device = "ooo@BOTRIO.BOTRIO"
    apikey = "41d753080c1a2a72515e2fff11d116cdd8f7e91a5b3a2b278b9612af135edc71"  # Replace with your Carriots apikey
    client_carriots = Client(apikey)
    timestamp = int(mktime(datetime.utcnow().timetuple()))
    data = {"protocol": "v2", "device": device, "at": timestamp, "data": dict(
    light=ack)}
    carriots_response = client_carriots.send(data)
    #print carriots_response.read()


def readfile(filename):
    global yureka_str
    file=open(filename,"r")
    data =file.read()
    file.close()
    list = re.findall("iot[\d][\d][\d]",data)
    #rint list
    numlist = []
    for entry in list:
                #rint int(entry[-3:])
                numlist.append(int(entry[-3:]))
    #print numlist
    curmax= max(numlist)
    if curmax < 9 :
	curmax = "00"+str(curmax)
    elif curmax > 9 and curmax <100 :
	curmax = "0"+str(curmax)
    else:
	curmax = str(curmax)	
    #print curmax
    yureka_str = "iot"+curmax+"(.*)~"
    #print yureka_str
    matches = re.findall(yureka_str,data)
    #print matches
    fo=open("iotoldmax.txt","r")
    oldmax =fo.readline().strip()
    fo.close()
    fo=open("iotoldmax.txt","w")
    fo.write(str(curmax))
    fo.close()
    #print "************"
    #print oldmax
    #print "************"
    #print curmax
    #print "************"
    if int(curmax) >int(oldmax):
	ifile=open("appdata.txt","w")
	ifile.write(".")
	ifile.close()
	ffile=open("flag.txt","w")
	ffile.write("1")
	ffile.close()
	time.sleep(1)   #here it was 4 and it was working fine
	ifile=open("appdata.txt","w")
	ifile.write(matches[0])
	ifile.close()
	ifile=open("memory.txt","w")
	ifile.write(matches[0])
	ifile.close()
	ffile=open("flag.txt","w")
	ffile.write("1")
	ffile.close()
        iotsend("iot"+str(curmax)+"ACK")

    else:
        #print "fail"
	pass

def readfromcloud():
	#print "hello"
	
	while True:
		#os.system("curl --header \"carriots.apikey:41d753080c1a2a72515e2fff11d116cdd8f7e91a5b3a2b278b9612af135edc71\" \"http://api.carriots.com/streams/?device=iPhone6Mobile@BOTRIO.BOTRIO\" > hi.txt ")
		GPIO.output(WiFi_mode,0)
		os.system("curl --header \"carriots.apikey:41d753080c1a2a72515e2fff11d116cdd8f7e91a5b3a2b278b9612af135edc71\" \"http://api.carriots.com/streams/?device=iii@BOTRIO.BOTRIO\" > hi.txt ")
		readfile("hi.txt")
		GPIO.output(WiFi_mode,1)
		time.sleep(1)

def switch():
	while True:
       		if GPIO.input(WiFi_switch) == 0:
			if mode == "s":
				file= open("appdata.txt","w")
				file.write(".")
				file.close()
				flagfile= open("flag.txt","w")
				flagfile.write(str(1)+"\n")
				flagfile.close()
				file=open("wifi_mode.txt","w")
		                file.write("a")
                		file.close()
				time.sleep(.1)
		                os.chdir("/etc/network")
                		os.system("rm interfaces")
		                os.system("cp interfaces.apnmode interfaces")
                		os.system("sudo reboot")
			elif mode == "a":
				file= open("appdata.txt","w")
				file.write(".")
				file.close()
				flagfile= open("flag.txt","w")
				flagfile.write(str(1)+"\n")
				flagfile.close()
				time.sleep(.1)
				file=open("wifi_mode.txt","w")
		                file.write("s")
                		file.close()
		                os.chdir("/etc/network")
	                	os.system("rm interfaces")
	        	        os.system("cp interfaces.stamode interfaces")
                		os.system("sudo reboot")


def b():
	global wifi_ok
        global c
	global addr
        while True:
		try:
	                #print "please connect to the network"
        	        c, addr = s.accept()
	                #print addr
        	        y=c.recv(1024)
                	number = int(y[1:4])
	                #print number
        	        result = ((number%9)+(number%5)+7)*31
                	c.sendall(str(result))
			f = open("t_p.txt","w")
			f.write("0")
			f.close()
			wifi_ok =1
		except:
			pass


def appdatacollection():
	global c
	global wifi_ok
	while wifi_ok == 0:
		pass
	

	while True:
		y=c.recv(1024)
		if y.strip() == "":
			y="Y"
		file= open("appdata.txt","w")
		file.write(y.strip())
		file.close()
		if y.strip() != "." or y.strip() != "Y":
			filels= open("laststring.txt","w")
			filels.write(y.strip())
			filels.close()
		flagfile= open("flag.txt","w")
		flagfile.write(str(1)+"\n")
		flagfile.close()
		if y.startswith("#A"):
			time.sleep(5)
	

def pingtouch():
	global wifi_ok
	while wifi_ok == 0:
		pass	
	global c
	global addr
        while True:
                try:
                        f = open("t_p.txt","r")
                        flag = f.readline()
                        f.close()
                        if flag.strip() == "t":
                                fi = open("touch.txt","r")
                                c.sendall(fi.readline()+"\n")
                                fi.close()
                                f = open("t_p.txt","w")
                                f.write("0")
                                f.close()
                        if flag.strip() == "p":
                                time.sleep(0.1)
                                fi = open("ping.txt","r")
                                bt= fi.readline()
                                fi.close()
                                c.sendall(bt.strip())
                                f = open("t_p.txt","w")
                                f.write("0")
                                f.close()

                        else:
                                pass
                except:
                        pass


def main():
	while True:
		os.system("sudo python _subcode.py")
		
		


#**************************************************************** code starts here  *********************************************************************************

f = open("t_p.txt","w")
f.write("0")
f.close()
file=open("wifi_mode.txt","r")
mode = file.readline().strip()
file.close()
q= Queue()

file= open("memory.txt","r")
y=file.readline()
file.close()
file= open("appdata.txt","w")
file.write(y.strip())
file.close()
flagfile= open("flag.txt","w")
flagfile.write(str(1)+"\n")
flagfile.close()





if mode == "s":
	time.sleep(30)
	p1=Process(target =switch)
        p1.start()
	p2=Process(target =readfromcloud)
        p2.start()
	GPIO.output(WiFi_mode,1)
	while True:
		os.system("sudo python _subcode.py")
	
else:
	GPIO.output(WiFi_mode,0)
	s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
	host = "1.2.3.4"
	port=8891
	wifi_ok = 0
	s.bind((host, port))
	s.listen(5)
	p1=Process(target =switch)
        p1.start()
	p2=Process(target =main)
        p2.start()
        our_thread=threading.Thread(target =pingtouch)
        our_thread.setDaemon(True)
        our_thread.start()
	
	while True:
		c, addr = s.accept()
		y=c.recv(1024)
		number = int(y[1:4])
		result = ((number%9)+(number%5)+7)*31
		c.sendall(str(result))
		wifi_ok =1
		
		while True:
			y=c.recv(1024)
			print y
			file= open("magicfile.txt","a")
			file.write(y.strip())
			file.close()
			if y.strip() != "":
				file= open("appdata.txt","w")
				file.write(y.strip())
				file.close()
				if y.strip() !="." and  "U[" not in y.strip():
					filem= open("memory.txt","w")
					filem.write(y.strip())
					filem.close()
				flagfile= open("flag.txt","w")
				flagfile.write(str(1)+"\n")
				flagfile.close()
				if y.startswith("#A"):
					time.sleep(5)
			else:
				break
		c.close()

		

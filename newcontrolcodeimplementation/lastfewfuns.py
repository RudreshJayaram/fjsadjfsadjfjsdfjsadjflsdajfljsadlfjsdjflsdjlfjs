#***********************************************************************************new function addition *******************************************************************

def ping():
	time.sleep(.5)
	global i
	SenNo = int(String[i+1])
	i = i+2
	
	data = ""
	temp = ""
	if SenNo == 0:
		FTs = "FV012"
	elif SenNo == 1:
		FTs = "FV102"
	elif SenNo == 2:
		FTs = "FV201"
	elif SenNo == 3:
		FTs = "FV501"
	elif SenNo == 4:
		FTs = "FV401"
	por.write(FTs)
	while data != "#":
		data = por.read(1)
		if data == "\n" or data == "\r":
			data = ""
		temp= temp+data
	tpfile = open("t_p.txt","w")
	tpfile.write("p\n")
	tpfile.close()
	pf = open("ping.txt","w")
	pf.write(temp[1:4])	
	pf.close()

def calibrate():
	time.sleep(0.5)
	global i
	SenNo = int(String[i+1])
	i = i+2
	print SenNo
	
	data = ""
	temp = ""
	if SenNo == 0:
		FTs = "FV012"
	elif SenNo == 1:
		FTs = "FV102"
	elif SenNo == 2:
		FTs = "FV201"
	elif SenNo == 5:
		FTs = "FV301"
	elif SenNo == 3:                  # for pg sensor 
		FTs = "FV401"
	while True:
		data = ""
		temp = ""
		por.write(FTs)
		while data != "#":
			data = por.read(1)
			if data == "\n" or data == "\r":
				data = ""
			temp= temp+data
		
		tpfile = open("t_p.txt","w")
		tpfile.write("p\n")
		tpfile.close()
		pf = open("ping.txt","w")
		pf.write(temp[1:4])	
		pf.close()
		time.sleep(0.5)

def touch():
	global i
	por.write(String[i:i+3])
	i=i+3
	por.write("Q")
	while True:
		data = ""
		temp = ""
		while data != "#":
			data = por.read(1)
			if data == "\n" :
				data = ""
			temp= temp+data
		touchdata = temp	
		tpfile = open("t_p.txt","w")
		tpfile.write("t\n")
		tpfile.close()
		file =open("touch.txt","w")
		file.write(touchdata)
		file.close()


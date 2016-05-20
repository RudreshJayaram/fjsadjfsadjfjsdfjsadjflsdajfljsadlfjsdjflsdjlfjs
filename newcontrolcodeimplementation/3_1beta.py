import time
import serial
import os
import serial
import threading
import re
import sys

import RPi.GPIO as GPIO
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)

usbport='/dev/ttyAMA0'
por = serial.Serial(usbport,115200,timeout=15.0)
por.flushInput()



def led(k):
        time.sleep(0.005)
        por.write(string[k:k+13])
        return k+12


def buzzer(k):
        time.sleep(0.005)
        por.write(string[k:k+3])
        return k+2

def delay(k):
	#print "delay"
	if string[k+5] == "m":
		time.sleep(int(string[k+1:k+5])/1000.0)
		return k+5
	elif string[k+5] == "s":
		time.sleep(int(string[k+1:k+5]))
		return k+5
					
	
def lcd(k):
	time.sleep(.005)
	por.write(string[k:k+38])	
	return k+37
		
def motor(k):
	#print "motor"
	time.sleep(0.005)
	if int(string[k+1]) <=2:
		por.write(string[k:k+4])
		return k+3
	else :
		pass	
	
	
#************************************************************************************************


'''
While
IF
Repate
'''
string = ""
mainFlag = 0
wbCount = 0
wFlag = 0
bCount = 0
fFlag = 0
brCount = 0
rFlag = 0
i = 0
senEndPos = 0
repEndPos = 0
whileEndPos = 0
n = 0
#count = 0
state = 1
senCount = 0
#..................................While Function..............................................
def whilefun(p):
    global whileEndPos
    global senCount
    state = 1
    breakStatus = 0
    wEndPos = 0
    eWCount = 0
    eWFlag = 1
    eeWFlag = 0
    uCount = 0
    senCount = 0
    v = p + 1
    #print "v",
    #print v
    #print "whileEndPos",
    #print whileEndPos
    #print "while"
    if string[p + 1] == 'I':
        while v <= whileEndPos:
            if string[v] == '[' and eWFlag == 1:
                eeWFlag = 1
                eWCount += 1
            if string[v] == ']' and eWFlag == 1:
                eWCount -= 1
            if eWCount == 0 and eWFlag == 1 and eeWFlag == 1:
                eWFlag = 0
                wEndPos = v
                #print " While end pos ",
                #print wEndPos
            v += 1
        port = string[p + 2]
        val = int(string[p + 4: p + 7])
        uCount = int(string[p + 10: p + 13])
        while 1:
	    #**************************************
            #svalW = raw_input("input the sensor value on port")
	    FTs = "FV"+port+port+port
	    data = ""
            temp = ""
            por.write(FTs)
            while data != "#":
                data = por.read(1)
                if data == "\n" or data == "\r":
                        data = ""
                temp= temp+data
            #print temp[1:4]
	    #**************************************
            svalW = int(temp[1:4])
            breakStatus = 0
            #print "one sensor While"
            if string[p + 3] == 'g' and svalW > val:
                #print "greater"
                if svalW > val and state == 1:
                    state = 0
                    senCount += 1
                    #print senCount
            elif string[p + 3] == 'l' and svalW < val:
                #print "lesser"
                if svalW < val and state == 1:
                    state = 0
                    senCount += 1
                    #print senCount
            elif string[p + 3] == 'e' and svalW == val:
                #print "equal"
                if svalW < val and state == 1:
                    state = 0
                    senCount += 1
                    #print senCount
            else:
		#print "inside else"
                if svalW < val and state == 0:
                    state = 1
                if svalW > val and state == 0:
                    state = 1
                if svalW != val and state == 0:
                    state = 1
            if string[p + 9] == 'g' and senCount > uCount:
                breakStatus = whileexe( p+13, wEndPos)
            elif string[p + 9] == 'l' and senCount < uCount:
                breakStatus = whileexe( p+13, wEndPos)
                #print "break status",
                #print breakStatus
            elif string[p + 9] == 'e' and senCount == uCount:
                breakStatus = whileexe( p+13, wEndPos)
            else:
		#print "breaking here"
                break
            if breakStatus ==  breakStatus == 1:
                #print "break inside while "
                breakStatus = 0
                break
#................................../While Function ..............................................
def whileexe(x, y):
    #print "whileexe"
    #print x,
    #print y
    global repEndPos
    global rFlag
    global brCount
    global senEndPos
    global bCount
    global fFlag
    #print string[x:y + 1]
    j = x
    while j <= y:
        if string[j] == "W":
	    j=led(j)
        if string[j] == "T":
	    j=delay(j)
        if string[j] == "M":
	    j=motor(j)
        if string[j] == "Z":
	    j=buzzer(j)
        if string[j] == "L":
	    j=lcd(j)
        if string[j] == "F":
            #.............................................................................
            if j >= senEndPos:
                bCount = 0
                fFlag = 0
                n = j + 1
                #print n
                while n < y:
                    if string[n] == '{':
                        fFlag = 1
                        bCount += 1
                    if string[n] == '}':
                        bCount -= 1
                    if fFlag == 1 and bCount == 0:
                        break
                    n += 1
                #print n
                senEndPos = n
                #print "senEndPos",
                #print senEndPos
                #..............................................................................
            j = senfun(j, y)
            #print "j",
            #print j
        if string[j] == "|":
            pass
        if string[j] == "B":
            #print "break!!"
            return 1
        if string[j] == "R":
            #.........................................................
            if j >= repEndPos:
                brCount = 0
                rFlag = 0
                n = j + 1
                while n < y:
                    if string[n] == '<':
                        rFlag = 1
                        brCount += 1
                    if string[n] == '>':
                        brCount -= 1
                    if rFlag == 1 and brCount == 0:
                        break
                    n += 1
                repEndPos = n
                #print repEndPos,
                #print string[repEndPos]
            #........................................................
            j = repfun(j)
        if j == y + 1:
            #print"break is here"
            return 1
        j += 1
    return j
# .........................................../whileexe function............................................................
# ...............................................sen function...........................................................
def senfun(p, z):
    global senEndPos
    global count
    Ppos = 0
    endPos = 0
    pCount = 1
    pFlag = 1
    eCount = 0
    eFlag = 1
    eeFlag = 0
    v = p + 1
    #print "v",
    #print v
    #print "senEndPos",
    #print senEndPos
    #print "sen"
    if string[p + 1] == 'I' or string[p + 1] == 'i':
        while v <= senEndPos:
            if string[v] == '|' and pFlag == 1:
                pCount -= 1
            if string[v] == 'F' and pFlag == 1:
                pCount += 1
            if pCount == 0 and pFlag == 1:
                Ppos = v
                pFlag = 0
                #print "Ppos  ",
                #print Ppos,
                #print string[Ppos]
            if string[v] == '{' and eFlag == 1:
                eeFlag = 1
                eCount += 1
            if string[v] == '}' and eFlag == 1:
                eCount -= 1
            if eCount == 0 and eFlag == 1 and eeFlag == 1:
                eFlag = 0
                endPos = v
                #print "end pos ",
                #print endPos
            v += 1
        # ...................While ppos...............
        if string[p + 1] == 'I':
            port = string[p + 2]
            val = int(string[p + 4: p + 7])
	    #********************************************
            #sval1 = raw_input("input the sensor value for if on port")
	    FTs = "FV"+port+port+port
	    data = ""
            temp = ""
            por.write(FTs)
            while data != "#":
                data = por.read(1)
                if data == "\n" or data == "\r":
                        data = ""
                temp= temp+data
            #print temp[1:4]
	    #********************************************
            sval1 = int(temp[1:4])
        elif string[p + 1] == 'i':
            var = string[p + 2]
            sval1 = count
            val = int(string[p + 4: p + 7])
        # count = int(string[p + 8])
        breakStatus = 0
        #print "one sensor "
        # ................................................
        if string[p + 3] == 'g' and sval1 > val:
            #print "greater"
            breakStatus = senexe(p + 8, Ppos - 1, z)
        elif string[p + 3] == 'l' and sval1 < val:
            #print "lesser"
            breakStatus = senexe(p + 8, Ppos - 1, z)
        elif string[p + 3] == 'e' and sval1 == val:
            #print "equal"
            breakStatus = senexe(p + 8, Ppos - 1, z)
        elif string[Ppos + 1] != '}':
            #print "else"
            #print Ppos + 1,
            #print endPos - 1,
            #print z,
            breakStatus = senexe(Ppos + 1, endPos - 1, z)
        if breakStatus == 1 or breakStatus == z + 1:
            #print "breakStatus",
            #print breakStatus
            breakStatus = 0
            #print z+1,
            #print "return"
            return z + 1
            # .................................................
    # #print endPos
    return endPos
# .........................................../sen function............................................................
# ...........................................senex function............................................................
def senexe(x, y, z):
    #print "senexe"
    #print x,
    #print y,
    global count
    global state
    global repEndPos
    global rFlag
    global brCount
    global wbCount
    global wFlag
    global whileEndPos
    #print string[x:y + 1]
    h = x
    while h <= y:
        if string[h] == "W":
	    h=led(h)
        if string[h] == "T":
	    h=delay(h)
        if string[h] == "M":
	    h=motor(h)
        if string[h] == "Z":
	    h=buzzer(h)
        if string[h] == "L":
            #print "LCD"
	    h=lcd(h)
        if string[h] == "F":
            h = senfun(h, z)
        if string[h] == "|":
            pass
        if string[h] == "B":
            #print "break!!"
            return 1
        if string[h] == "R":
            #.........................................................
            if h >= repEndPos:
                brCount = 0
                rFlag = 0
                n = h + 1
                while n < y:
                    if string[n] == '<':
                        rFlag = 1
                        brCount += 1
                    if string[n] == '>':
                        brCount -= 1
                    if rFlag == 1 and brCount == 0:
                        break
                    n += 1
                repEndPos = n
                #print repEndPos,
                #print string[repEndPos]
            #........................................................
            h = repfun(h)
        if string[h] == "H":
            if h >= whileEndPos:
                wbCount = 0
                wFlag = 0
                n = h + 1
                while n < y:
                    #print n
                    while n < y:
                        if string[n] == '[':
                            wFlag = 1
                            wbCount += 1
                        if string[n] == ']':
                            wbCount -= 1
                        if wFlag == 1 and wbCount == 0:
                            break
                        n += 1
                    whileEndPos = n
                    #print "whileEndPos",
                    #print whileEndPos
            h = whilefun(h)
        if h == z + 1:
            return 1
        if string[h] == "V":
            if string[h+1] == 'a':
                #print "state",
                #print state
                if string[h+2] == '+':
                    if state == 1:
                        state = 0
                        count += 1
                        #print "count",
                        #print count
                elif string[h+2] == '-':
                    if state == 1:
                        state = 0
                        count -= 1
                        #print "count",
                        #print count
                elif string[h+2] == 'x':
                    if state == 0:
                        state = 1
                        #print "count",
                        #print count
        h += 1
    return h
# .........................................../senex function............................................................
# ...........................................rep function............................................................
def repfun(p):
    global repEndPos
    endrPos = 0
    pCount = 1
    pFlag = 1
    erCount = 0
    erFlag = 1
    eerFlag = 0
    v = p + 1
    re = 1
    # #print "rep"
    re = int(string[p + 1])
    #print "repeat ",
    #print re
    while v <= repEndPos:
        if string[v] == '<' and erFlag == 1:
            eerFlag = 1
            erCount += 1
        if string[v] == '>' and erFlag == 1:
            erCount -= 1
        if erCount == 0 and erFlag == 1 and eerFlag == 1:
            erFlag = 0
            endrPos = v
            #print "end pos ",
            #print endrPos
        v += 1
    # ...................While ppos...............
    rexe(p + 3, endrPos - 1, re)
    # .................................................
    # #print endrPos
    return endrPos
# ........................................../rep function............................................................
# ............................................rexe....................................................................
def rexe(x, y, z):
    global senEndPos
    global whileEndPos
    global bCount
    global fFlag
    global wbCount
    global wFlag
    #print string[x:y + 1]
    #print z,
    #print "repeat"
    b = 0
    if z == 0:
        z = 15000
    while b < z:
        t = x
        while t <= y:
            if string[t] == "W":
		t=led(t)
            if string[t] == "T":
		t=delay(t)
            if string[t] == "Z":
		t=buzzer(t)
            if string[t] == "M":
		t=motor(t)
		#print "motttttttttor"
            if string[t] == "L":
                t=lcd(t)
            if string[t] == "R":
                t = repfun(t)
            if string[t] == "F":
                #.............................................................................
                if t >= senEndPos:
                    bCount = 0
                    fFlag = 0
                    n = t + 1
                    #print n
                    while n < y:
                        if string[n] == '{':
                            fFlag = 1
                            bCount += 1
                        if string[n] == '}':
                            bCount -= 1
                        if fFlag == 1 and bCount == 0:
                            break
                        n += 1
                    #print n
                    senEndPos = n
                    #print "senEndPos",
                    #print senEndPos
                #..............................................................................
                t = senfun(t, y)
            if string[t] == "H":
                if t >= whileEndPos:
                    wbCount = 0
                    wFlag = 0
                    n = t + 1
                    while n < y:
                        #print n
                        while n < y:
                            if string[n] == '[':
                                wFlag = 1
                                wbCount += 1
                            if string[n] == ']':
                                wbCount -= 1
                            if wFlag == 1 and wbCount == 0:
                                break
                            n += 1
                        whileEndPos = n
                        #print "whileEndPos",
                        #print whileEndPos
                h = whilefun(t)
            if t == y + 1:
                #print "break is there"
                return y
            t += 1
        b += 1
# ............................................/rexe...................................................................
#*******************  now ve to add normaal operation and main to the prog ***************

nflag = 0
string = ""
appdata = "Y."
print "starts here"

def main():
	our_thread=threading.Thread(target =no)
	our_thread.setDaemon(True)
	our_thread.start()
	global appdata
	global nflag
	global string
	while 1:
                flagfile=open("flag.txt","r")
                flag = flagfile.readline()
                flagfile.close()
                if flag.strip() == "1":
			print "entered flag if"
                        flagfile=open("flag.txt","w")
                        flagfile.write(str(0)+"\n")
                        flagfile.close()
                        file= open("appdata.txt","r")
                        appdata =file.readline()
                        file.close()
			if appdata.strip()== ".":
		 		filels= open("appdata.txt","w")
	                        filels.write("Y.\n")
        	                filels.close()
				f = open("t_p.txt","w")
                                f.write("0")
                                f.close()
				por.write("N")
				sys.exit(1)
			else:
				nflag = 1
				print "n flagg made 1"

#*************************************************** for integration purpose **************************************



def no():
	global nflag 
	global string 
	global appdata 
	global string 
	global mainFlag 
	global wbCount 
	global wFlag 
	global bCount 
	global fFlag 
	global brCount 
	global rFlag 
	global i 
	global senEndPos 
	global repEndPos 
	global whileEndPos 
	global n 
	global state 
	global senCount 
	while True:	
		if nflag == 1:
			print "data recieved >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"	
			if appdata.strip() != "Y":
				#print "data read"
				string = appdata.strip()
				#*********************
				#string = raw_input("enter the string")
				mainFlag = 1
				senEndPos = 0
				repEndPos = 0
				whileEndPos = 0
				count = 0
				dot = len(string)
				#print "senEndPos",
				#print senEndPos
				#print "dot ",
				#print dot
				i = 0
				if mainFlag == 1:
					while i < dot:
						#.................rudresh edit........................................
						if string[i] == "W":
						    i=led(i)
						if string[i] == "T":
						    i=delay(i)
						if string[i] == "M":
						    i=motor(i)
						if string[i] == "Z":
						    i=buzzer(i)
						if string[i] == "L":
						    i=lcd(i)
						#.................rudresh edit........................................
					#.................WHILE........................................
						if string[i] == 'H':
							wbCount = 0
							wFlag = 0
							if i >= whileEndPos:
								n = i + 1
								while n < dot:
									if string[n] == '[':
										wFlag = 1
										wbCount += 1
									if string[n] == ']':
										wbCount -= 1
									if wFlag == 1 and wbCount == 0:
										break
									n+= 1
								whileEndPos = n
								#print whileEndPos,
								#print string[whileEndPos]
							whilefun(i)
							i = whileEndPos
					#................/WHILE........................................
					# ..............................SEN.........................................................
						if string[i] == 'F':
							bCount = 0
							fFlag = 0
							if i >= senEndPos:
								n = i + 1
								while n < dot:
									if string[n] == '{':
										fFlag = 1
										bCount += 1
									if string[n] == '}':
										bCount -= 1
									if fFlag == 1 and bCount == 0:
										break
									n+= 1
								senEndPos = n
								#print senEndPos,
								#print string[senEndPos]
							senfun(i, 1)
							i = senEndPos
					# ........................../SEN............................................................
					# ...........................REP.............................................................
						if string[i] == 'R':
							brCount = 0
							rFlag = 0
							#print string[i]
							if i >= repEndPos:
								n = i + 1
								while n < dot:
									if string[n] == '<':
										rFlag = 1
										brCount += 1
									if string[n] == '>':
										brCount -= 1
									if rFlag == 1 and brCount == 0:
										break
									n += 1
								repEndPos = n
								#print repEndPos,
								#print string[repEndPos]
							repfun(i)
							#print "i ",
							i = repEndPos
							#print i
					# ............................/REp................................................................
						i += 1
					mainFlag = 0
				#*********************
			nflag = 0
		elif nflag == 0:
			print str(nflag)+" nflag is tthis"
			pass
		time.sleep(1)
main()
print "ends here"

##f inal new main code ()................................................................................................................................

def main1():
	global appdata
	global nflag
	global string
        our_thread=threading.Thread(target =no)
        our_thread.setDaemon(True)
        our_thread.start()
	while 1:
                flagfile=open("flag.txt","r")
                flag = flagfile.readline()
                flagfile.close()
                if flag.strip() == "1":
                        flagfile=open("flag.txt","w")
                        flagfile.write(str(0)+"\n")
                        flagfile.close()
                        file= open("appdata.txt","r")
                        appdata =file.readline()
                        file.close()
			if appdata.strip().startswith("U[") :
                        	file= open("appdata.txt","w")
	                        file.write("Y")
         	                file.close()
				s=appdata.strip()
				data= s.split("|")
				#print data[]
				#print data[2]
				file=open("wifi_mode.txt","w")
				file.write("s")
				file.close()
				os.chdir("/etc/network")
				os.system("rm interfaces")
				file = open("interfaces.stamode","r")
				lines = file.readlines()
				i=0
				for line in lines:
				        if re.search("wpa-ssid",lines[i]):
				                lines[i] = "\twpa-ssid "+"\""+data[0][2:]+"\""
				        if re.search("wpa-psk",lines[i]):
				                lines[i] = "\n\twpa-psk "+"\""+data[1][:-2]+"\""
				        i=i+1
				file=open("interfaces","w")
				for lin in  lines:
				        #print lin
				        file.write(lin)
				file.close()
				por.write("N")
				time.sleep(.05)
				os.system("reboot")

			if appdata.strip()== ".":
		 		filels= open("appdata.txt","w")
	                        filels.write("Y.\n")
        	                filels.close()
				f = open("t_p.txt","w")
                                f.write("0")
                                f.close()
				por.write("N")
				sys.exit(1)
			if appdata.strip()== "Y.":
				print "yahooooooooooooooooooooooooooooooooooooooooo"
				f = open("t_p.txt","w")
                                f.write("0")
                                f.close()
				f = open("yahooooooooooooot.txt","w")
                                f.write("0")
                                f.close()
			if appdata.strip().startswith("#A"):
				os.system("clear")
				y=appdata.strip()	
				Upart =re.findall("AU\([^\(]*\)",y)[0][3:-1]+"."
		                Dpart =re.findall("AD\([^\(]*\)",y)[0][3:-1]+"."
                		Rpart =re.findall("AR\([^\(]*\)",y)[0][3:-1]+"."
		                Lpart =re.findall("AL\([^\(]*\)",y)[0][3:-1]+"."
				while True:
					
                			flagfile=open("flag.txt","r")
			                flag = flagfile.readline()
			                flagfile.close()
                			if flag.strip() == "1":
						flagfile=open("flag.txt","w")
			                        flagfile.write(str(0)+"\n")
                        			flagfile.close()
			                        file= open("appdata.txt","r")
                        			appdata =file.readline()
			                        #print "*****inside acc***********"
                        			print appdata.strip()
			                        #print "*****inside acc***********"
                        			file.close()
                        			Adata=appdata
			                        #print  "*"+Adata+"**"
        	                		if Adata.strip() == "AU":
        		                	        print "up"
        	                		if Adata.strip() == "AD":
        		                	        print "down"
        	                		if Adata.strip() == "AL":
        		                	        print "left"
        	                		if Adata.strip() == "AR":
        		                	        print "right"
						elif Adata.strip() == "AX":
							por.write("N")
							time.sleep(.05)
                                			
                        			elif Adata.strip() == ".":
                        			        sys.exit(1)


			else:
				nflag = 1

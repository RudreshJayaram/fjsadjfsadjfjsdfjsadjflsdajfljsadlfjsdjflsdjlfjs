
############################## adding the new part to the code ###########################################################################################################################################################
BracketList = []
RepeatCountList = []
Bi= 0
Ri = 0
i = 0

String = "#W255,000,000,."
def repeat4function():	
	global Bi
	global Ri
	global i
	if String[BracketList[Bi+2]] == "<" and String[BracketList[Bi+5]] == ">":
		for i in range(0, RepeatCountList[Ri]):
			tempi = i
			tempBi = Bi
			tempRi = Ri
			basicrepeat(1, BracketList[Bi]+1 ,BracketList[Bi+1]-3)
			Ri=Ri+1
			Bi=Bi+1
			i=BracketList[Bi+1]
			repeat3functionfor4()
			basicrepeat(1, BracketList[Bi]+1 ,BracketList[Bi+1])
			i = tempi
			Bi = tempBi
			Ri = tempRi
		i=BracketList[Bi+7]
		Bi=Bi+8
		Ri=Ri+4
	elif String[BracketList[Bi+2]] == ">" and String[BracketList[Bi+5]] == ">":		
		for i in range(0, RepeatCountList[Ri]):
			tempi = i
			tempBi = Bi
			tempRi = Ri
			Ri=Ri+1
			basicrepeat(1, BracketList[Bi]+1 ,BracketList[Bi+1]-3)
			Bi=Bi+1
			i=BracketList[Bi+1]
			basicrepeat( RepeatCountList[Ri],BracketList[Bi]+1, BracketList[Bi+1])
			Ri=Ri+1
			Bi=Bi+1
			i=BracketList[Bi+1]
			
			basicrepeat(1, BracketList[Bi]+1 ,BracketList[Bi+1]-3)
			Bi=Bi+1
			i=BracketList[Bi+1]
			repeat2functionfor2()
			Bi=Bi-1
			#print Bi
			#print Ri
			basicrepeat(1, BracketList[Bi]+1 ,BracketList[Bi+1])
			i = tempi
			Bi = tempBi
			Ri = tempRi
		i=BracketList[Bi+7]
		Bi=Bi+8
		Ri=Ri+4
	elif String[BracketList[Bi+2]] == "<" and String[BracketList[Bi+5]] == "<":
		for i in range(0, RepeatCountList[Ri]):
			tempi = i
			tempBi = Bi
			tempRi = Ri
			Ri=Ri+1
			basicrepeat(1, BracketList[Bi]+1 ,BracketList[Bi+1]-3)
			Bi=Bi+1
			i=BracketList[Bi+1]
			repeat2functionfor2()
			Bi=Bi-1
			basicrepeat(1, BracketList[Bi]+1 ,BracketList[Bi+1]-3)
			Bi=Bi+1
			basicrepeat(RepeatCountList[Ri], BracketList[Bi]+1 ,BracketList[Bi+1])
			Ri=Ri+1
			Bi=Bi+1
			basicrepeat(1, BracketList[Bi]+1 ,BracketList[Bi+1])
			i = tempi
			Bi = tempBi
			Ri = tempRi
		i=BracketList[Bi+7]
		Bi=Bi+8
		Ri=Ri+4
	elif String[BracketList[Bi+2]] == ">" and String[BracketList[Bi+5]] == "<":
		for i in range(0, RepeatCountList[Ri]):
			tempi = i
			tempBi = Bi
			tempRi = Ri
			Ri=Ri+1
			basicrepeat(1, BracketList[Bi]+1 ,BracketList[Bi+1]-3)
			Bi=Bi+1
			i=BracketList[Bi+1]
			basicrepeat(RepeatCountList[Ri], BracketList[Bi]+1 ,BracketList[Bi+1])
			Ri=Ri+1
			Bi=Bi+1
			basicrepeat(1, BracketList[Bi]+1 ,BracketList[Bi+1]-3)
			Bi=Bi+1
			basicrepeat(RepeatCountList[Ri], BracketList[Bi]+1 ,BracketList[Bi+1])
			Ri=Ri+1
			Bi=Bi+1
			basicrepeat(1, BracketList[Bi]+1 ,BracketList[Bi+1]-3)
			Bi=Bi+1
			basicrepeat(RepeatCountList[Ri], BracketList[Bi]+1 ,BracketList[Bi+1])
			Ri=Ri+1
			Bi=Bi+1
			basicrepeat(1, BracketList[Bi]+1 ,BracketList[Bi+1])
			i = tempi
			Bi = tempBi
			Ri = tempRi
		i=BracketList[Bi+7]
		Bi=Bi+8
		Ri=Ri+4		
#######################################################################################################################################################
def stringdataextractor(String):
	if String != "Y":
		for k in range(0, len(String)):
			if String[k] == "<" or String[k] == ">":
				BracketList.append(k)
				if String[k] == "<":
					RepeatCountList.append(int(String[k-2:k]))
	else :
		#print  "in pause"
		pass

def basicrepeat(NoOfTimes, Start, End):
	global i
	i=Start
	for j in range(0, NoOfTimes):
		stringiterator_for_repeat(End)
		i = Start
	

def repeat2functionfor3():
	global Bi
	global Ri
	global i
	for k in range(0,RepeatCountList[Ri]):
		basicrepeat(1,BracketList[Bi]+1 ,BracketList[Bi+1]-3)
		basicrepeat(RepeatCountList[Ri+1],BracketList[Bi+1]+1 ,BracketList[Bi+2])
		basicrepeat(1,BracketList[Bi+2]+1 ,BracketList[Bi+3])
	i=BracketList[Bi+3]
	Bi=Bi+3
	Ri=Ri+1

def repeat2functionfor2():
	global Bi
	global Ri
	global i
	for k in range(0,RepeatCountList[Ri]):
		basicrepeat(1,BracketList[Bi]+1 ,BracketList[Bi+1]-3)
		basicrepeat(RepeatCountList[Ri+1],BracketList[Bi+1]+1 ,BracketList[Bi+2])
		basicrepeat(1,BracketList[Bi+2]+1 ,BracketList[Bi+3])
	i=BracketList[Bi+3]
	Bi=Bi+4
	Ri=Ri+2

def repeat3function():	
	global Bi
	global Ri
	global i
	if String[BracketList[Bi+2]] == "<":
		for j in range(0,RepeatCountList[Ri]):
			tempi = i
			tempBi = Bi
			tempRi = Ri
			basicrepeat(1,BracketList[Bi]+1 ,BracketList[Bi+1]-3)
			Ri=Ri+1
			Bi=Bi+1
			i=BracketList[Bi+1]
			repeat2functionfor3()
			basicrepeat(1,BracketList[Bi]+1 ,BracketList[Bi+1])
			i = tempi
			Bi = tempBi
			Ri = tempRi
	
		i=BracketList[Bi+5]
		Bi=Bi+6
		Ri=Ri+3 
		
	elif String[BracketList[Bi+2]] == ">":
		#print "#################################################"
		for j in range(0, RepeatCountList[Ri]):
			tempi = i
			tempBi = Bi
			tempRi = Ri
			basicrepeat(1,BracketList[Bi]+1 ,BracketList[Bi+1]-3)
			basicrepeat(RepeatCountList[Ri+1],BracketList[Bi+1]+1 ,BracketList[Bi+2])
			basicrepeat(1,BracketList[Bi+2]+1 ,BracketList[Bi+3]-3)
			basicrepeat(RepeatCountList[Ri+2],BracketList[Bi+3]+1 ,BracketList[Bi+4])
			basicrepeat(1,BracketList[Bi+4]+1 ,BracketList[Bi+5])
			i = tempi
			Bi = tempBi
			Ri = tempRi
		i=BracketList[Bi+5]
		Bi=Bi+6
		Ri=Ri+3
def repeat3functionfor4():	
	global Bi
	global Ri
	global i
	if String[BracketList[Bi+2]] == "<":
		#print "#######################"+String[BracketList[Bi+2]]
		for j in range(0,RepeatCountList[Ri]):
			tempi = i
			tempBi = Bi
			tempRi = Ri
			basicrepeat(1,BracketList[Bi]+1 ,BracketList[Bi+1]-3)
			Ri=Ri+1
			Bi=Bi+1
			i=BracketList[Bi+1]
			repeat2functionfor3()
			basicrepeat(1,BracketList[Bi]+1 ,BracketList[Bi+1])
			i = tempi
			Bi = tempBi
			Ri = tempRi
	
		i=BracketList[Bi+5]
		Bi=Bi+5
		Ri=Ri+3 
			
	elif String[BracketList[Bi+2]] == ">":
		#print "#################################################"
		for j in range(0, RepeatCountList[Ri]):
			tempi = i
			tempBi = Bi
			tempRi = Ri
			basicrepeat(1,BracketList[Bi]+1 ,BracketList[Bi+1]-3)
			basicrepeat(RepeatCountList[Ri+1],BracketList[Bi+1]+1 ,BracketList[Bi+2])
			basicrepeat(1,BracketList[Bi+2]+1 ,BracketList[Bi+3]-3)
			basicrepeat(RepeatCountList[Ri+2],BracketList[Bi+3]+1 ,BracketList[Bi+4])
			basicrepeat(1,BracketList[Bi+4]+1 ,BracketList[Bi+5])
			i = tempi
			Bi = tempBi
			Ri = tempRi
		i=BracketList[Bi+5]
		Bi=Bi+6
		Ri=Ri+3
	





def loopdecider():
	global Bi
	global Ri
	global i

	if String[i-1] == "4":
		repeat4function()
		
	if String[i-1] == "3":
		repeat3function()
		
	if String[i-1] == "1":
		basicrepeat(RepeatCountList[Ri],BracketList[Bi]+1 ,BracketList[Bi+1])
		i=BracketList[Bi+1]
		Bi=Bi+2
		Ri=Ri+1

	if String[i-1] == "2":
		repeat2functionfor2()

def finalstringprocessor(String):
	global Bi
	global Ri
	global i 
	Bi= 0
	Ri = 0
	i = 0	
	while i<len(String):
		#print "**"+String[i]+"**"
		if String[i] == "R":
			loopdecider()
		i=i+1					

	

def LED():
	time.sleep(0.005)	
	global String
	global i
	por.write(String[i:i+13])
	i=i+13

def BUZZER():
	time.sleep(0.005)
	global i
	por.write(String[i:i+4])
	i=i+4

def DELAY():
	#print "delay"
	global i
	if String[i+5] == "m":
		time.sleep(int(String[i+1:i+5])/1000.0)
		i=i+7
	elif String[i+5] == "s":
		time.sleep(int(String[i+1:i+5]))
		i=i+7
#******************************************************************************************************************************

def LCD():
	print "lcd"
	time.sleep(.005)
	global i
	por.write(String[i:i+38])	
	i=i+38
def stringiterator_for_repeat(end):
	global i			
	while i<end:
		if String[i] == "W":
			LED()				
		elif String[i] == "Z":
			BUZZER()	
		elif String[i] == "L":
			LCD()
		elif String[i] == "T":
			DELAY()
		elif String[i] == "F":
			sensor()
		elif String[i] == "M":
			MOTOR()
		elif String[i] == "#":
			i=i+1
		else:
			i = i+1

def stringiterator_for_sensor(end):
	global i			
	while i<end:
		if String[i] == "W":
			LED()				
		elif String[i] == "Z":
			BUZZER()	
		elif String[i] == "L":
			LCD()
		elif String[i] == "Q":
			touch()
		elif String[i] == "T":
			DELAY()
		elif String[i] == "M":
			MOTOR()
		elif String[i] == "R":
			loopdecider()
		else:
			i=i+1
		
		

def MOTOR():
	global i
	time.sleep(0.005)
	print String[i+1]
	if int(String[i+1]) <=2:
		por.write(String[i:i+4])
		i=i+4
	else :
		pass	

def main_stringiterator():
	s=time.time()	
	global Bi
	global Ri
	global i 
	Bi= 0
	Ri = 0
	i = 0			
	#print String + "2>>>>>>>>>>>>>>>>>>>>>>>>string iterator>>>>>>>>>>>>>>>>>>>>>."
	if String[i]=="Y":
		return 0
	slen = len(String)
	while i<slen:
	#hile String[i]!=".":
		elif String[i] == "W":
			LED()				
		elif String[i] == "Z":
			BUZZER()	
		elif String[i] == "L":
			LCD()
		elif String[i] == "T":
			DELAY()
		elif String[i] == "M":
			#print "Motor" 
			MOTOR()
		elif String[i] == "R":
			loopdecider()
			
		else:
			i=i+1
	#print time.time()-s	
#****************************************************************************************************************************************************************************					
String = "W255,000,000,."
stringdataextractor(String)
por.write("N")
time.sleep(0.5)
main_stringiterator()

############################## adding the new part to the code ###########################################################################################################################################################

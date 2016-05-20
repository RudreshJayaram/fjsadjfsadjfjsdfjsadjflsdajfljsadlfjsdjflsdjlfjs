
##f inal new main code () 

def main():
	global appdata
	global nflag
	global string
        our_thread=threading.Thread(target =normaloperation)
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

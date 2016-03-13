import time
import os
os.chdir("/root/revolution")
#************************** This is the uart mode set up *********************************************
os.system("mv /boot/cmdline.txt /boot/cmdline.txt.bkp")
os.system("cp cmdline.txt.grp /boot/cmdline.txt")
os.system("mv /etc/inittab /etc/inittab.bkp")
os.system("cp inittab.grp /etc/inittab")

#************************** This is the apn mode set up *********************************************
os.system("mv  /etc/dhcp/dhcpd.conf  /etc/dhcp/dhcpd.conf.bkp")
os.system("cp dhcpd.conf.grp  /etc/dhcp/dhcpd.conf")

os.system("mv /etc/default/isc-dhcp-server /etc/default/isc-dhcp-server.bkp")
os.system("cp isc-dhcp-server.grp /etc/default/isc-dhcp-server")

os.system("mv /etc/network/interfaces /etc/network/interfaces.bkp")
file=open("/root/revolution/wifi_mode.txt","r")
mode = file.read()
file.close()

if mode.strip() == "s":
	os.system("cp /etc/network/interfaces.stamode /etc/network/interfaces")
elif mode.strip() == "a":
	os.system("cp /etc/network/interfaces.apnmode /etc/network/interfaces")
print mode
os.system("mv /etc/hostapd/hostapd.conf /etc/hostapd/hostapd.conf.bkp") 
os.system("cp hostapd.conf.grp /etc/hostapd/hostapd.conf")

os.system("mv /etc/default/hostapd /etc/default/hostapd.bkp")
os.system("cp hostapd.grp /etc/default/hostapd")

os.system("mv /etc/sysctl.conf /etc/sysctl.conf.bkp")
os.system("cp sysctl.conf.grp /etc/sysctl.conf")

os.system("mv /etc/rc.local /etc/rc.local.bkp")
os.system("cp rc.local.grp /etc/rc.local")
os.system( "chmod 777 /etc/rc.local")

os.system("mv  /etc/bash.bashrc /etc/bash.bashrc.bkp")
file = open("/etc/bash.bashrc","a")
file.write( "alias ls=\"export GLOBIGNORE_TMP=$GLOBIGNORE; export GLOBIGNORE=$GLOBIGNORE:.*:$(tr \'\\n\' \':\' < /root/.hidden); ls -dC * ;export GLOBIGNORE=$GLOBIGNORE_TMP; export GLOBIGNORE_TMP=\'\'\"")
file.close()
os.system("clear")
time.sleep(2)

print "all done"
#os.system("sudo reboot")


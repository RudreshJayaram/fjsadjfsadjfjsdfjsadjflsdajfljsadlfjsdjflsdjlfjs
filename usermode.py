import time
import os
os.system("mv /boot/cmdline.txt.bkp /boot/cmdline.txt")
os.system("mv /etc/inittab.bkp /etc/inittab")
os.system("mv  /etc/dhcp/dhcpd.conf.bkp  /etc/dhcp/dhcpd.conf")
os.system("mv /etc/default/isc-dhcp-server.bkp /etc/default/isc-dhcp-server")
os.system("mv /etc/network/interfaces.bkp /etc/network/interfaces")
os.system("mv /etc/hostapd/hostapd.conf.bkp /etc/hostapd/hostapd.conf") 
os.system("mv /etc/default/hostapd.bkp /etc/default/hostapd")
os.system("mv /etc/sysctl.conf.bkp /etc/sysctl.conf")
os.system("mv /etc/rc.local.bkp /etc/rc.local")
os.system( "chmod 777 /etc/rc.local")
os.system("mv  /etc/bash.bashrc.bkp /etc/bash.bashrc")
os.system("clear")
time.sleep(2)
print "all done"
#os.system("sudo reboot")


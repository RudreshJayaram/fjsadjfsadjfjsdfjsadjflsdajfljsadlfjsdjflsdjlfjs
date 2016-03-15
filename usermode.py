import time
import os
os.system("mv  /etc/dhcp/dhcpd.conf.bkp  /etc/dhcp/dhcpd.conf")
os.system("mv /etc/default/isc-dhcp-server.bkp /etc/default/isc-dhcp-server")
os.system("mv /etc/network/interfaces.bkp /etc/network/interfaces")
os.system("mv /etc/hostapd/hostapd.conf.bkp /etc/hostapd/hostapd.conf") 
os.system("mv /etc/default/hostapd.bkp /etc/default/hostapd")
os.system("mv /etc/sysctl.conf.bkp /etc/sysctl.conf")
os.system("mv  /etc/bash.bashrc.bkp /etc/bash.bashrc")
os.system("sudo reboot")


import time
import os
#os.system("sudo apt-get update")
os.chdir("/root/")

#************************** This is the servoblaster installation ***********************************
os.system("git clone https://github.com/richardghirst/PiBits.git")
os.chdir("PiBits/ServoBlaster/user/")
os.system("make servod")
os.system("./servod")
os.chdir("/root/")


os.system("git clone https://github.com/RudreshJayaram/revolution.git")
os.chdir("revolution")
os.system("cp /root/PiBits/ServoBlaster/user/mailbox.c mailbox.c")
os.system("cp /root/PiBits/ServoBlaster/user/mailbox.h mailbox.h")
os.system("cp /root/PiBits/ServoBlaster/user/Makefile Makefile")
os.system("make servod")
os.system("./servod")
#************************** This is the uart mode set up *********************************************
os.system("mv /boot/cmdline.txt /boot/cmdline.txt.bkp")
os.system("cp cmdline.txt.grp /boot/cmdline.txt")
os.system("mv /etc/inittab /etc/inittab.bkp")
os.system("cp inittab.grp /etc/inittab")

#************************** This is the apn mode set up *********************************************
os.system("sudo apt-get install hostapd isc-dhcp-server")
os.system("mv  /etc/dhcp/dhcpd.conf  /etc/dhcp/dhcpd.conf.bkp")
os.system("cp dhcpd.conf.grp  /etc/dhcp/dhcpd.conf")

os.system("mv /etc/default/isc-dhcp-server /etc/default/isc-dhcp-server.bkp")
os.system("cp isc-dhcp-server.grp /etc/default/isc-dhcp-server")

os.system("sudo ifdown wlan0")

os.system("mv /etc/network/interfaces /etc/network/interfaces.bkp")
os.system("mv interfaces.stamode /etc/network/")
os.system("mv interfaces.apnmode /etc/network/")
os.system("cp /etc/network/interfaces.apnmode /etc/network/interfaces")

os.system("sudo ifconfig wlan0 1.2.3.4")


os.system("mv /etc/hostapd/hostapd.conf /etc/hostapd/hostapd.conf.bkp") 
os.system("cp hostapd.conf.grp /etc/hostapd/hostapd.conf")


os.system("mv /etc/default/hostapd /etc/default/hostapd.bkp")
os.system("cp hostapd.grp /etc/default/hostapd")

os.system("mv /etc/sysctl.conf /etc/sysctl.conf.bkp")
os.system("cp sysctl.conf.grp /etc/sysctl.conf")
os.system("sudo sh -c \"echo 1 > /proc/sys/net/ipv4/ip_forward\"")


os.system("sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE")
os.system("sudo iptables -A FORWARD -i eth0 -o wlan0 -m state --state RELATED,ESTABLISHED -j ACCEPT")
os.system("sudo iptables -A FORWARD -i wlan0 -o eth0 -j ACCEPT")


os.system("sudo iptables -t nat -S")
os.system("sudo iptables -S")

os.system("sudo sh -c \"iptables-save > /etc/iptables.ipv4.nat\"")
os.system("wget http://adafruit-download.s3.amazonaws.com/adafruit_hostapd_14128.zip")
os.system("unzip adafruit_hostapd_14128.zip")
os.system("sudo mv /usr/sbin/hostapd /usr/sbin/hostapd.ORIG")
os.system("sudo mv hostapd /usr/sbin")
os.system("sudo chmod 755 /usr/sbin/hostapd")
os.system("sudo service hostapd start")
os.system("sudo service isc-dhcp-server start")
os.system("sudo service hostapd status")
os.system("sudo service isc-dhcp-server status")

os.system("sudo update-rc.d hostapd enable")
os.system("sudo update-rc.d isc-dhcp-server enable")
os.system("sudo mv /usr/share/dbus-1/system-services/fi.epitest.hostap.WPASupplicant.service ~/")

#os.system("mv /etc/rc.local /etc/rc.local.bkp")
os.system("cp rc.local.grp /etc/rc.local")
os.system( "chmod 777 /etc/rc.local")

os.system("mv bt.py /root/")
os.chdir("/root/revolution")
os.system("mv  /root/revolution/.hidden /root/.hidden")

os.system("cp  /etc/bash.bashrc /etc/bash.bashrc.bkp")
file = open("/etc/bash.bashrc","a")
file.write( "alias ls=\"export GLOBIGNORE_TMP=$GLOBIGNORE; export GLOBIGNORE=$GLOBIGNORE:.*:$(tr \'\\n\' \':\' < /root/.hidden); ls -dC * ;export GLOBIGNORE=$GLOBIGNORE_TMP; export GLOBIGNORE_TMP=\'\'\"")
file.close()
os.system("clear")
time.sleep(2)

print "all done"
os.system("sudo reboot")


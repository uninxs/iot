#Practical 5 - IOT based Web Automation
#Connection:
#Connect Pin no.3 (GPIO 2) to LED1 of LED module
#Connect Pin no.6 (GND) to GND of LED module
#Commands: It should be executed in Terminal.
 sudo apt-get update
 sudo apt-get upgrade
 cd/home/pi/Downloads (Move to the downloaded folder)
 tar xvzf WebIOPi-0.7.1.tar.gz
 cd WebIOPi-0.7.1
 wget https://raw.githubusercontent.com/doublebind/raspi/master/webiopipi2bplus.patch
 patch -p1 -i webiopi-pi2bplus.patch
 sudo ./setup.sh
 sudo reboot
 sudo webiopi -d -c/etc/webiopi/config

Go to Web browser
Type http://172.16.250.200:8000/
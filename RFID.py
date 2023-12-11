#Practical 3 -Rfid
#Connection:
#Connect TX of Card Reader to RX of TTL
#Connect GND of Card Reader to GND of TTL
#Connect Red of Power Supply to VCC of Card Reader
#Connect Black of Power Supply to GND of Card Reader
#Connect TTL to Raspberry Pi
#Code:
import RPi.GPIO as GP
import time
import serial
GP.setmode(GP.BOARD)
def read_rfid():
ser=serial.Serial(“/dev/ttyUSB0”)
ser.baudrate=9600
data=ser.read(12)
ser.close()
return data
try:
while True:
id=read_rfid()
print(id)
if id==b’1D00AF5623C7’:
print (“Access Granted”)
time.sleep(2)
else:
print (“Access Denied”) time.sleep(2) finally:
GP.cleanup()

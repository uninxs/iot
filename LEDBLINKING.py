#Practical 1 - Led blinking
#Connection:
#Connect Pin no.7 (GPIO 4) to LED1 of LED module
#Connect Pin no.11 (GPIO 17) to LED2 of LED module
#Connect Pin no.13 (GPIO 27) to LED3 of LED module
#Connect Pin no.15 (GPIO 22) to LED4 of LED module
#Connect Pin no.6 (GND) to GND of LED module
#Code:
import RPi.GPIO as GP 
import time 
GP.setmode(GP.BOARD) 
GP.setup(7,GP.OUT) 
GP.setup(11,GP.OUT)
GP.setup(13,GP.OUT) 
GP.setup(15,GP.OUT) 
while (1): 
GP.output(7,GP.HIGH) 
time.sleep(0.2) 
GP.output(11,GP.LOW) 
time.sleep(0.2) 
GP.output(13,GP.HIGH)
time.sleep(0.2) 
GP.output(15,GP.LOW) 
time.sleep(0.2) 
print (" LED IS ON! ") 
GP.cleanup()

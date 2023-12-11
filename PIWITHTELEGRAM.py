#Practical 6 - Controlling Raspberry Pi with Telegram
#Connection:
#Connect Pin no.3 (GPIO 2) to LED1 of LED module
#Connect Pin no.6 (GND) to GND of LED module
#Step 1: Install Telegram Bot on Raspberry Pi.
 sudo apt-get update
 sudo apt-get upgrade
 sudo apt-get install python-pip
 sudo pip install telepot
#Step 2: Create a Bot in your Telegram App.
#Code:
import time,datetime 
import RPi.GPIO as GP 
import telepot
import sys
def on(pin): 
GP.output(pin, GP.HIGH) 
def off(pin): 
GP.output(pin, GP.LOW)
return
GP.setmode(GP.BOARD) 
GP.setwarnings(False) 
GP.setup(3, GP.OUT) 
def handle(msg): 
chat id = msg['chat']['id'] 
command = msg['text'] 
print ('Got command: %s' % command) 
if command == '/on':
bot.sendMessage(chat_id, on(3)) 
elif command == '/off':
bot.sendMessage(chat_id, off(3)) 
bot = telepot.Bot('Enter_your_bot_token_here')
bot.message_loop(handle) 
print ("I am Listening...") 
while 1:
try:
time.sleep(10) 
except KeyboardInterrupt: 
print ('Program interrupted') 
GP.cleanup()
exit()
except:
print (‘Other error’) 
GP.cleanup()
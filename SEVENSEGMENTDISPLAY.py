#Practical 2 - time on seven segment display
#Connection:
#Pin no.16 (GPIO 23) to CLK of Timer
#Pin no.18 (GPIO 24) to DIO of Timer
#Pin no.4 (5V Power) to VCC of Timer
#Pin no.6 (GND) to GND of Timer
#Code:
from time import sleep
import tm1637
try:
import Thread
except:
from threading import Thread
Display = tm1637.TM1637(CLK=21, DIO=20, brightness=1.0)
try:
print(“Starting”)
Display.StartClock(military_time=True)
Display.SetBrightness(1.0)
while(True):
Display.ShowDoublePoint(True)
sleep(1)
Display.ShowDoublePoint(False)
sleep(1)
Display.ShowDoublePoint(False)
sleep(1)
Display.StopClock()
Thread.interrupt_main()
except KeyboardInterrupt:
print(“Closing”)
Display.cleanup()
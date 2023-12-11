#Practical 4 - Camera
#Commands: To install Pi-camera packages.
# sudo apt-get install python-picamera
# sudo apt-get install python3-picamera
# sudo pip install picamera
#Code:
import time
import picamera
camera=picamera.PiCamera()
camera.resolution=(1024,768) 
camera.start_preview()
time.sleep(2)
camera.capture(‘/home/pi/Desktop/visitor/images%s.jpg’)
camera.stop_preview
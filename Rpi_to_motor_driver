import RPi.GPIO as GPIO
from time import sleep
import board
import Adafruit_CharLCD as LCD
# Raspberry Pi pin setup
lcd_rs = 0
lcd_en = 5
lcd_d4 = 6
lcd_d5 = 19
lcd_d6 = 26
lcd_d7 = 21
lcd_backlight = 2
#
# Pins for Motor Driver Inputs
Motor1A = 4
Motor1B = 17
Motor1E = 12
Motor2A = 27
Motor2B = 22
Motor2E = 13
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(Motor1A,GPIO.OUT)  
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)
GPIO.setup(Motor2A,GPIO.OUT)  
GPIO.setup(Motor2B,GPIO.OUT)
GPIO.setup(Motor2E,GPIO.OUT)
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(Motor1E , 1)
GPIO.output(Motor2E , 1)
while True:            
    input_state = GPIO.input(14)
    if input_state == 'w':
        #Forward
                GPIO.output(Motor1A , 1)
                GPIO.output(Motor1B , 0)
                GPIO.output(Motor2A , 1)
                GPIO.output(Motor2B , 0)
    if input_state == 's':
        #Reverse
                GPIO.output(Motor1A , 0)
                GPIO.output(Motor1B , 1)
                GPIO.output(Motor2A , 0)
                GPIO.output(Motor2B , 1)
    if input_state == 'a':
        #Left
                GPIO.output(Motor1A , 0)
                GPIO.output(Motor1B , 1)
                GPIO.output(Motor2A , 1)
                GPIO.output(Motor2B , 1)
    if input_state == 'd':
          #Right
                GPIO.output(Motor1A , 1)
                GPIO.output(Motor1B , 0)
                GPIO.output(Motor2A , 0)
                GPIO.output(Motor2B , 0)
     if input_state == 'x':
               #Stop
                GPIO.output(Motor1A , 0)
                GPIO.output(Motor1B , 0)
                GPIO.output(Motor2A , 0)
                GPIO.output(Motor2B , 0)

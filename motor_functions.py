import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

E1 = 2 #Left motor
E2 = 3  #Right motor
M1 = 4  #Input pin 1 for motor 1 
M2 = 17 #Input pin 2 for motor 1
M3 = 27 #Input pin 1 for motor 2
M4 = 22 #Input pin 2 for motor 2

pwm = GPIO.PWM(12, 100) #settuping up pin 12 for images hor 100 hz frequency

GPIO.setup(M1, GPIO.OUT)
GPIO.setup(M2, GPIO.OUT)
GPIO.setup(M3, GPIO.IN)
GPIO.setup(M4, GPIO.IN)

#function for both enabling and disbling
def enable(p):
    if p=='E1':
        GPIO.output(E1, GPIO.HIGH)  #Enabling right turn
        GPIO.output(E2, GPIO.LOW)
    elif p=='E2':
        GPIO.output(E2, GPIO.HIGH)  #Enabling left turn
        GPIO.output(E1, GPIO.LOW)
    elif p=='E3':
        GPIO.output(E1, GPIO.HIGH)  #Enabling  both motors
        GPIO.output(E2, GPIO.HIGH)
    else:
        GPIO.output(E1, GPIO.LOW)   #Disabling both motors
        GPIO.output(E2, GPIO.LOW)

#function for anti clockwise motor rotation (reverse motion) 
def reverse(t):
    enable('E3')
    GPIO.output(M1, GPIO.LOW) 
    GPIO.output(M2, GPIO.HIGH)
    GPIO.output(M3, GPIO.LOW)
    GPIO.output(M4, GPIO.HIGH)
    set_time(t) #for each action some time is spent
    #speed()

#function for clockwise motor rotation (straight motion) 
def forward(t):
    enable('E3')
    GPIO.output(M2, GPIO.LOW) 
    GPIO.output(M1, GPIO.HIGH)
    GPIO.output(M4, GPIO.LOW)
    GPIO.output(M3, GPIO.HIGH)
    set_time(t)
    #speed()

#function stops right motor
def right(t):
    enable('E1')
    GPIO.output(M2, GPIO.HIGH) 
    GPIO.output(M1, GPIO.LOW)
    set_time(t)
#function stops left motor
def left(t):
    enable('E2')
    GPIO.output(M4, GPIO.LOW)
    GPIO.output(M3, GPIO.HIGH)
    set_time(t)

def set_time(t):
    return time.sleep(0.5*t)

while True:
    #image_capture()
    #the function returns 



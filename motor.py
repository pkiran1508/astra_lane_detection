import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

en1 = 7
en2 = 12
inp11 = 11
inp12 = 13
inp21 = 16
inp22 = 18

GPIO.setup(en1, GPIO.OUT)
GPIO.setup(en2, GPIO.OUT)
GPIO.setup(inp11, GPIO.OUT)
GPIO.setup(inp12, GPIO.OUT)
GPIO.setup(inp21, GPIO.OUT)
GPIO.setup(inp22, GPIO.OUT)


def enable():
    GPIO.output(en1, 1)
    GPIO.output(en2, 1)


def disable():
    GPIO.output(en1, 0)
    GPIO.output(en2, 0)


def forward():
    GPIO.output(inp11, 1)
    GPIO.output(inp21, 1)
    GPIO.output(inp12, 0)
    GPIO.output(inp22, 0)


def backward():
    GPIO.output(inp11, 0)
    GPIO.output(inp21, 0)
    GPIO.output(inp12, 1)
    GPIO.output(inp22, 1)


def left():
    GPIO.output(inp11, 0)
    GPIO.output(inp21, 1)
    GPIO.output(inp12, 0)
    GPIO.output(inp22, 0)


def right():
    GPIO.output(inp11, 1)
    GPIO.output(inp21, 0)
    GPIO.output(inp12, 0)
    GPIO.output(inp22, 0)


def direction(x):
    if x == '1':  # Move Forward
        forward()
        time.sleep(2)

    if x == '2':  # Move Backward
        backward()
        time.sleep(2)

    if x == '3':  # Turn Left
        left()
        time.sleep(2)

    if x == '4':  # Turn Right
        right()
        time.sleep(2)


while True:
    c = input()
    if c == 's':  # Start/Stop
        disable()

    elif c == 'speed':
        s = int(input())  # percentage speed
        move = input()
        s = s / 100.0
        for i in range(100):
            enable()
            direction(move)
            time.sleep(s * 0.1)
            disable()
            time.sleep((1 - s) * 0.1)

    else:
        enable()
        direction(c)

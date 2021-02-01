# !/bin/python3
# code.py
# Author: Advik Singhania
# Date: 1st February, 2021
# Board: Seeeduino Xiao (32-bit Cortex M0+)
''' CircuitPython code for Line Follower Robot made using Seeeduino Xiao'''

# Importing required built-in libraries
import board  # For pin definitions
import digitalio  # For digital input/output
import time  # For delays
import analogio  # For analog input

led = digitalio.DigitalInOut(board.D13)  # LED at pin 13 (built-in)
led.direction = digitalio.Direction.OUTPUT  # Setting the LED as output

# Setting up the right side of the motor driver (output signal: 8, 9) (EN: 7)
right1 = digitalio.DigitalInOut(board.D8)
right1.direction = digitalio.Direction.OUTPUT
right2 = digitalio.DigitalInOut(board.D9)
right2.direction = digitalio.Direction.OUTPUT
right_en = digitalio.DigitalInOut(board.D7)
right_en.direction = digitalio.Direction.OUTPUT

# Setting up the left side of the motor driver (output signal: 4, 5) (EN: 6)
left1 = digitalio.DigitalInOut(board.D4)
left1.direction = digitalio.Direction.OUTPUT
left2 = digitalio.DigitalInOut(board.D5)
left2.direction = digitalio.Direction.OUTPUT
left_en = digitalio.DigitalInOut(board.D6)
left_en.direction = digitalio.Direction.OUTPUT

# Setting up the analog IR Sensor pins on left and right
ir_left = analogio.AnalogIn(board.A3)
ir_right = analogio.AnalogIn(board.A10)


def initialize():  # Function to initalize/stop the motors
    left1.value = False  # LOW
    left2.value = False  # LOW
    left_en.value = True  # HIGH
    right1.value = False  # LOW
    right2.value = False  # LOW
    right_en.value = True  # HIGH


def right():  # Function for turning the robot to the right
    left1.value = False  # HIGH
    left2.value = True  # LOW
    right1.value = False  # LOW
    right2.value = True  # HIGH
    print('Turning right')


def left():  # Function for turning the robot to the left
    left1.value = True  # LOW
    left2.value = False  # HIGH
    right1.value = True  # HIGH
    right2.value = False  # LOW
    print('Turning left')


def forward():  # Function for forward movement of the robot
    left1.value = False  # HIGH
    left2.value = True  # LOW
    right1.value = True  # HIGH
    right2.value = False  # LOW
    print('Moving forward')


if __name__ == '__main__':
    initialize()
    time.sleep(0.1)  # Delay of 100 ms
    while True:
        readleft = ir_left.value // 10000  # values now in the range of 0 to 6
        readright = ir_right.value // 10000
        threshold = 3  # <- Adjust this value according to your needs
        # print('Left: ', readleft, end='\t')  # for debugging
        # print('Right: ', readright)
        if readleft < threshold and readright < threshold:  # Both sensors detect infrared (white)
            forward()
        # Left sensor doesn't detect infrared (black)
        elif readleft > threshold and readright < threshold:
            left()
        # Right sensor doesn't detect infrared (black)
        elif readleft < threshold and readright > threshold:
            right()
        else:  # If both the sensors are off (black),  then stop
            initialize()
        led.value = True
        time.sleep(0.25)
        led.value = False
        time.sleep(0.25)

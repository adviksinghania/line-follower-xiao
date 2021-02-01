import board
import digitalio
import time
import analogio

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

right1 = digitalio.DigitalInOut(board.D8)
right1.direction = digitalio.Direction.OUTPUT
right2 = digitalio.DigitalInOut(board.D9)
right2.direction = digitalio.Direction.OUTPUT
right_en = digitalio.DigitalInOut(board.D7)
right_en.direction = digitalio.Direction.OUTPUT

left1 = digitalio.DigitalInOut(board.D4)
left1.direction = digitalio.Direction.OUTPUT
left2 = digitalio.DigitalInOut(board.D5)
left2.direction = digitalio.Direction.OUTPUT
left_en = digitalio.DigitalInOut(board.D6)
left_en.direction = digitalio.Direction.OUTPUT

ir_left = analogio.AnalogIn(board.A3)
ir_right = analogio.AnalogIn(board.A10)

def initialize():
    left1.value = False  # LOW
    left2.value = False  # LOW
    left_en.value = True  # HIGH
    right1.value = False  # LOW
    right2.value = False  # LOW
    right_en.value = True  # HIGH

def right():
    left1.value = False  # HIGH
    left2.value = True  # LOW
    right1.value = False  # LOW
    right2.value = True  # HIGH
    print('Turning right')

def left():
    left1.value = True  # LOW
    left2.value = False  # HIGH
    right1.value = True  # HIGH
    right2.value = False  # LOW
    print('Turning left')

def forward():
    left1.value = False  # HIGH
    left2.value = True  # LOW
    right1.value = True  # HIGH
    right2.value = False  # LOW
    print('Moving forward')

if __name__ == '__main__':
    initialize()
    time.sleep(0.1)
    while True:
        readleft = ir_left.value // 10000  # values now in the range of 0 to 6
        readright = ir_right.value // 10000
        # print('Left: ', readleft, end='\t')  # for debugging
        # print('Right: ', readright)
        if readleft < 3 and readright < 3:
            forward()
        elif readleft > 3 and readright < 3:
            left()
        elif readleft < 3 and readright > 3:
            right()
        else:
            initialize()
        led.value = True
        time.sleep(0.25)
        led.value = False
        time.sleep(0.25)

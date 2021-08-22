#!/usr/bin/python
# Import required libraries
from time import sleep
from pyfirmata import ArduinoMega, util, Pin, OUTPUT
from Control import Device, Stepper

mega = {
    'digital' : tuple(x for x in range(54)),
    'analog' : tuple(x for x in range(16)),
    'pwm' : tuple(x for x in range(2,14)),
    'use_ports' : True,
    'disabled' : (0, 1, 14, 15) # Rx, Tx, Crystal
}


device = Device("/dev/ttyACM0", mega)
board = device.getBoard()

motor_right = Stepper(device, board.digital[26], board.digital[28], board.digital[24], 0.000001, 0.001)
motor_left = Stepper(device, board.digital[36], board.digital[34], board.digital[30], 0.000001, 0.001)
 
DIR = 28   # Direction GPIO Pin
STEP = 26  # Step GPIO Pin
CW = 1     # Clockwise Rotation
CCW = 0    # Counterclockwise Rotation
SPR = 2400   # Steps per Revolution (360 / 7.5)
ENBL = 24  # Enable GPIO Pin

# board.digital[ENBL].write(0)
motor_right.enable()
motor_left.enable()
#motor_left.disable()
#while True:
#   sleep(10)
 
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(DIR, GPIO.OUT)
# GPIO.setup(STEP, GPIO.OUT)
# GPIO.output(DIR, CW)

step_count = SPR
delay = .0001

# print("forward")
# board.digital[DIR].write(CW)
# for x in range(step_count):
#     board.digital[STEP].write(1) # GPIO.output(STEP, GPIO.HIGH)
#     sleep(delay)
#     board.digital[STEP].write(0) # GPIO.output(STEP, GPIO.LOW)
#     sleep(delay)
motor_right.run(1, 4800, 0.5)

sleep(.5)

motor_right.run(0, 4800, 0.5)

sleep(.5)

motor_left.run(1, 4800, 0.5)

sleep(.5)

motor_left.run(0, 4800, 0.5)



# print("backward")
# board.digital[DIR].write(CCW) # GPIO.output(DIR, CCW)
# for x in range(step_count):
#     board.digital[STEP].write(1) # GPIO.output(STEP, GPIO.HIGH)
#     sleep(delay)
#     board.digital[STEP].write(0) # GPIO.output(STEP, GPIO.LOW)
#     sleep(delay)
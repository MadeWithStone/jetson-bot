from time import sleep
from pyfirmata import Board, util

class Device:
  def __init__(self, device, layout):
    self.board = Board("/dev/ttyACM0", layout)

  def getBoard(self):
    return self.board

class Stepper:
  def __init__(self, device, step, direction, enable, min_delay, max_delay):
    self.board = device.getBoard()
    self.stp = step
    self.dir = direction
    self.enbl = enable
    self.min = min_delay
    self.max = max_delay

  def enable(self):
    self.enbl.write(0)

  def disable(self):
    self.enbl.write(1)

  def calc_delay(self, speed):
    diff = self.max - self.min
    delay = self.max - ((speed/1.0)*diff)
    return delay

  def run(self, direction, steps, speed):
    delay = self.calc_delay(speed)
    print("running motor direction: {}".format(direction))
    self.dir.write(direction)
    for x in range(steps):
        self.stp.write(1) # GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        self.stp.write(0) # GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

  def run_cont(self, direction, speed):
    delay = self.calc_delay(speed)
    print("running motor direction: {}".format(direction))
    self.board.digital[self.dir].write(direction)
    while True:
        self.board.digital[self.stp].write(1) # GPIO.output(STEP, GPIO.HIGH)
        sleep(delay)
        self.board.digital[self.stp].write(0) # GPIO.output(STEP, GPIO.LOW)
        sleep(delay)

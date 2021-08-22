from pyfirmata import ArduinoMega, util

led_pin = 7
button_pin = 8

board = ArduinoMega("/dev/ttyACM0")
while True:
  board.digital[13].write(1)
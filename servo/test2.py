import serial
import time
import keyboard  # using module keyboard

port ="/dev/ttyUSB0"

s1 = serial.Serial(port,9600)
s1.flushInput()
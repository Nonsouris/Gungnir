import sys, termios, tty, os, time
import serial
import time

port ="/dev/ttyUSB0"

s1 = serial.Serial(port,9600)
s1.flushInput()


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 
button_delay = 0.2
 
while True:
    char = getch()
 
    if (char == "w"):
        print("w")
 
    if (char == "s"):
        print("s")

    if (char == "a"):
        print("a")
 
    if (char == "d"):
        print("d")

    if (char == "p"):
        break

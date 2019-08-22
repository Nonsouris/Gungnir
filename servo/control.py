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
    time.sleep(.03)
    char = getch()
 
    if (char == "w"):
        s1.write('3\r')
 
    if (char == "s"):
        s1.write('4\r')

    if (char == "a"):
        s1.write('1\r')
 
    if (char == "d"):
        s1.write('2\r')

    if (char == "p"):
        break
    s1.flushInput()

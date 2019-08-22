from receive import receive_messages
from publish import publish_messages
from google.oauth2 import service_account
from time import sleep
from gpiozero import MCP3008
import RPi.GPIO as GPIO
from random import randrange


adc = MCP3008(channel=0)
while True:   
	light_value = adc.value
	publish_messages("gungnir-249212", "data",light_value)
	GPIO.setwarnings(False)
	if light_value > 0.9:
		print("LightOn")
		GPIO.output(18,GPIO.HIGH)
	else:
		GPIO.output(18,GPIO.LOW)
	sleep(9)


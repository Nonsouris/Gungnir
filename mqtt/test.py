from receive import receive_messages
from publish import publish_messages
from google.oauth2 import service_account
from gpiozero import MCP3008
from time import sleep
import RPi.GPIO as GPIO
adc = MCP3008(channel=0)

source_credentials = service_account.Credentials.from_service_account_file('../credentials/credentials_davis.json')

while True:   
	light_value = adc.value
	publish_messages("gungnir-249212", "data",light_value)
	GPIO.setwarnings(False)
	#receive_messages()
	if light_value > 0.9:
		print("LightOn")
		GPIO.output(18,GPIO.HIGH)
	else:
		GPIO.output(18,GPIO.LOW)
	print(light_value)
	sleep(3)


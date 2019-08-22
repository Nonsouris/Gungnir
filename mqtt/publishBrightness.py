from receive import receive_messages
from publish import publish_messages
from google.oauth2 import service_account
from time import sleep
from random import uniform
from google.cloud import pubsub_v1
from gpiozero import MCP3008

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path("gungnir-249212","data")
print(topic_path)

adc = MCP3008(channel=0)

while True:
        sleep(5)			#to be removed
	light_value = uniform(0,1) #rng, to be removed	
        #light_value=adc.value
	print(light_value)


	data = u'{}'.format(light_value)
        # Data must be a bytestring
        print("data :" + data)
	data = data.encode('utf-8')
        # When you publish a message, the client returns a future.
        future = publisher.publish(topic_path, data=data)
        print(future.result())

        print('Published messages.')

#	GPIO.setwarnings(False)
	#receive_messages()
#	if light_value > 0.9:
#		print("LightOn")
#		GPIO.output(18,GPIO.HIGH)
#	else:
#		GPIO.output(18,GPIO.LOW)
#	sleep(9)

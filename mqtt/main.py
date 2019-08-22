import base64
import json
import os
import smtplib
import time, sys
from random import randrange
from pygame import mixer
from google.cloud import pubsub_v1
from google.cloud import storage
from google.cloud import vision
from time import sleep
from datetime import datetime
from picamera import PiCamera
from google.cloud.vision import types
from face_detection import highlight_faces
from PIL import Image, ImageDraw
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

gmail_user = 'pentestnil@gmail.com'
gmail_password = '1qwe$#@!'

credential_path = "../credentials/credentials_davis.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

sent_from = 'pentestnil@gmail.com'
to = ['t0016029b@gmail.com']
From = "pentestnil@gmail.com"
To = "t0016029b@gmail.com"
delay=2
client = vision.ImageAnnotatorClient()

def detect_face(face_file, max_results=4):
    """Uses the Vision API to detect faces in the given file.

    Args:
        face_file: A file-like object containing an image with faces.

    Returns:
        An array of Face objects with information about the picture.
    """
    client = vision.ImageAnnotatorClient()

    content = face_file.read()
    image = types.Image(content=content)

    return client.face_detection(image=image, max_results=max_results).face_annotations
def warning(option):
	mixer.init()
	if option == 1:
		sound = mixer.Sound('target.wav')
	else:
		sound = mixer.Sound('seeyou.wav')
	sound.play()
	time.sleep(sound.get_length()+1) 	

def emailalert():
	try:
		img_data = open(full_path_post, 'rb').read()
		msg = MIMEMultipart()
		msg['Subject'] = 'Alert!!'
		text = MIMEText("Hey, you have a visitor\n\n -Davis ")
		msg.attach(text)
		image = MIMEImage(img_data, name=os.path.basename(full_path_post))
		msg.attach(image)
		server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
		server.ehlo()
		server.login(gmail_user, gmail_password)
		server.sendmail(From,To, msg.as_string())
		server.close()
		print ('Email sent!')
	except:
		print ('Something went wrong...')
	
	
def takePhotoWithPiCam():
	camera.capture(full_path)
	sleep(delay)

def faces(input_filename, output_filename, max_results):
    with open(input_filename, 'rb') as image:
        faces = detect_face(image, max_results)
        print('Found {} face{}'.format(
            len(faces), '' if len(faces) == 1 else 's'))

        print('Writing to file {}'.format(output_filename))
        # Reset the file pointer, so we can read the file again
        image.seek(0)
        highlight_faces(image, faces, output_filename)
	if len(faces) == 1:
		print("hi")
		emailalert()
		warning(randrange(2))
		upload_blob("images1703221",full_path_post,"visitor")

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

# Set the filename and bucket name
bucket = 'images1703221' # replace with your own unique bucket name
with PiCamera() as camera:
	while True:
		full_path = ('/home/pi/Desktop/pre.jpg')
		full_path_post = ('/home/pi/Desktop/post.jpg')
		file_name = (str(datetime.now()) + ' pre.jpg')
		takePhotoWithPiCam()
		faces(full_path,full_path_post,4)
		upload_blob("images1703221",full_path,"current")

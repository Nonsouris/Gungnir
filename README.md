Python Gungnir
==================================

## Code style
Standard Python code

[![js-standard-style](https://img.shields.io/badge/code%20style-standard-brightgreen.svg?style=flat)](https://github.com/feross/standard)
# Overview of project

Our project, takes images using the camera every predefined seconds, feeds it into a cloud bucket and performs image recognition on it. It has been preconfigured to identify faces and highlight them. Currently it is performing the function of security camera, thus when it recognises a person, it will email the owner and issue a verbal warning to the visitor.It has been attached to servos to allow movement of the camera however this application is infinitely dynamic, allowing it to be used for a variety of other purposes such as as being able to be configured for Optical character recognition and other artificial intelligence purposes.


Quick Start
-----------

In order to run this project, you first need to go through the following steps:

1. `Select or create a Cloud Platform project.`
2. `Enable billing for your project.`
3. `Set up the RPI as per the image shown below`
3. `Git clone the repository.`
4. `Cd into IOT/IOTv2-Electric-Boogaloo/mqtt.`
5. `Run the authentication`
6. `Run the main.py file`
7. `Run the dataup.py`

##Supported Python Versions

Python >= 2.7

#Deprecated Python Versions

Python == 2.7. Python 2.7 support will be removed on January 1, 2020.

## Installation

To implement the google cloud functions, the libraries need to be installed on the Raspberry Pi. 
Install Google Cloud Storage (https://pypi.org/project/google-cloud-storage/)

```bash
sudo pip install google-cloud-storage
```
Install Google Cloud Vision (https://pypi.org/project/google-cloud-vision/)
```bash
sudo  install google-cloud-vision
```

Install Pillow (https://pypi.org/project/Pillow/2.2.1)
```bash
sudo  pip install Pillow
```
To implement MySQL database, the MySQL libraries need to be installed. If you are using the ST0324 IoT Raspbian image, you might encounter an error as the libraries have already been pre-installed. If you are using a fresh image, you would need to run the commands below to install the MySQL libraries.

```bash
sudo pip install mysql-connector-python
sudo pip install mysql-connector
```
Finally, install the pubsub libararies needed to send mqtt data

```bash
sudo pip install google-cloud-pubsub
```

## Authentication

If you want to run all programs, you will need a billing-enabled GCP project, and a service account with access to the APIs. Running the command below allows for your computer to be authenticated and allowed to run and use the files.
```bash
export PROJECT_ID=<project-id> GOOGLE_APPLICATION_CREDENTIALS=</path/to/creds.json>
```
## Hardware
- 1x Raspberry pi
- 1x Raspberry pi camera
- 1x Breadboard
- 2x SG90 servo
- 2x AA battery packs
- 1x Light-Dependant Resistor
- 1x Light-emitting diode
- 1x Speaker
- 1x AUX Cable
- 1x Portable Charger

## Final RPI Setup
![Image of Setup](https://github.com/evanderleng/IOTv2-Electric-Boogaloo/blob/master/Images/1.png)

# Fritzing of LDR

Add the LDR to the breadboard as shown

1. One end of the LDR should be connected to Pin 1 of the MCP3008 ADC and the 10k ohms resistor
2. The other end of the LDR should be connected to GND

![Image of Fritzing1](https://github.com/evanderleng/IOTv2-Electric-Boogaloo/blob/master/Images/2.png)

# Fritzing of Servos

Follow the wiring display down below to properly connect the servos to the arduino

![Image of Fritzing2](https://github.com/evanderleng/IOTv2-Electric-Boogaloo/blob/master/Images/3.png)


## Billing
To re-enable billing on a project:

1. Go to the Google Cloud Platform Console.
1. From the projects list drop-down at the top of the page, select the project to re-enable billing for.
1. Open the console navigation menu (menu) and select Billing.
1. Click Link a billing account.
1. Select a billing account, then click SET ACCOUNT.

## Storage
In your terminal window, create a Cloud Storage bucket, where [YOUR_BUCKET_NAME] represents the name of your bucket:
```bash
gsutil mb gs://[YOUR_BUCKET_NAME]
```

## Architecture

The System architecture of the image recognition.

![Image of Imagerecog](https://github.com/evanderleng/IOTv2-Electric-Boogaloo/blob/master/Images/4.png)

The System architecture of the pubsub mqtt data and the app engine.
![Image of AppEngine](https://github.com/evanderleng/IOTv2-Electric-Boogaloo/blob/master/Images/7.png)

## Web View
The following images are screenshots of how the web application should look if setup was done correctly. All the screenshots are of index.html.
![Image of WebView](https://github.com/evanderleng/IOTv2-Electric-Boogaloo/blob/master/Images/5.png)

## Expected outcome
To test if the program works, run main.py as well as dataup.py. If everything is configured correctly and everything is set up properly. It should work

## Authors

* **Davis Zheng** - [Nonsour](https://github.com/nonsour)/[Nonsouris](https://github.com/nonsouris)

* **Evander Leng** - [EvanderLeng](https://github.com/evanderleng/)

## Acknowledgments

* Thanks to Ms Dora Chua for her guidance


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

from flask import Flask, render_template, jsonify, request,Response

#from google.cloud import pubsub_v1
import mysql.connector
import sys

import json
import numpy
import datetime
import decimal
import os
import gevent
import gevent.monkey
from gevent.pywsgi import WSGIServer
#from gpiozero import LED

CLOUDSQL_CONNECTION_NAME = 'gungnir-249212:us-central1:iotsql'
CLOUDSQL_USER = 'root'
CLOUDSQL_PASSWORD = '1qwer$#@!'
cloudsql_unix_socket = os.path.join('/cloudsql', str(CLOUDSQL_CONNECTION_NAME))
db = 'testdatabase'
cnx = mysql.connector.connect(user=CLOUDSQL_USER, password=CLOUDSQL_PASSWORD, unix_socket=cloudsql_unix_socket, database=db)
print('Connected to Google Cloud SQL (Unix Socket)')

gevent.monkey.patch_all()


class GenericEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.generic):
            return numpy.asscalar(obj) 
        elif isinstance(obj, datetime.datetime):  
            return obj.strftime('%Y-%m-%d %H:%M:%S') 
        elif isinstance(obj, decimal.Decimal):
            return float(obj)
        else:  
            return json.JSONEncoder.default(self, obj) 


'''led = LED(18)

def ledOn():
  led.on()
  return "On"

def ledOff():
  led.off()
  return "Off"

def ledStatus():
  if led.is_lit:
     return 'On'
  else:
    return 'Off'
'''

def data_to_json(data):
    json_data = json.dumps(data,cls=GenericEncoder)
    return json_data


def fetch_fromdb_as_json(cnx,cursor,sql):
    try:
        cursor.execute(sql)
        row_headers=[x[0] for x in cursor.description] 
        results = cursor.fetchall()
        data = []
        for result in results:
            data.append(dict(zip(row_headers,result)))
        
        data_reversed = data[::-1]

        data = {'data':data_reversed}

        return data_to_json(data)

    except:
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])
        return None


app = Flask(__name__)

@app.route("/api/getdata",methods = ['POST', 'GET'])
def apidata_getdata():
    global conn
    if request.method == 'POST':
        try:
            sql="SELECT * FROM light ORDER BY datetime_value DESC LIMIT 10"
            cur = cnx.cursor()
            json_data = fetch_fromdb_as_json(cnx,cur,sql)
            loaded_r = json.loads(json_data)
            data = {'chart_data': loaded_r, 'title': "IOT Data"}
            return jsonify(data)
        except:
            print(sys.exc_info()[0])
            print(sys.exc_info()[1])

'''
@app.route("/moveL")
def moveL():
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path("gungnir-249212", "move")
    print(topic_path)
    data = u'left'
    data = data.encode('utf-8')
    future = publisher.publish(topic_path, data=data)
    print(future.result())
    print('Published messages.')

@app.route("/moveR")
def moveR():
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path("gungnir-249212", "move")
    print(topic_path)
    data = u'right'
    data = data.encode('utf-8')
    future = publisher.publish(topic_path, data=data)
    print(future.result())
    print('Published messages.')

@app.route("/moveU")
def moveU():
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path("gungnir-249212", "move")
    print(topic_path)
    data = u'up'
    data = data.encode('utf-8')
    future = publisher.publish(topic_path, data=data)
    print(future.result())
    print('Published messages.')


@app.route("/moveD")
def moveD():
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path("gungnir-249212", "move")
    print(topic_path)
    data = u'down'
    data = data.encode('utf-8')
    future = publisher.publish(topic_path, data=data)
    print(future.result())
    print('Published messages.')
'''
@app.route("/")
def chartsimple():
    return render_template('index.html')


if __name__ == '__main__':
   try:
        app.run(host='127.0.0.1', port=8080, debug=True)
   except:
        print("Exception")
        import sys
        print(sys.exc_info()[0])
        print(sys.exc_info()[1])

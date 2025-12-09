import socketio
import time

# standard Python
sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def disconnect():
    print('disconnected from server')

try:
    sio.connect('http://localhost:8080')
    print('Connected with sid:', sio.sid)
    time.sleep(5)
    sio.disconnect()
except socketio.exceptions.ConnectionError as e:
    print("Connection error:", e)


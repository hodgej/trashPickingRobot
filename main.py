import serial
import objectID
import time

arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

def main():
    while True:
        objectID.run()
        rotation = 60

        arduino.write(bytes("h", 'utf-8'))

        
        time.sleep(.05)
        print(arduino.readline())

        

    objectID.destroy()
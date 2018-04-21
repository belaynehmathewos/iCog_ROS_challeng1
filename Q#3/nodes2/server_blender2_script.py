import bge
import socket
#import sys

bge.logic.mouse.visible = True

def locationReader():
    #Remember: I want to move my objects(both turtles and blender obj) 
    #in linear only x-direction and in angular only z-direction
    global x_cord,y_cord,teta,msg
    x_cord = obj.getLinearVelocity(True).x / 240 # linear
    teta = obj.getAngularVelocity(True).z / 10 # rotation
    msg = str(x_cord) + ' ' + str(teta)
    print(msg)

def myBlender():
    #Global variables
    global x_cord,y_cord,teta,sock,obj,msg
    x_cord = 5.5
    y_cord=5.5
    teta=0
    msg = '1 0'
    obj = bge.logic.getCurrentController().owner

    # create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = socket.gethostname()

    port = 12345

    # connection to hostname on the port.
    sock.connect((host, port))
    print("In Blender connected")
    # Receive no more than 1024 bytes
    msg2 = sock.recv(1024).decode('ascii')
    print(str(msg2))


if __name__ == "__main__":
    myBlender()
    locationReader()
    sock.send(msg.encode('ascii'))

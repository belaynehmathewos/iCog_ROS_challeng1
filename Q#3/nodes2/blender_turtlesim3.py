#!/usr/bin/env python
import rospy
from turtlesim.srv import SetPen
from turtlesim.srv import TeleportAbsolute
from turtlesim.srv import TeleportRelative
from std_srvs.srv import Empty as EmptyServiceCall
import socket
import shlex

def client_ros():
    #Global variables
    global serversock,pen_setting_turtle1, absolute_teleport_turtle1, relative_teleport_turtle1, background_clear
    # create a socket object
    serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # get local machine name
    host = socket.gethostname()

    port = 12345

    # bind to the port
    serversock.bind((host, port))

    # queue up to 10 requests
    serversock.listen(10)


    #ros turtle controller initialization
    rospy.wait_for_service('turtle1/set_pen')
    rospy.wait_for_service('clear')
    pen_setting_turtle1 = rospy.ServiceProxy('turtle1/set_pen', SetPen)
    absolute_teleport_turtle1 = rospy.ServiceProxy('turtle1/teleport_absolute', TeleportAbsolute)
    relative_teleport_turtle1 = rospy.ServiceProxy('turtle1/teleport_relative', TeleportRelative)
    background_clear = rospy.ServiceProxy('clear', EmptyServiceCall)
    pen_setting_turtle1(200,100,50,2,0)
    absolute_teleport_turtle1(5.5,5.5,0)
    background_clear()


if __name__ == "__main__":
    try:
        client_ros()
        while not rospy.is_shutdown():
            # establish a connection
            clientsock,addr = serversock.accept()
            clientsock.send('Connected'.encode('ascii'))
            # Receive no more than 1024 bytes
            msg = clientsock.recv(1024).decode('ascii') #receive a message from blender
            #Convert the received message to str
            pose_input = str(msg)
            #parse and partionion message
            str_vector = shlex.split(pose_input)
            x_cord = str_vector[0]
            #x= x*5 #To magnify its(turtle) motion
            teta = str_vector[1]
            #move turtle using relative motion
            #relative_teleport_turtle1(5*(float(x_cord)),float(teta))
            relative_teleport_turtle1(float(x_cord),float(teta))
            print ('Object location is at {}'.format(str_vector))
        clientsock.close()

    except rospy.ROSInterruptException:
        clientsock.close()
        pass
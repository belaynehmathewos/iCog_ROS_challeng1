#! /usr/bin/env python2
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

def callback(data):
    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(data, "bgr8")
    # Converts to grayscale ima type
    gray_picture = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY) 
    cv2.imshow("Converted2", gray_picture)
    
    keyctr = cv2.waitKey(1)
    
rospy.init_node("image_subscriber2")  # initiate a node named 'image_publisher'

# create a publisher object that will publish on a 'image_publisher' topic
sub = rospy.Subscriber('image_publisher2', Image, callback)

rospy.spin()
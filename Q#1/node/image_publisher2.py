#!/usr/bin/env python2
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

def imagePublisher():
    cap = cv2.VideoCapture(0)
    #publish on topic image_publisher
    pub = rospy.Publisher('image_publisher2', Image)
    rospy.init_node('image_publisher2', anonymous=True)
    rate = rospy.Rate(2) # 10hz
    
    frame=""
    while True:
        check, frame = cap.read()
        bridge = CvBridge()
        #publish it into ros/ bgr8 type
        pub.publish(bridge.cv2_to_imgmsg(frame, "bgr8"))
        cv2.imshow("Captured2", frame)
        
        # rospy.loginfo(frame)
        key = cv2.waitKey(1)
        if (key == ord('q')):
            break
        rate.sleep()
    #Release All Images and Windows
    cvReleaseImage(frame)
    cvDestroyWindow("Captured")

if __name__ == '__main__':
    try:
        imagePublisher()
    except rospy.ROSInterruptException:
        pass
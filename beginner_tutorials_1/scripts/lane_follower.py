#!/usr/bin/env python3
 
import rospy
import cv2
import numpy as np
import os, rospkg
import json

from sensor_msgs.msg import CompressedImage
from cv_bridge import CvBridgeError
from std_msgs.msg import Float64

from utils import purePursuit


if __name__ == '__main__':
    
    rp = rospkg.RosPack()
    
    currentPath = rp.get_path("beginner_tutorials")
    
    with open(os.path.join(currentPath, 'sensor/sensor_params.json'), 'r') as fp:
        sensor_params = json.load(fp)

    rospy.init_node('lane_follower', anonymous=True)

    ctrller = purePursuit(lfd=4.0)
    #5.3
    rate = rospy.Rate(20)

    while not rospy.is_shutdown():
        #print("nocal")
        if ctrller.lpath is not None:

            #ctrller.calc_acc(30/3.6)
            print("cal & pub")
            ctrller.steering_angle()
            
            ctrller.pub_cmd()

            rate.sleep()

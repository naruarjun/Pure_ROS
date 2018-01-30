#!/usr/bin/env python  
import rospy
import math
import numpy as np
import tf2_ros
import geometry_msgs.msg
if __name__ == '__main__':
    rospy.init_node('dynamic_broadcast')
    #Creating Transform Broadcaster
    broadcaster=tf2_ros.TransformBroadcaster()
    tfBuffer = tf2_ros.Buffer()
    #Creaing Transform Listener
    listener = tf2_ros.TransformListener(tfBuffer)
    #Object to be broadcast over /tf topic (Transform from center to target)
    t = geometry_msgs.msg.TransformStamped()
    rate = rospy.Rate(10.0)
    theta=0.0
    #Inputting parameters from launch file
    radius=rospy.get_param('~radius')
    while not rospy.is_shutdown():
        try:
            #Looking up latest available transform from center to origin
            trans = tfBuffer.lookup_transform("center","origin", rospy.Time(0))
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rate.sleep()
            continue
        t.header.frame_id = "center"
        t.header.stamp = rospy.Time.now()
        t.child_frame_id = "target"
        #t.transform.translation.x = radius*math.cos(theta)
        #t.transform.translation.y = radius*math.sin(theta)
	#Setting coordinates for target with respect to center
	t.transform.translation.x = radius*np.cos(theta)
	t.transform.translation.y = radius*np.sin(theta)
	#Incrementing theta for next iteration
        theta=theta+0.1
        t.transform.translation.z = 0.0
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0
	#Broadcasting transform over /tf topic
        broadcaster.sendTransform(t)
        rate.sleep()

#!/usr/bin/env python
import rospy
import geometry_msgs.msg
import sys
import tf
import tf2_ros  
import tf2_msgs.msg

#Class to broadcast static frame for offset
class FixedTFBroadcaster:

    def __init__(self):
	#Publisher for /tf topic
        self.pub_tf = rospy.Publisher("/tf", tf2_msgs.msg.TFMessage, queue_size=1000)
        rate=rospy.Rate(10)
	#Inputting parameters from launch file (demo.launch)
	x_offset = rospy.get_param('~x_offset')
	y_offset = rospy.get_param('~y_offset')
        while not rospy.is_shutdown():
	    #Object to be broadcast over /tf topic (Transform from origin to center) 
            t = geometry_msgs.msg.TransformStamped()
            t.header.frame_id = "origin"
            t.header.stamp = rospy.Time.now()
            t.child_frame_id = "center"
            t.transform.translation.x = x_offset
            t.transform.translation.y = y_offset
            t.transform.translation.z = 0.0
            t.transform.rotation.x = 0.0
            t.transform.rotation.y = 0.0
            t.transform.rotation.z = 0.0
            t.transform.rotation.w = 1.0
            tfm = tf2_msgs.msg.TFMessage([t])
            self.pub_tf.publish(tfm)
            rate.sleep()
if __name__ == '__main__':
    rospy.init_node('static_broadcast')
    tfb = FixedTFBroadcaster()
    rospy.spin()

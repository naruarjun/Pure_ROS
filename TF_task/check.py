#!/usr/bin/env python
import rospy
import tf
import tf2_ros
import math

#Checking the various transforms and printing their output
if __name__=='__main__':
	rospy.init_node('check')
	tfBuffer = tf2_ros.Buffer()
    	listener = tf2_ros.TransformListener(tfBuffer)
	rate=rospy.Rate(10)
	i=1
	while not rospy.is_shutdown():
		try:
			trans1 = tfBuffer.lookup_transform('target', 'center', rospy.Time.now(),rospy.Duration(5.0))
			trans2 = tfBuffer.lookup_transform('center', 'origin', rospy.Time.now(),rospy.Duration(5.0))
			trans3 = tfBuffer.lookup_transform('target', 'origin', rospy.Time.now(),rospy.Duration(5.0))
       		except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
        		continue
		rospy.loginfo('Iteration: %f'%(i))
		rospy.loginfo('Radius: %f'%(math.sqrt(trans1.transform.translation.x**2+trans1.transform.translation.y**2)))
		rospy.loginfo('Target to Center: [x:%f,y:%f]'%(trans1.transform.translation.x,trans1.transform.translation.y))
		rospy.loginfo('Center to Origin: [x:%f,y:%f]'%(trans2.transform.translation.x,trans2.transform.translation.y))
		rospy.loginfo('Target to Origin: [x:%f,y:%f]'%(trans3.transform.translation.x,trans3.transform.translation.y))	
		rospy.loginfo(' ')
		i=i+1		
		rate.sleep()

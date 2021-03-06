import sys,serial
import threading
import __future__
from serial.tools import list_ports
import math
import time
import tf
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3

if sys.version_info.major < 3:
    import thread as _thread
else:
    import _thread

def callback(message):
	v = message.linear.x
	w = message.angular.z
	WHEEL_DIST = 0.327
    # this should be a REQUIRED parameter - confirm if this is the right value for Musafir v2
	speed_wish_right = (w*WHEEL_DIST)/2.0 + v
	speed_wish_left = v*2.0-speed_wish_right
	vl = speed_wish_left
	vr = speed_wish_right
	commandOut ="D," + str(vl) + "," + str(vr) + "\n"
	VelocityV3.publish(commandOut)
	print(commandOut)

if __name__ == '__main__':
    try:
        VelocityV3 = rospy.Publisher("msgForMotorControllerV3", String, queue_size=2)
        rospy.Subscriber("/cmd_vel", Twist, callback)
        # subscribed topic should be a parameter
        rospy.init_node('Velocity')
        rospy.spin()
        # spin is the ROS while LOOP
        
    except KeyboardInterrupt:
        print "Key-interrupt"
        sys.exit(0)
        
    sys.exit(0)
#!/usr/bin/env python3 

import rospy
from std_msgs.msg import String

def callback(self):
    rospy.loginfo(self)

def listener():
    rospy.init_node('hello_world_listener', anonymous=True)
    rospy.Subscriber('chatter', String, callback)
    # rospy.spin()
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        rate.sleep()



if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass


#! /usr/bin/env python3

from std_msgs.msg import String
import rospy

def callback_channel_1(message):
   rospy.loginfo(message.data)
   

def comm():
    rospy.init_node('comm_2',anonymous=True)
    rospy.loginfo('node comm_2 has been initialized')
    pub = rospy.Publisher('channel_2', String, queue_size=10)
    rospy.Subscriber('channel_1',String,callback_channel_1)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
         str_data = input()
         data = f"{rospy.get_time():.4f} | {str_data}"
         pub.publish(data)
         rate.sleep()


if __name__ == '__main__':
    try: 
       comm()
    except rospy.ROSInternalException:
      pass        
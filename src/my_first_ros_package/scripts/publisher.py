#!/usr/bin/env python3 
import rospy as rs 
from std_msgs.msg import String as st 

# def talker():
    # pub = rs.Publisher('chatter', st, queue_size=10)
    # rs.init_node('talker', anonymous=True)
    # rate = rs.Rate(10) # 10hz
    
    # while not rs.is_shutdown():
    #     hello_str = "hello world %s" % rs.get_time()
    #     rs.loginfo(hello_str)
    #     pub.publish(hello_str)
    #     rate.sleep()
   
if __name__ == '__main__':
    try:
        # talker()
        pub = rs.Publisher('chatter', st, queue_size=10)
        rs.init_node('talker', anonymous=True)
        rate = rs.Rate(10) # 10hz
            
        while not rs.is_shutdown():
            hello_str = "hello world %s" % rs.get_time()
            rs.loginfo(hello_str)
            pub.publish(hello_str)
            rate.sleep()
    except rs.ROSInterruptException:
        pass
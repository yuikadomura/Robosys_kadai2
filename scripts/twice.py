//BSD 3-Clause Licence
//Copyright (c) 2021 Ryuichi Ueda + Yui Kadomura. All rights reserved.

#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64
import time

n = 0.0

def cb(message):
    global n
    n = message.data

if __name__ == '__main__':
    rospy.init_node('twice')
    sub = rospy.Subscriber('count_up', Int64, cb)
    pub = rospy.Publisher('twice', Int64, queue_size=1) 
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        date_time = datetime.datetime.fromtimestamp(n)
        pub.publish(n)
        rate.sleep()

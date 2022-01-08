//BSD 3-Clause License
//Copyright (c) 2021 Ryuichi Ueda. All rights reserved

#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64

rospy.init_node('count')
pub = rospy.Publisher('count_up', Int64, queue_size=1)
rate = rospy.Rate(10)
n = 0

while not rospy.is_shutdown():
    n = int(datetime.datetime.now())
    pub.publish(n)
    rate.sleep()

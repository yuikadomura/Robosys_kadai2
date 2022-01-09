//BSD 3-Clause License
//Copyright (c) 2021 Ryuichi Ueda + Yui Kadomura. All rights reserved

#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
import time

rospy.init_node('getUnix')
pub = rospy.Publisher('get_Unix', Float64, queue_size=1)
rate = rospy.Rate(10)
n = 0.0

while not rospy.is_shutdown():
    n = time.time()
    print(type(time.time()),':',t)
    pub.publish(t)
    rate.sleep()

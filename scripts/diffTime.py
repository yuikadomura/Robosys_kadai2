//BSD 3-Clause Licence
//Copyright (c) 2021 Ryuichi Ueda + Yui Kadomura. All rights reserved.

#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64, String
from datetime import datetime, timedelta, timezone

t = 0.0
JST = timezone(timedelta(hours =+ 9),'JST')
pre_tm = 0.0
def_time = 0.0

def cb(message):
    global t
    t = message.data

if __name__ == '__main__':
    rospy.init_node('diffTime')
    sub = rospy.Subscriber('get_Unix', Float64, cb)
    pub = rospy.Publisher('diffTime', String, queue_size=1) 
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        date_time = datetime.fromtimestamp(t, JST)
        def_tm = t - pre_tm
        pre_tm = t
        def_str = '{:0.5f}'.format(def_tm)
        dt_str = date_time.strftime("%Y/%m/%d/ %H:%M:%S.%f")
        res_str = '[UNIX Time:' + str(t) + '] [Date Time:' + str(dt_str) + '] [Diff Time:' + str(def_str) + ']'
        print(res_str)
        pub.publish(res_str)
        rate.sleep()

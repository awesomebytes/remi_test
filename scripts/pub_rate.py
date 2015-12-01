#!/usr/bin/env python

import rospy
from std_msgs.msg import Header
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        rate = float(sys.argv[1])
    else:
        rate = 10
    rospy.init_node('asfasdfa')
    r = rospy.Rate(rate)
    pub = rospy.Publisher('/test', Header, queue_size=1)
    seq = 0
    while not rospy.is_shutdown():
        h = Header()
        h.seq = seq
        seq += 1
        h.stamp = rospy.Time.now()
        pub.publish(h)
        r.sleep()

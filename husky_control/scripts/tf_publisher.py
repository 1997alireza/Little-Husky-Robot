#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry


import tf

def broadcastTf(msg, robotname):
    br = tf.TransformBroadcaster()
    ori = (msg.pose.pose.orientation.x,
             msg.pose.pose.orientation.y,
             msg.pose.pose.orientation.z,
             msg.pose.pose.orientation.w)
    br.sendTransform((msg.pose.pose.position.x, msg.pose.pose.position.y, 0), ori,
                    rospy.Time.now(),
                    robotname + "/base_link",
                    robotname + "/odom")

if __name__ == '__main__':
    rospy.init_node('tf_pub')

    robotname = rospy.get_param('~robotname')

    rospy.Subscriber('/%s/odom' % robotname,
                    Odometry,
                    broadcastTf,
                    robotname)

    rospy.spin()

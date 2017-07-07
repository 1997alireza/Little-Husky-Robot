#! /usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from gazebo_msgs.srv import GetModelState, GetModelStateRequest
from std_msgs.msg import Header

rospy.init_node('odom_pub')

robotname = rospy.get_param('~robotname')

odom_pub = rospy.Publisher('/'+robotname+'/odom', Odometry, queue_size=10)

rospy.wait_for_service ('/gazebo/get_model_state')
get_model_srv = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)

odom = Odometry()
header = Header()
header.frame_id = '/'+robotname+'/odom'

model = GetModelStateRequest()
model.model_name = robotname

r = rospy.Rate(100)

while not rospy.is_shutdown():

    result = get_model_srv(model)

    odom.pose.pose = result.pose
    odom.twist.twist = result.twist

    header.stamp = rospy.Time.now()
    odom.header = header

    odom_pub.publish (odom)

    r.sleep()

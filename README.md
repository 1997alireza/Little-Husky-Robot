Little Husky
============
A mini version of husky model
============
This husky is small sized of original one.
I have changed all of it's dimensions like d to (0.5 * d) and changed meshes to change it's look to small size too.

To ride my boy you should install twist teleop:
sudo apt-get install ros-kinetic-teleop- twist-keyboard

And launch:
roslaunch husky_gazebo husky_empty_world.launch

Then run teleop:
rosrun teleop_twist_keyboard teleop_twist_keyboard.py

## husky


Common ROS packages for the Clearpath Husky, useable for both simulation and
real robot operation.

 - husky_control : Control configuration
 - husky_description : Robot description (URDF)
 - husky_msgs : Message definitions
 - husky_navigation : Navigation configurations and demos

For Husky instructions and tutorials, please see [Robots/Husky](http://wiki.ros.org/Robots/Husky).

To create a custom Husky description or simulation, please fork [husky_customization](https://github.com/husky/husky_customization).

## husky_desktop

Desktop ROS packages for the Clearpath Husky, which may pull in graphical dependencies.

 - husky_viz : Visualization (rviz) configuration and bringup

For Husky instructions and tutorials, please see http://wiki.ros.org/Robots/Husky

## husky_robot

Robot ROS packages for the Clearpath Husky, for operating robot hardware.

 - husky_bringup : Bringup launch files and scripts.
 - husky_base : Hardware driver for communicating with the onboard MCU.

For Husky instructions and tutorials, please see http://wiki.ros.org/Robots/Husky

## husky_simualtor

Simulator ROS packages for the Clearpath Husky.

 - husky_gazebo : Gazebo plugin definitions and extensions to the robot URDF.

For Husky instructions and tutorials, please see http://wiki.ros.org/Robots/Husky

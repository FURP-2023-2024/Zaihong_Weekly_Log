# Moving a Robot
#3-resources/ROS #1-projects/FURP 

1. create a pkg `vel_pkg`
2. create a node in the pkg `vel_node`
3. use `NodeHandle` to create a publisher object `vel_pub` publish a [Topic](Topic.md) `/cmd_vel`
4. create a [Message](Message.md) with type `geometry_msgs/Twist` called `vel_msg` (see [geometry_msgs](geometry_msgs.md))
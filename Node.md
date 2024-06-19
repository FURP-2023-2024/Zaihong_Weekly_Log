# Node
#3-resources/ROS #1-projects/FURP 

## 1. Steps to creating a node

1. use `catkin_create_pkg node_name rospy roscpp std_msgs` to create a package
2. create a node file under src of the package dir
3. `#include <ros/ros.h>`
4. `while(ros::ok())`

in CMakeLists:
uncomment `add_executable` and `target_link_libraries` as needed
# Node
#3-resources/ROS #1-projects/FURP 

## 1. Definition 
a standalone process in a robot system

[ROS Master](ROS%20Master.md)

## 2. Steps to creating a node
1. use `catkin_create_pkg node_name rospy roscpp std_msgs` to create a [Package](Package.md)
> rospy if python, roscpp if cpp
2. then to make roscore have access to the package,
```bash
cd ..
catkin make
```


[Creating a Node in cpp](Creating%20a%20Node%20in%20cpp.md)
[Creating a Node in python](Creating%20a%20Node%20in%20python.md)

## 3. Launching several nodes

[roslaunch file](roslaunch%20file.md)
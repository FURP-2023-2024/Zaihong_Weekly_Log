# Node
#3-resources/ROS #1-projects/FURP 

## 1. Definition 
a standalone process in a robot system

[ROS Master](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/ROS%20Master.md)

## 2. Steps to creating a node
1. use `catkin_create_pkg node_name rospy roscpp std_msgs` to create a [Package](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Package.md)
> rospy if python, roscpp if cpp
2. then to make roscore have access to the package,
```bash
cd ..
catkin make
```


[Creating a Node in cpp](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Creating%20a%20Node%20in%20cpp.md)
[Creating a Node in Python](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Creating%20a%20Node%20in%20Python.md)

## 3. Launching several nodes

[roslaunch file](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/roslaunch%20file.md)
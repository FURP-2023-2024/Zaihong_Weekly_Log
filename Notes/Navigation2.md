# Navigation2
#3-resources/ROS2 #1-projects/FURP 

successor of ros1 navigation [Navigation1](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Navigation1.md)

## 1. Installation
```bash
sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup ros-humble-turtlebot3*
```

## 2. Overview
![Pasted image 20240708185305.png](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Pasted%20image%2020240708185305.png.md)

- **Inputs:**
	- [Behavior Tree](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Behavior%20Tree.md)
	- [nav2_behavior_tree](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/nav2_behavior_tree.md)
	- [Transform](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Transform.md)
	- [map](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/map.md)
	- sensor data
- **Outputs:** 
	- velocity smoother
- **Servers:**
	- ==BT Navigator Server==
	- Controller Server
		- [local_costmap](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/local_costmap.md)
	- Planner Server
		- [global_costmap](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/global_costmap.md)
	- Behavior Server
		- Recovery actions
	- Smoother Server
		- Improve path
- Lifecycle Manager

## 3. Differences with [Navigation1](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Navigation1.md)

- [Navigation1](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Navigation1.md):
	- Unconfigurable state machine
	- Single process navigation
	- Single global and local planner allowed at a time
- [Navigation2](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Navigation2.md):
	- Behavior tree based navigation
	- independent modular servers
	- multiple trajectory and path planners allowed


## 4. Basic Usage


## 5. Errors
### 5.1. Unable to spawn 
```
[ERROR] [spawn_entity.py-4]: process has died [pid 48744, exit code 1, cmd '/opt/ros/humble/lib/gazebo_ros/spawn_entity.py -entity waffle_pi -file /home/zorx/Desktop/tb3_ws/install/turtlebot3_gazebo/share/turtlebot3_gazebo/models/turtlebot3_waffle_pi/model.sdf -x 0.0 -y 0.0 -z 0.01 --ros-args'].
```

**Solution:**
need to install all gazebo packages:
```bash
sudo apt install ros-humble-gazebo-*
```



### 5.2. Unable to open gazebo

```
[gzclient-2] gzclient: /usr/include/boost/smart_ptr/shared_ptr.hpp:728: typename boost::detail::sp_member_access<T>::type boost::shared_ptr<T>::operator->() const [with T = gazebo::rendering::Camera; typename boost::detail::sp_member_access<T>::type = gazebo::rendering::Camera*]: Assertion `px != 0' failed. [ERROR] [gzclient-2]: process has died [pid 22131, exit code -6, cmd 'gzclient'].
```

**Solution:**
source gazebo setup file:
```
source /usr/share/gazebo/setup.sh
```

Put in bashrc

### 5.3. Unable to use 

**Solution:**
```yaml
robot_model_type: "nav2_amcl::DifferentialMotionModel"
```


```error
[ERROR] [1720614215.961820111] [rcl]: Error getting RMW implementation identifier / RMW implementation not installed (expected identifier of 'rmw_cyclonedds_cpp'), with error message 'failed to load shared library 'librmw_cyclonedds_cpp.so' due to dlopen error: librmw_cyclonedds_cpp.so: cannot open shared object file: No such file or directory, at ./src/shared_library.c:99, at ./src/functions.cpp:65', exiting with 1., at ./src/rcl/rmw_implementation_identifier_check.c:139[ERROR] [1720614215.961820111] [rcl]: Error getting RMW implementation identifier / RMW implementation not installed (expected identifier of 'rmw_cyclonedds_cpp'), with error message 'failed to load shared library 'librmw_cyclonedds_cpp.so' due to dlopen error: librmw_cyclonedds_cpp.so: cannot open shared object file: No such file or directory, at ./src/shared_library.c:99, at ./src/functions.cpp:65', exiting with 1., at ./src/rcl/rmw_implementation_identifier_check.c:139
```

**Solution:**
uninstall cyclonedds and reboot

## 6. 
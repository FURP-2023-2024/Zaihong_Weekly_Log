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
	
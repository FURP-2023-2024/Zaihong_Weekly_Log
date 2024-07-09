---
number headings: off, first-level 1, max 6, _.1.1.
---
# Project Log
#1-projects/FURP 

Issues faced and configuration options will be uploaded to this repository as reference.

Some links may be broken, as these notes are only part of the full obsidian vault.

Files are not stored in seperate folders as that would make transfer of notes more complicated, and using links is more flexible and straight-forward.

## Week 0
Basic information about [ROS](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/ROS.md)

Tried docker with [ROS](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/ROS.md) but failed [Dockerfile for ROS](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Dockerfile%20for%20ROS.md)

- virtual box installation log 
	- [Shared Folders in VirtualBox Ubuntu](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Shared%20Folders%20in%20VirtualBox%20Ubuntu.md)
	- [Terminal Not Opening in Virtualbox Ubuntu](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Terminal%20Not%20Opening%20in%20Virtualbox%20Ubuntu.md)
	- [Guest Additions Installation](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Guest%20Additions%20Installation.md)

[ROS](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/ROS.md) installation errors:
- [rosdep init failure](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/rosdep%20init%20failure.md)
- gpg key error

## Week 1
- **Learnt:**
	- [Moving a Robot](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Moving%20a%20Robot.md): how to move a robot in gazebo sim
	- [sensor_msgs](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/sensor_msgs.md): how to intepret and send sensor data
	- how to create a [Node](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Node.md)
		- [Creating a Node in Python](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Creating%20a%20Node%20in%20Python.md)
		- [Creating a Node in cpp](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Creating%20a%20Node%20in%20cpp.md)
	- how to create a [Topic](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Topic.md) and utilize it
		- [Publishing a ROS Topic](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Publishing%20a%20ROS%20Topic.md)
		- [Subscribing to a ROS Topic](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Subscribing%20to%20a%20ROS%20Topic.md)
	- different [Message](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Message.md)
		- [Creating a Custom ROS Message](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Creating%20a%20Custom%20ROS%20Message.md)
	- [Service](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Service.md)
		- [Creating a Client Node](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Creating%20a%20Client%20Node.md)
		- [Creating a Server Node](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Creating%20a%20Server%20Node.md)
	- [Parameter](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Parameter.md)
		- [Parameter Server](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Parameter%20Server.md)
		

- **Reviewing:**
	- [ROS Workspace](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/ROS%20Workspace.md)
	- [Package](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Package.md)

- **Errors:**
	- [Unable to load robot model in rviz](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Unable%20to%20load%20robot%20model%20in%20rviz.md) 
	- [Guest Additions Installation](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Guest%20Additions%20Installation.md)

## Week 2
added minimal configuration for [Cmdline Tools](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Cmdline%20Tools.md)
[bashrc config](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/bashrc%20config.md)

- [Message](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Message.md)
	- [OccupancyGrid](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/OccupancyGrid.md)
	- [imu](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/imu.md) 

- [SLAM](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/SLAM.md)
	- [Transform](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Transform.md)
	- [Hector_Mapping](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Hector_Mapping.md)
	- [Gmapping](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Gmapping.md)

- [Navigation1](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Navigation1.md)
	- [move_base](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/move_base.md)
		- [Dynamic Window Approach](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Dynamic%20Window%20Approach.md)
	- [amcl](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/amcl.md)
	- [Costmap](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Costmap.md)
	- [Recovery Behaviors](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Recovery%20Behaviors.md)

- [dwa_local_planner](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/dwa_local_planner.md)
- [teb_local_planner](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/teb_local_planner.md)
- [Action](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Action.md)

- Installation Logs:
	- [Cartographer Installation](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Cartographer%20Installation.md)
	- [Turtlebot3](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Turtlebot3.md)

- Solved issues
	- [Unable to load robot model in rviz](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Unable%20to%20load%20robot%20model%20in%20rviz.md)
	- [Cartographer Installation](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Cartographer%20Installation.md) see Errors section

## Week 3

size of burger is: 138 x 178 x 192 mm


What is [Cartographer](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Cartographer.md)
[Steps to Using Cartographer](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Steps%20to%20Using%20Cartographer.md)

- [parameter tuning](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/parameter%20tuning.md)
	- [local_costmap](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/local_costmap.md) 
	- [global_costmap](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/global_costmap.md)
	- [move_base](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/move_base.md)
	- [teb_local_planner](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/teb_local_planner.md)
	- [teb_local_planner Parameters](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/teb_local_planner%20Parameters.md)

- Exploring alternative to A\* for global planner
	- [Jump Point Search](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Jump%20Point%20Search.md)

[Autonomous Exploration](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Autonomous%20Exploration.md)

fixed an error where the costmap won't show up when using cartographer:
[global_costmap](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/global_costmap.md) > Errors

[Cartographer Integration Errors](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Cartographer%20Integration%20Errors.md)

learning about [ROS2](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/ROS2.md)

## Week 4
[ROS2 Installation](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/ROS2%20Installation.md)
[ROS2 Packages](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/ROS2%20Packages.md)
[Navigation2](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Navigation2.md)
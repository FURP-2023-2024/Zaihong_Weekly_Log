---
Aliases: [ "#3-resources/ROS/Packages" ]
---
# Package
#3-resources/ROS #1-projects/FURP 

## 1. Definition
- The basic unit in ROS software, which includes node source code, configuration files, data definitions, etc.

**Package Manifest**
- Records the basic information of the function package, including author information, licensing information, dependency options, compilation flags, etc.

**Meta Packages**
- Organizes multiple function packages that serve the same purpose.

## 2. Creating a package
Run the following in the src directory of the [ROS Workspace](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/ROS%20Workspace.md)
```bash
# common dependencies are rospy roscpp std_msgs ...
catkin_create_pkg <pkg_name> [dependency1] [dependency2] ...
```
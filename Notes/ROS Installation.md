# ROS Installation
#3-resources/Linux/Ubuntu #1-projects/FURP #3-resources/ROS

[Official Installation Guide](https://wiki.ros.org/noetic/Installation/Ubuntu)
## 1. Repositories Setup
### 1.1. Sources List
Find mirrors here: [ROS/Installation/UbuntuMirrors - ROS Wiki](https://wiki.ros.org/ROS/Installation/UbuntuMirrors#China)

```bash
sudo sh -c '. /etc/lsb-release && echo "deb http://mirrors.ustc.edu.cn/ros/ubuntu/ `lsb_release -cs` main" > /etc/apt/sources.list.d/ros-latest.list'
```

#### 1.1.1. gpg: no valid OpenPGP data found.

```bash
wget http://packages.ros.org/ros.key  
sudo apt-key add ros.key  
sudo apt-get update --fix-missing
```

### 1.2. [rosdep init failure](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/rosdep%20init%20failure.md)


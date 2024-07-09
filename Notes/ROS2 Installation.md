# ROS2 Installation
#3-resources/ROS2 #1-projects/FURP

https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html
https://gitee.com/gwmunan/ros2/wikis/pages

> ubuntu 22.04

some useful tools
```bash
sudo apt update && sudo apt install -y \
  python3-flake8-docstrings \
  python3-pip \
  python3-pytest-cov \
  ros-dev-tools
```

in bashrc:
```bash
# for ros core
source /opt/ros/humble/setup.bash

# for colcon autocompletions
source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
```
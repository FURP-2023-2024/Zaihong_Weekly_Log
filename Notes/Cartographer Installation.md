# Cartographer Installation
#1-projects/FURP 

## 1. Official Install Guide
[Compiling Cartographer ROS — Cartographer ROS documentation (google-cartographer-ros.readthedocs.io)](https://google-cartographer-ros.readthedocs.io/en/latest/compilation.html)


## 2. Errors

### 2.1. Unable to Connect to gitubusercontent.com
```error
$ wstool merge -t src https://raw.githubusercontent.com/cartographer-project/cartographer_ros/master/cartographer_ros.rosinstall  

>>> 
ERROR in config: Unable to download URL [https://raw.githubusercontent.com/cartographer-project/cartographer_ros/master/cartographer_ros.rosinstall]:   <urlopen error [Errno 111] Connection refused>
```

**Solution:**
> Change IP address
```bash
sudo sh -c "echo 185.199.110.133 raw.githubusercontent.com >> /etc/hosts"
```

### 2.2. libabsl-dev not available in ubuntu 20.04
```
$ rosdep install --from-paths src --ignore-src --rosdistro=${ROS_DISTRO} -y

>>>

ERROR: the following packages/stacks could not have their rosdep keys resolved
to system dependencies:
cartographer: [libabsl-dev] defined as "not available" for OS version [focal]
```

**Solution:**

> comment out the depend libasbsi-dev in `package.xml`


### 2.3. Issue: Incompatible Workspace Paths

When compiling projects like Turtlebot and Cartographer in separate ROS (Robot Operating System) workspaces, conflicts may arise due to different versions of the same package within each workspace. The default behavior of the `setup.bash` script is to remove paths from `$ROS_PACKAGE_PATH` that do not have a direct dependency on the already sourced workspaces to resolve such conflicts.

**Solution:**
To avoid losing the path of one workspace when sourcing another, use the `--extend` option with the `source` command. This allows both workspaces to coexist in the `$ROS_PACKAGE_PATH` without interference.

Example `.bashrc`
```bash
source $HOME/catkin_ws/devel/setup.bash
source $HOME/turtlebot_ws/devel/setup.bash
source $HOME/cartographer_ws/install_isolated/setup.bash --extend
```

This approach ensures that both Turtlebot and Cartographer workspaces are accessible, with Cartographer benefiting from its isolated build environment created by `catkin_make_isolated --use-ninja`.
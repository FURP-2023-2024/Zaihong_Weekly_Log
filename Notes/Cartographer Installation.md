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
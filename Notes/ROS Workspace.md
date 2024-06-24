# ROS Workspace
#1-projects/FURP #3-resources/ROS 

## 1. Setting up a workspace
1. creating a workspace
```bash
# workspace name can be chosen as you like
# but the src directory cannot be changed
mkdir -p catkin_ws/src
cd catkin_ws/src
# run the following in the src directory
catkin_init_workspace
```
2. compiling the workspace
```bash
cd catkin_ws
# run the following in the root dir of the workspace
cakin_make
```
3. setting env variables
```bash
# you can also put this in .bashrc
source catkin_ws/devel/setup.bash
```
4. checking if env variables are set correctly
```bash
echo $ROS_PACKAGE_PATH
```



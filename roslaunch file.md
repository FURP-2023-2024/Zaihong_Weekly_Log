# roslaunch file
#3-resources/ROS #1-projects/FURP 
## 1. Basic usage
use `*.xml` files

```xml
<launch>
<node pkg="atr_pkg" type="motor_node" name="motor_node"/>
<node pkg="atr_pkg" type="arm_node" name="arm_node"/>
</launch>
```

running the launch file
`roslaunch pkg_name launchfile.launch`

## 2. Parameters
`launch-prefix="gnome-terminal -e"`
- show node on a separate terminal
`output="screen"`
- show output to screen (ROS_WARN is not affected by this paramenter)

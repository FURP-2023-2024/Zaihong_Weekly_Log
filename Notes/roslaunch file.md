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

## 3. Tags

### 3.1. `node`
**Attributes:**
acts like `rosrun`

`pkg` specifices the package name
`type` specifies the name of the node within the package
`name` gives a node a name
`args` parameters passed to the node (see also `param` tag)
`ns` namespace

example:
```xml
<node pkg="rviz" type="rviz" name="rviz" args="-d $(find slam_pkg)/rviz/slam.rviz"/>
```


### 3.2. `include`
incorporates the contents of another launch file into the current one

example:
```xml
<include file="$(find wpr_simulation)/launch/wpb_stage_slam.launch"/>
```

### 3.3. `param`
parameters of the parent node

example 
```xml
    <node pkg="hector_mapping" type="hector_mapping" name="hector_mapping">
        <param name="map_update_distance_thresh" value="0.1"/>
        <param name="map_update_angle_thresh" value="0.1"/>
        <param name="map_pub_period" value="1"/>
    </node>
```
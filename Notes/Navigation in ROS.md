# Navigation in ROS
#3-resources/ROS #1-projects/FURP 

![Pasted image 20240625210408.png](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Pasted%20image%2020240625210408.png.md)

[move_base](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/move_base.md)
[Action](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Action.md)

## 1. Dependencies
`roscpp rospy` `move_base_msgs` `actionlib`

## 2. Launch
#### 2.1.1. A simple example
see [move_base](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/move_base.md) parameters
```xml
<launch>
    <!--- Run move_base -->
    <node pkg="move_base" type="move_base" name="move_base">
        <rosparam file="$(find wpb_home_tutorials)/nav_lidar/costmap_common_params.yaml" command="load" ns="global_costmap" />
        <rosparam file="$(find wpb_home_tutorials)/nav_lidar/costmap_common_params.yaml" command="load" ns="local_costmap" />
        <rosparam file="$(find wpb_home_tutorials)/nav_lidar/global_costmap_params.yaml" command="load" />
        <rosparam file="$(find wpb_home_tutorials)/nav_lidar/local_costmap_params.yaml" command="load" />
        <param name="base_global_planner" value="global_planner/GlobalPlanner" />
        <param name="base_local_planner" value="wpbh_local_planner/WpbhLocalPlanner" />
    </node>

    <!-- Run map server -->
    <node pkg="map_server" type="map_server" name="map_server" args="$(find wpr_simulation)/maps/map.yaml"/>

    <!--- Run AMCL -->
    <node pkg="amcl" type="amcl" name="amcl"/>

    <!--- Run rviz -->
    <node name="rviz" pkg="rviz" type="rviz" args="-d $(find wpr_simulation)/rviz/nav.rviz"/>
</launch>
```
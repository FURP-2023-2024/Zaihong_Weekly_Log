# Hector_Mapping
#3-resources/ROS/SLAM #3-resources/ROS/Packages #1-projects/FURP 
[hector_mapping - ROS Wiki](https://wiki.ros.org/hector_mapping)

some important [Topic](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Topic.md)s and [Message](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Message.md)s are listed below
**Subscribed Topics**
- [Topic](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Topic.md): [scan](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/scan.md)
- [Message](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Message.md): [LaserScan](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/LaserScan.md)

**Published Topics**
- [Topic](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Topic.md): [map](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/map.md)
- [Message](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Message.md): [OccupancyGrid](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/OccupancyGrid.md)


## 1. Parameters

- `map_update_distance_thresh`
	- Threshold for performing map updates in (m). The platform has to travel this far in meters or experience an angular change as described by the map_update_angle_thresh parameter since the last update before a map update happens.
- `map_update_angle_thresh`
	- Threshold for performing map updates (rad). The platform has to experience an angular change as described by this parameter of travel as far as specified by the map_update_distance_thresh parameter since the last update before a map update happens.
- `map_pub_period`
	- - The map publish period in seconds.
	

## 2. [Transform](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Transform.md)
calculates `map` to `scanmatcher_frame`
uses `odom` to keep `scanmatcher_frame` equal to `base_footprint`
different from [Gmapping](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Gmapping.md)

## 3. Launch
see [roslaunch file](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/roslaunch%20file.md) for basics of creating a launch file

```xml
<launch>
    <include file="$(find wpr_simulation)/launch/wpb_stage_slam.launch"/>
    <node pkg="hector_mapping" type="hector_mapping" name="hector_mapping"/>
    <node pkg="rviz" type="rviz" name="rviz" args="-d $(find slam_pkg)/rviz/slam.rviz"/>
    <node pkg="rqt_robot_steering" type="rqt_robot_steering" name="rqt_robot_steering"/>
</launch>
```

## 4. Limitations
If characteristic differences from sensor values are not detected, it cannot approximate distance travel correctly

see [Gmapping](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Gmapping.md)


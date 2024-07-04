# Costmap
#1-projects/FURP #3-resources/ROS 

map type visualization in rviz
[global_costmap](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/global_costmap.md)
[local_costmap](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/local_costmap.md)

to have the same base config for global and local, you can use `ns` attribute in `node` tag

(see [roslaunch file](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/roslaunch%20file.md))

common params

[ROS导航系统 | 代价地图的参数设置_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1GH4y1p7kd/?spm_id_from=pageDriver&vd_source=7bebd01634aa9bf248bd76a3a9a62bff)
```yaml
robot_radius: 0.25
inflation_radius: 0.5
obstacle_range: 6.0
raytrace_range: 6.0
observation_sources: base_lidar
base_lidar: {
    data_type: LaserScan,
    topic: /scan, 
    marking: true, 
    clearing: true
    }
```

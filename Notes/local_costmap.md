# local_costmap
#3-resources/ROS #1-projects/FURP 

[ROS导航系统 | 代价地图的参数设置_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1GH4y1p7kd/?spm_id_from=pageDriver&vd_source=7bebd01634aa9bf248bd76a3a9a62bff)
```yaml
local_costmap:
  global_frame: odom
  robot_base_frame: base_footprint
  static_map: false
  rolling_window: true
  width: 3.0
  height: 3.0
  update_frequency: 10.0
  publish_frequency: 10.0
  transform_tolerance: 1.0
```



# global_costmap
#1-projects/FURP #3-resources/ROS 

[ROS导航系统 | 代价地图的参数设置_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1GH4y1p7kd/?spm_id_from=pageDriver&vd_source=7bebd01634aa9bf248bd76a3a9a62bff)

```yaml
global_costmap:
  global_frame: map
  robot_base_frame: base_footprint
  static_map: true
  update_frequency: 1.0
  publish_frequency: 1.0
  transform_tolerance: 1.0

recovery_behaviors:
  - name: 'conservative_reset'
    type: 'clear_costmap_recovery/ClearCostmapRecovery'
  - name: 'rotate_recovery'
    type: 'rotate_recovery/RotateRecovery'
  - name: 'aggressive_reset'
    type: 'clear_costmap_recovery/ClearCostmapRecovery'

conservative_reset:
  reset_distance: 2.0
  layer_names: ["obstacle_layer"]

aggressive_reset:
  reset_distance: 0.0
  layer_names: ["obstacle_layer"]
```

## 1. Errors
add the following lines to common config to setup the costmap to have input from the sensor mounted on the robot
```yaml
map_type: costmap
observation_sources: scan
scan: {sensor_frame: base_scan, data_type: LaserScan, topic: scan, marking: true, clearing: true}
```

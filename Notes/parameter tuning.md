# parameter tuning
#1-projects/FURP 
[Turtlebot3-burger入门教程#foxy版#-Navigation2调参_创客智造ROS的技术博客_51CTO博客](https://blog.51cto.com/u_1790502/6084633)

size
138 x 178 x 192 mm
## 1. Costmap Params
[costmap_2d - ROS Wiki](https://wiki.ros.org/costmap_2d#Inflation)
**Costmap Common Params**
```yaml
robot_radius: 0.15
inflation_radius: 0.3

# add obstactle to costmap (set distance as the sensor distance)

obstacle_range: 6.0
raytrace_range: 6.0

# Threshold values for the costmap
lethal_threshold: 40
unknown_threshold: 20
marking_threshold: 0

# footprint: [-0.105, -0.105], [-0.105, 0.105], [0.041, 0.105], [0.041, -0.105](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/-0.105%2C%20-0.105%5D%2C%20%5B-0.105%2C%200.105%5D%2C%20%5B0.041%2C%200.105%5D%2C%20%5B0.041%2C%20-0.105.md)

cost_scaling_factor: 3.0

map_type: costmap
observation_sources: scan # an arbitary name for a sensor (there can be multiple added)
scan: {
	data_type: LaserScan, 
	sensor_frame: base_scan,
	topic: scan, 
	marking: true, # add obstactle to costmap
	clearing: true # delete obstacle shadow
}
```

**Global**
```yaml
global_costmap:
  global_frame: map
  robot_base_frame: base_footprint

  update_frequency: 10.0
  publish_frequency: 10.0
  
  # laser_frame -> base_footprint -> odom -> map
  # make the following larger if tf timeout
  transform_tolerance: 1
 
 # an empty map to start with and creates the map during navigation if set to false (but doesn't work with cartographer)
  static_map: true

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
**Local**

```yaml
local_costmap:
# setting odom as reference reduces obstacle positional errors for a local costmap creation
  global_frame: odom
  robot_base_frame: base_footprint

# set to lidar scanning frequency
  update_frequency: 10.0
  publish_frequency: 10.0
  transform_tolerance: 1

  static_map: false
  rolling_window: true
  width: 3
  height: 3
  resolution: 0.05
```

## 2. Errors
```text
[ERROR] [1704170973.897661461, 3938.652000000]: Global Frame: odom Plan Frame size 258: map
[ WARN] [1704170973.897699511, 3938.652000000]: Could not transform the global plan to the frame of the controller
[ERROR] [1704170973.897724570, 3938.652000000]: Could not get local plan
[ INFO] [1704170973.998262391, 3938.752000000]: Got new plan
[ERROR] [1704170973.998675448, 3938.753000000]: Extrapolation Error: Lookup would require extrapolation 0.001000000s into the future.  Requested time 3938.748000000 but the latest data is at time 3938.747000000, when looking up transform from frame [odom] to frame [map]
[ERROR] [1704170973.998714677, 3938.753000000]: Global Frame: odom Plan Frame size 258: map
```

in global costmap params set global frame from "odom" to "map"
```yaml
global_costmap:
	global_frame: map
```

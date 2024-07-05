# Cartographer
#1-projects/FURP 

## 1. Installation
[Cartographer Installation](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Cartographer%20Installation.md)

## 2. Usage
```bash
roslaunch cartographer_ros offline_backpack_2d.launch bag_filenames:=${HOME}/Downloads/b2-2016-04-05-14-44-52.bag
```

## 3. Parameters
**Increase Efficiency**
```lua
-- local
-- if the imu and odom is trustable
TRAJECTORY_BUILDER_2D.use_online_correlative_scan_matching = false
-- increase:
TRAJECTORY_BUILDER_2D.max_angle_radians
TRAJECTORY_BUILDER_2D.max_distance_meters

-- global
-- decrease:
MAP_BUILDER.pose_graph.constraint_builder.min_score
MAP_BUILDER.pose_graph.constraint_builder.max_constraint_distacne
MAP_BUILDER.pose_graph.constraint_builder.sampling_ratio
```

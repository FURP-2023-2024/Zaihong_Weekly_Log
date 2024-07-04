# move_base
#3-resources/ROS/Node #1-projects/FURP

[map_server](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/map_server.md)
sensor source
odometry source
sensor transforms
[amcl](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/amcl.md)

## 1. Parameters
### 1.1. `base_global_planner`

**Description:** sets the global planner
- navfn/NavfnROS (default)
- global_planner/Global_planner
	- dijkstra (default)
	- a\*

carrot_planner/Carrot_planner
custom_planners
### 1.2. `base_local_planner`
https://www.bilibili.com/video/BV1dq421w7e1/?spm_id_from=pageDriver&vd_source=7bebd01634aa9bf248bd76a3a9a62bff
**Description:** sets the local planner
- base_local_planner/TrajectoryPlannerROS (default)
- dwa_local_planner/EBandPlannerROS
	- [dwa_local_planner](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/dwa_local_planner.md)
	- [Dynamic Window Approach](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Dynamic%20Window%20Approach.md)
- teb_local_planner/TebLocalPlannerROS 
- wpbh_local_planner/WpbhLocalPlanner
- ...
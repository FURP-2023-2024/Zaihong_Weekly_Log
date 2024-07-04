# teb_local_planner
#3-resources/ROS/LocalPlanner #1-projects/FURP

[ROS导航系统 | TEB规划器 | TEB Planner_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1fM4m1f792/?spm_id_from=333.788&vd_source=7bebd01634aa9bf248bd76a3a9a62bff)

## 1. Installation
```bash
sudo apt install ros-noetic-teb-local-planner
```


## 2. Usage
in launch file:
```xml
<param name="base_local_planner" value="teb_local_planner/TebLocalPlannerROS"/>
<rosparam file="$(find auto_nav)/param/teb_local_planner_params.yaml"/>
```

in rviz:
- add path subscribe to move_base/TebLocalPlanner
- use billboards line style
- pose array subscribe to tebposes 


## 3. Parameters

[teb_local_planner Parameters](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/teb_local_planner%20Parameters.md)



### 3.1. Configuration
```bash
rosrun rqt_reconfigure rqt_reconfigure
```

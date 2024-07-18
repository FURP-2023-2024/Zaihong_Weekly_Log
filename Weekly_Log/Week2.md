## 1. Configuration for Cmd-line Tools
[fzf](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/fzf.md)
[zoxide](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/zoxide.md)
[tmux](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/tmux.md)
[bashrc config](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/bashrc%20config.md)


## 2. OccupancyGrid
**Reference:**
[nav_msgs/OccupancyGrid Documentation (ros.org)](https://docs.ros.org/en/lunar/api/nav_msgs/html/msg/OccupancyGrid.html)

## 3. Creating a map
1. [Publishing a ROS Topic](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Publishing%20a%20ROS%20Topic.md)
2. [Topic](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Topic.md) is `/map` [Message](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Message.md) type is [OccupancyGrid](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/OccupancyGrid.md)
3. use rviz to view the created map

### 3.1. Python Example
```python
#!/usr/bin/env python3

import rospy
from nav_msgs.msg import OccupancyGrid

if __name__ =="__main__":
    rospy.init_node("map_pub_node")
    pub = rospy.Publisher("/map", OccupancyGrid, queue_size=10)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        msg = OccupancyGrid()

        msg.header.frame_id = "test_map"
        msg.header.stamp = rospy.Time.now()

        msg.info.origin.position.x = 0
        msg.info.origin.position.y = 0
        msg.info.resolution = 1
        msg.info.width = 4
        msg.info.height = 2

        msg.data = [0] * 4 * 2
        msg.data[0] = 100
        msg.data[1] = 100
        msg.data[2] = 0
        msg.data[3] = -1

        pub.publish(msg)
        rate.sleep()
```

## 4. imu
### 4.1. Usage
#### 4.1.1. [Topic](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Topic.md)s
`imu/data_raw`
accelerometer + gyroscope
`imu/data`
accelerometer + gyroscope + orientation
`imu/mag` 
magnetic field

#### 4.1.2. How to get imu info
1. [Subscribing to a ROS Topic](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Subscribing%20to%20a%20ROS%20Topic.md)
2. use `TF` tools to convert quaternion to Euler angles

#### 4.1.3. C++ Example
```cpp
#include "ros/ros.h"
#include "sensor_msgs/Imu.h"
#include "tf/tf.h"

void IMU_Callback(sensor_msgs::Imu msg) {
    if (msg.orientation_covariance[0] < 0 )
    return;
    tf::Quaternion quaternion(
        msg.orientation.x,
        msg.orientation.y,
        msg.orientation.z,
        msg.orientation.w
    );
    double roll, pitch, yaw;
    tf::Matrix3x3(quaternion).getRPY(roll, pitch, yaw);
    roll = roll * 180 /M_PI;
    pitch = pitch * 180 /M_PI;
    yaw = yaw * 180 /M_PI;

    ROS_INFO("roll= %.0f pitch= %.0f yaw= %.0f", roll, pitch, yaw);

}

int main(int argc, char ** argv){
    ros::init(argc,argv, "imu_node");
    ros::NodeHandle n;
    ros::Subscriber imu_sub = n.subscribe("/imu/data/", 10, IMU_Callback);
    ros::spin();
    return 0;
}
```
#### 4.1.4. Python Example
```python
#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Imu
from tf.transformations import euler_from_quaternion
import math

def imu_callback (msg):
    if msg.orientation_covariance[0] < 0:
        return
    quaternion = [
        msg.orientation.x,
        msg.orientation.y,
        msg.orientation.z,
        msg.orientation.w,
    ]
    (roll, pitch, yaw) = euler_from_quaternion(quaternion)
    roll = roll * 180 /math.pi
    pitch = pitch * 180 /math.pi
    yaw = yaw * 180 /math.pi
    rospy.loginfo("roll= %.0f pitch = %.0f yaw= %.0f", roll, pitch, yaw)

if __name__ == "__main__":
    rospy.init_node("imu_node")
    imu_sub = rospy.Subscriber("/imu/data", Imu, imu_callback, queue_size=10)
    rospy.spin()

```

## 5. Basic SLAM Algorithms
### 5.1. Hector Mapping
[hector_mapping - ROS Wiki](https://wiki.ros.org/hector_mapping)

some important [Topic](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Topic.md)s and [Message](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Message.md)s are listed below
**Subscribed Topics**
- [Topic](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Topic.md): [scan](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/scan.md)
- [Message](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Message.md): [LaserScan](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/LaserScan.md)

**Published Topics**
- [Topic](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Topic.md): [map](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/map.md)
- [Message](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Message.md): [OccupancyGrid](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/OccupancyGrid.md)


#### 5.1.1. Parameters

- `map_update_distance_thresh`
	- Threshold for performing map updates in (m). The platform has to travel this far in meters or experience an angular change as described by the map_update_angle_thresh parameter since the last update before a map update happens.
- `map_update_angle_thresh`
	- Threshold for performing map updates (rad). The platform has to experience an angular change as described by this parameter of travel as far as specified by the map_update_distance_thresh parameter since the last update before a map update happens.
- `map_pub_period`
	- - The map publish period in seconds.
	

#### 5.1.2. [Transform](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Transform.md)
calculates `map` to `scanmatcher_frame`
uses `odom` to keep `scanmatcher_frame` equal to `base_footprint`
different from [Gmapping](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Gmapping.md)

#### 5.1.3. Launch
see [roslaunch file](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/roslaunch%20file.md) for basics of creating a launch file

```xml
<launch>
    <include file="$(find wpr_simulation)/launch/wpb_stage_slam.launch"/>
    <node pkg="hector_mapping" type="hector_mapping" name="hector_mapping"/>
    <node pkg="rviz" type="rviz" name="rviz" args="-d $(find slam_pkg)/rviz/slam.rviz"/>
    <node pkg="rqt_robot_steering" type="rqt_robot_steering" name="rqt_robot_steering"/>
</launch>
```

#### 5.1.4. Limitations
If characteristic differences from sensor values are not detected, it cannot approximate distance travel correctly

### 5.2. Gmapping
- [Gmapping](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Gmapping.md)

- [Navigation1](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Navigation1.md)
	- [move_base](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/move_base.md)
		- [Dynamic Window Approach](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Dynamic%20Window%20Approach.md)
	- [amcl](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/amcl.md)
	- [Costmap](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Costmap.md)
	- [Recovery Behaviors](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Recovery%20Behaviors.md)

- [dwa_local_planner](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/dwa_local_planner.md)
- [teb_local_planner](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/teb_local_planner.md)
- [Action](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Action.md)

- Installation Logs:
	- [Cartographer Installation](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Cartographer%20Installation.md)
	- [Turtlebot3](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Turtlebot3.md)

- Solved issues
	- [Unable to load robot model in rviz](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Unable%20to%20load%20robot%20model%20in%20rviz.md)
	- [Cartographer Installation](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Cartographer%20Installation.md) see Errors section
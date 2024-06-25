# imu
#3-resources/ROS/Messages #1-projects/FURP 
[sensor_msgs/Imu Documentation (ros.org)](https://docs.ros.org/en/noetic/api/sensor_msgs/html/msg/Imu.html)

## 1. Usage
### 1.1. [Topic](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Topic.md)s
`imu/data_raw`
accelerometer + gyroscope
`imu/data`
accelerometer + gyroscope + orientation
`imu/mag` 
magnetic field

### 1.2. How to get imu info
1. [Subscribing to a ROS Topic](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Subscribing%20to%20a%20ROS%20Topic.md)
2. use `TF` tools to convert quaternion to Euler angles

#### 1.2.1. C++ Example
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
#### 1.2.2. Python Example
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

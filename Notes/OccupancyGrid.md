# OccupancyGrid
#3-resources/ROS/Messages #1-projects/FURP 

**Reference:**
[nav_msgs/OccupancyGrid Documentation (ros.org)](https://docs.ros.org/en/lunar/api/nav_msgs/html/msg/OccupancyGrid.html)

## 1. Creating a map
1. [Publishing a ROS Topic](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Publishing%20a%20ROS%20Topic.md)
2. [Topic](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Topic.md) is `/map` [Message](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Message.md) type is [OccupancyGrid](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/OccupancyGrid.md)
3. use rviz to view the created map

### 1.1. Python Example
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
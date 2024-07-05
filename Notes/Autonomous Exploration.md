# Autonomous Exploration
#1-projects/FURP 

https://blog.csdn.net/m0_71775106/article/details/128394793
## 1. Converting map format
Cartographer constructed map consists of probability, instead of
`EMPTY UNKNOWN LETHAL`, which `m-explore` uses

node to convert:
```python
#!/usr/bin/env python3
import rospy
from nav_msgs.msg import OccupancyGrid

# ***************
#   OBSTACLE
M = 75
#   unknown
N = 50
#   free
# ----0-----
#   unknown
# ***************
def callback(cmap):
    data = list(cmap.data)
    for y in range(cmap.info.height):
        for x in range(cmap.info.width):
            i = x + (cmap.info.height - 1 - y) * cmap.info.width
            if data[i] >= M:  
                data[i] = 100
            elif (data[i] >= 0) and (data[i] < N):  # free
                data[i] = 0
            else:  # unknown
                data[i] = -1
    cmap.data = tuple(data)
    pub.publish(cmap)

if __name__ == "__main__":
    rospy.init_node('mapc_node', anonymous=True)
    sub = rospy.Subscriber('/map', OccupancyGrid, callback)
    pub = rospy.Publisher('/cmap', OccupancyGrid, queue_size=20)

    rospy.spin()

```


## 2. Modify explore.launch
~/catkin_ws/src/m-explore/explore/launch/explore.launch

```xml
change this to 
<param name="costmap_topic" value="map"/>
this:
<param name="costmap_topic" value="cmap"/>
```
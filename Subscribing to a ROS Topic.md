# Subscribing to a ROS Topic
#3-resources/ROS #1-projects/FURP 


1. set topic name and type of msg
2. use `NodeHandler` to subscibe to a topic and write a callback function
3. use `ros::spinOnce()` function to respond to msgs


python example:
```python
#!/usr/bin/env python3
#coding=utf-8
import rospy
from std_msgs.msg import String

def chao_callback(msg):
	rospy.loginfo(msg.data)

if __name__ == "__main__":
	rospy.init_node("ma_node")
	sub = rospy.Subscriber("kuai_shang_che", String, queue_size=10, callback=chao_callback)
	rospy.spin()
```
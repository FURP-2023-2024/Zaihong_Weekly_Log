# Subscribing to a ROS Topic
#3-resources/ROS #1-projects/FURP 

1. initalize a node
2. subscribe to a [Topic](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Topic.md)
3. `ros::spin()` to wait for [Message](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Message.md)
4. run the callback function upon data recieval

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
# Creating a Node in Python
#3-resources/ROS #1-projects/FURP 
Do not forget the shebang lines!
For earlier versions of ubuntu, the default python executable may be `python`, instead of `python 3`

[Making Python Node Executable](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Making%20Python%20Node%20Executable.md)

```python
#!/usr/bin/env python3
#coding=utf-8
import rospy
from std_msgs.msg import String

if __name__ == "__main__":
	rospy.init_node("chao_node")
	rospy.logwarn("node begin")
	pub = rospy.Publisher("kuai_shang_che", String, queue_size=10)
	rate = rospy.Rate(10)
	
	while not rospy.is_shutdown():
		rospy.loginfo("in loop")
		msg = String()
		msg.data = "rospy std_msg data"
		pub.publish(msg)
		rate.sleep()
```
really similar to [Creating a Node in cpp](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Creating%20a%20Node%20in%20cpp.md)
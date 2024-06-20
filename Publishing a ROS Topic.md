# Publishing a ROS Topic
#3-resources/ROS #1-projects/FURP 
1. create `NodeHandle` object
2. create `Publisher` object using `nh.advertize<std_msgs::String>(topic_name, bufr_size)` 
3. `#include <std_msgs/String.h>` 
4. create a msg "struct" `std_msgs::String msg;` and fill in the fields
5. finally pulish `pub.publish(msg);`


python example:
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
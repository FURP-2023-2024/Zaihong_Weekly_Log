# Creating a Client Node
#3-resources/ROS #1-projects/FURP 

1. initalize node
2. create a client object
3. send request to server
4. wait for response from server

cpp example:
```cpp
#include <ros/ros.h>
#include <turtlesim/Spawn.h>

int main(int argc, char** argv) {
	ros::init(argc, argv, "turtle_spawn");
	ros::NodeHandle n;
	
	// waits until the service is found
	ros::service::waitForService("/spawn");
	ros::ServiceClient add_turtle = n.serviceClient<turtlesim::Spawn>("/spawn");
	
	turtlesim::Spawn srv;
	srv.request.x = 2;
	srv.request.y = 2;
	srv.request.name = "turtle2";
	
	// waits for response
	add_turtle.call(srv);
	ROS_INFO("Spawned turtle successfully [name:%s]",srv.response.name.c_str());
}
```


python example:
```python
#!/usr/bin/env python3
import sys
import rospy
from turtlesim.srv import Spawn

def turtle_spawn():
	rospy.init_node("turtle_spawn")
	rospy.wait_for_service('/spawn', 10)
try:
	add_turtle = rospy.ServiceProxy("/spawn", Spawn)
	response = add_turtle(2,2,0,"turtle2")
	print(response.name)
except rospy.ServiceException as e:
	print(f"Service call failed: {e}")

if __name__ == "__main__":
	turtle_spawn()
```
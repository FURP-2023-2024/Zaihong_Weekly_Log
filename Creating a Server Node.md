# Creating a Server Node
#3-resources/ROS #1-projects/FURP 

1. Initialize a ROS node.
2. Create an instance of Server.
3. Loop to wait for service requests and enter the callback function.
4. In the callback function, complete the processing of the service function and provide the response data.

## 1. cpp example:
AddTwoInts.srv:
```srv
int64 a
int64 b
---
int64 sum
```

[Creating Custom Service Message](Creating%20Custom%20Service%20Message.md)

server class definition:
```cpp
#include "ros/ros.h"
#include "beginner_tutorials/AddTwoInts.h"

class Server
{
public:
    Server() {
        // Initialize the ROS node
        ros::init(ros::count_args(), ros::argv, "add_two_ints_server");
        
        // Create a node handle
        ros::NodeHandle n;

        // Create a service server, which will call the function below when received a request
        service = n.advertiseService("add_two_ints", &Server::handleAdd, this);
        
        // Spin to prevent the program from exiting until the node has been shutdown
        ros::spin();
    }

private:
    ros::ServiceServer service;

    // This function is called when the service receives a request
    bool handleAdd(beginner_tutorials::AddTwoInts::Request  &req,
                   beginner_tutorials::AddTwoInts::Response &res) {
        // Perform the service operation: add two integers
        res.sum = req.a + req.b;
        
        // Return true to indicate the service request was successfully processed
        return true;
    }
};

int main(int argc, char **argv) {
    // Create the server object
    Server server;

    return 0;
}
```

example 2:
```cpp
// The routine will request the /show_person service, the service data type is learning_service::Person
#include <ros/ros.h>
#include "learning_service/Person.h"

int main(int argc, char** argv) {
    // Initialize the ROS node
    ros::init(argc, argv, "person_client");

    // Create a node handle
    ros::NodeHandle node;

    // After discovering the /show_person service, create a service client to connect to the service named /show_person
    ros::service::waitForService("/show_person");
    ros::ServiceClient person_client = node.serviceClient<learning_service::Person>("/show_person");

    // Initialize the request data for learning_service::Person
    learning_service::Person srv;
    srv.request.name = "Tom";
    srv.request.age = 20;
    srv.request.sex = learning_service::Person::Request::male; // Assuming 'male' is an enum value

    // Request service call
    ROS_INFO("Call service to show person [name:%s, age:%d, sex:%d]", 
             srv.request.name.c_str(), srv.request.age, static_cast<int>(srv.request.sex));
    person_client.call(srv);

    // Display the result of the service call
    ROS_INFO("Show person result: %s", srv.response.result.c_str());

    return 0;
}
```

## 2. python example

```python
#!/usr/bin/env python
import rospy
from beginner_tutorials.srv import AddTwoInts, AddTwoIntsResponse

def handle_add(req):
    """Callback function to handle service requests."""
    result = req.a + req.b
    rospy.loginfo("Returning [%s + %s = %s]" % (req.a, req.b, result))
    return AddTwoIntsResponse(result)

def add_two_ints_server():
    """Initialize the ROS node and create a service server."""
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add)
    rospy.loginfo("Service 'add_two_ints' is ready to receive requests.")
    rospy.spin()  # Keep the service running

if __name__ == "__main__":
    add_two_ints_server()#!/usr/bin/env python
import rospy
from beginner_tutorials.srv import AddTwoInts, AddTwoIntsResponse

def handle_add(req):
    """Callback function to handle service requests."""
    result = req.a + req.b
    rospy.loginfo("Returning [%s + %s = %s]" % (req.a, req.b, result))
    return AddTwoIntsResponse(result)

def add_two_ints_server():
    """Initialize the ROS node and create a service server."""
    rospy.init_node('add_two_ints_server')
    s = rospy.Service('add_two_ints', AddTwoInts, handle_add)
    rospy.loginfo("Service 'add_two_ints' is ready to receive requests.")
    rospy.spin()  # Keep the service running

if __name__ == "__main__":
    add_two_ints_server()
```


**example 2:**
> person_server.py
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from learning_service.srv import Person, PersonResponse

def person_callback(req):
    # Display the request data
    rospy.loginfo("Person: name:%s, age:%d, sex:%d", req.name, req.age, req.sex)
    # Return feedback data
    return PersonResponse("OK")

def person_server():
    # ROS node initialization
    rospy.init_node('person_server')
    # Create a server named /show_person, register the callback function person_callback
    rospy.Service('/show_person', Person, person_callback)
    # Loop waiting for the callback function
    rospy.spin()

if __name__ == "__main__":
    person_server()
    print("Ready to show person information.")
```

> person_client.py
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from learning_service.srv import Person, PersonRequest

def person_client():
    # ROS node initialization
    rospy.init_node('person_client')
    # Wait until the service is available
    rospy.wait_for_service('/show_person')
    try:
        # Create a service proxy for the service named /show_person
        person_client = rospy.ServiceProxy('/show_person', Person)
        # Make a service call, input request data
        response = person_client("Tom", 20, PersonRequest.male)
        # Display the result of the service call
        print("Show person result: %s" % response.result)
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)

if __name__ == "__main__":
    person_client()
```
# Topic
#3-resources/ROS #1-projects/FURP 

## 1. Definition
A type of inter-process communication mechanism. It's a named data stream that can be published by one or more nodes and subscribed to by one or more other nodes.

## 2. Concepts
**Publishing**: A node can publish messages to a topic. These messages are data that the node wants to share with other nodes.

**Subscribing**: A node can subscribe to a topic to receive messages that are published to that topic.

## 3. Commands
`rostopic list` shows all topics
`rostopic echo` shows topic information
`rostopic hz` shows frequency


## 4. How to publish a topic
1. create `NodeHandle` object
2. create `Publisher` object using `nh.advertize<std_msgs::String>(topic_name, bufr_size)` 
3. `#include <std_msgs/String.h>` 
4. create a msg "struct" `std_msgs::String msg;` and fill in the fields
5. finally pulish `pub.publish(msg);`

[Message](Message.md)
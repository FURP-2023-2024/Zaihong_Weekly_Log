# Topic
#3-resources/ROS #1-projects/FURP 

## 1. Definition
A type of inter-process communication mechanism. It's a named data stream that can be published by one or more nodes and subscribed to by one or more other nodes.

Topics are managed by roshandler itself and is not owned by a singular publisher or subscriber

## 2. Concepts
**Publishing**: A node can publish messages to a topic. These messages are data that the node wants to share with other nodes.

**Subscribing**: A node can subscribe to a topic to receive messages that are published to that topic.

## 3. Commands
`rostopic list` shows all topics
`rostopic echo` shows topic information
`rostopic hz` shows frequency
`rqt_graph` shows a graphical relationship between publishers and subscribers


## 4. How to publish a topic
[Creating a Custom ROS Message](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Creating%20a%20Custom%20ROS%20Message.md)
[Publishing a ROS Topic](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Publishing%20a%20ROS%20Topic.md)
[Subscribing to a ROS Topic](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Subscribing%20to%20a%20ROS%20Topic.md)
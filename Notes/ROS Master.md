# ROS Master
#3-resources/ROS  #1-projects/FURP 

## 1. Definition
- Provides naming and registration services for [Node](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Node.md)s
- Tracks and records topic/service communications, assisting nodes in finding each other and establishing connections;
- Offers a parameter server where nodes store and retrieve runtime parameters.

## 2. Ways of Communication
- [Topic](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Topic.md) [Message](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Message.md) communication
	- uni-directional
	- async communication
	- many to many
	- buffer

- [Service](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Service.md)
	- bi-directional
	- synchronous
	- one to many
	- no buffer

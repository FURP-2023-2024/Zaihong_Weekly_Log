# ROS Master
#3-resources/ROS  #1-projects/FURP 

## 1. Definition
- Provides naming and registration services for [Node](Node.md)s
- Tracks and records topic/service communications, assisting nodes in finding each other and establishing connections;
- Offers a parameter server where nodes store and retrieve runtime parameters.

## 2. Ways of Communication
- [Topic](Topic.md) [Message](Message.md) communication
	- uni-directional
	- async communication
	- many to many
	- buffer

- [Service](Service.md)
	- bi-directional
	- synchronous
	- one to many
	- no buffer

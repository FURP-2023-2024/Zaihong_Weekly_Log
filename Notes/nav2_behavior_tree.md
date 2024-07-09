# nav2_behavior_tree
#3-resources/ROS2/Package #1-projects/FURP 
see [Behavior Tree](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Behavior%20Tree.md) reference

- Pipeline Sequence Node
	- success is returned to parent only if the rightmost child returns success
![Pasted image 20240708190722.png](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Pasted%20image%2020240708190722.png.md)

- Recovery Node
	- Main behavior
	- Additional behavior (fallback)

# VS Code Configuration
#1-projects/FURP #3-resources/ROS  
## 1. Build Default
```tasks.json
{
	"version": "2.0.0",
	"tasks": [{
		"type": "catkin_make",
		"args": [
			"--directory",
			"/home/robot/catkin ws"
		],
		"problemMatcher": [
			"$catkin-gcc"
		],
		"group": {
			"kind": "build",
			"isDefault": true
		},
		"label": "catkin make:build"
	}]
}
```
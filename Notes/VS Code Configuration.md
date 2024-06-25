# VS Code Configuration
#1-projects/FURP #3-resources/ROS  
## 1. Build Default
sets the default complier
`Ctrl + Shift + B` builds the projects automatically

in `.vscode/tasks.json`
```json
{
	"version": "2.0.0",
	"tasks": [{
		"type": "catkin_make",
		"args": [
			"--directory",
			"$HOME/catkin_ws"
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
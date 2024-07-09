# ROS2 Packages
#3-resources/ROS2 #1-projects/FURP 

## 1. Creating a package
1. create package directories and setup dependencies
```bash
ros2 pkg create <pkg_name> --build-type ament-python --dependencies rclpy
```

2. create a `.py` file in the main folder

3. modify `setup.py`:

```python
entry_points = {
	'console_scripts': [
		"<node_name> = <pkg_name>.<file_name>:main"
	]
}
```

4. build with `colcon build --symlink-install`

## 2. Errors
### 2.1. Colcon build fail with --symlink-install
**Error msg:**
```stderr
Starting >>> my_robot_controller --- stderr: my_robot_controller /usr/lib/python3/dist-packages/setuptools/command/easy_install.py:158: EasyInstallDeprecationWarning: easy_install command is deprecated. Use build and pip and other standards-based tools.   warnings.warn( --- Finished <<< my_robot_controller [1.03s]  Summary: 1 package finished [1.34s]   1 package had stderr output: my_robot_controller
```

**Solution:** downgrade setuptools
https://robotics.stackexchange.com/questions/101255/setuptoolsdeprecationwarning-setup-py-install-is-deprecated-use-build-and-pip

`pip install setuptools==58.2.0`


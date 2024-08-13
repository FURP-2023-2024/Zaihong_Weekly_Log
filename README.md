---
number headings: off, first-level 1, max 6, _.1.1.
---

Project logs are included in the Weekly_Log folder, the following is an executive summary of what has been installed on the provided aim-N305 and how to use the Go1 for future projects

## On-board Camera Integration Challenges

The Unitree camera SDK has exhibited compatibility issues with the nano boards on the Go1 robot, specifically preventing the transmission of camera feeds over UDP, except for the device at `unitree@192.168.123.15`. As a prospective solution, it is recommended to perform a complete software reflash, aligning with advice from Unitree's support team. Historical code modifications on devices with IP addresses ending in 12, 13, and 14 suggest prior attempts to address these issues.

For effective communication between a computer and the Go1 robot, the computer must be assigned a static IP within the `192.168.123.x` range. While documentation does not explicitly reserve specific IPs, those above 20 are less likely to conflict. Adjustments in the `trans_rect_config.yaml` file are necessary to direct the camera feed to the correct device, particularly when performing SLAM on a separate machine with an IP ending in 200.

If hardware decoding is unsupported, such as with `omxh264dec`, parameters within the GStreamer pipeline may need to be altered to utilize `avdec_h264`. This adjustment can be made within the `std::string udpBehindData` in the `example_getImageTrans.cc` from Unitree's GitHub repository. Should these measures fail, deleting the current OpenCV installation and compiling version 4.1.1 might be required. Direct camera stream observation can be facilitated by using the `-X` option during SSH connections to the Go1's nano board.

## Realsense D455 Utilization

To harness the capabilities of the Realsense D455, the `realsense2_camera` package must be cloned and built. When launching with `rs_camera.launch`, parameters `enable_accel:=true`, `enable_gyro:=true`, and `unite_imu_method:=linear_interpolation` should be included to utilize IMU data. The Realsense camera can be tested in mono and mono inertial modes of ORB-SLAM with the `image_publisher` package on the AIM-N305. This setup necessitates dependencies such as `ORB_SLAM3` and `orb_slam_ros`.

The `camera_base_link`, representing the camera's base, is mapped to `/camera` by default, as the `orb_slam_node` typically publishes transformations from `/world` to `/camera`. Adjustments can be made to better approximate the `/odom` of the robot.

## Usage Tips

To send high-level movement commands to the Go1 robot using ROS messages, the package `go1-math-motion` could be helpful. Instead of setting XY velocity and sending UDP packets, `go1-math-motion` converts `/cmd_vel` messages and creates and sends the commands as udp packets, which is helpful as `/cmd_vel` is the output of `move_base`. Credits to [GitHub - dbaldwin/go1-math-motion: Go1 high level control with ROS](https://github.com/dbaldwin/go1-math-motion).

IMU data received from the dog and the camera can be fused using a Kalman filter. Credits to [Fusing GPS, IMU and odom data - ROS Answers: Open Source Q&A Forum](https://answers.ros.org/question/304502/fusing-gps-imu-and-odom-data/).

Converting `/imu` and `/odom` data from the Go1 to ROS topics could also be simplified with reference to: [GitHub - aatb-ch/go1_republisher: Publish camera/imu/odometry as ROS topics on the Unitree Go1 dogs.](https://github.com/aatb-ch/go1_republisher).
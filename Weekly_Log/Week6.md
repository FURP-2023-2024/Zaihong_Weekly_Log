This week was focused on implementation on actual robot

## 1. [[Installing Packages for Go1]]
install dependencies
```bash
sudo apt-get install ros-noetic-controller-interface ros-noetic-gazebo-ros-control ros-noetic-joint-state-controller ros-noetic-effort-controllers ros-noetic-joint-trajectory-controller
```

[宇树机器狗Unitree Go1开发指南1：安装Unitree工具包_宇树机器狗go1路径规划-CSDN博客](https://blog.csdn.net/ZJFJhanxi/article/details/137887419?spm=1001.2014.3001.5502)
 
 to install unitree guide you need lcm and pthread
installing LCM: [Ubuntu20.04安装、编译LCM1.4.0教程_ubuntu20.04安装lcm-CSDN博客](https://blog.csdn.net/SunPengMSE/article/details/118398226?csdn_share_tail=%7B%22type%22%3A%22blog%22%2C%22rType%22%3A%22article%22%2C%22rId%22%3A%22118398226%22%2C%22source%22%3A%22ZJFJhanxi%22%7D&fromshare=blogdetail)

[unitreerobotics/unitree_guide (github.com)](https://github.com/unitreerobotics/unitree_guide)
[unitreerobotics/unitree_ros (github.com)](https://github.com/unitreerobotics/unitree_ros)
[unitreerobotics/unitree_ros_to_real (github.com)](https://github.com/unitreerobotics/unitree_ros_to_real)
## 2. Error: Could not find GTSAM
```
CMake Error at LIO-SAM/CMakeLists.txt:27 (find_package):
  By not providing "FindGTSAM.cmake" in CMAKE_MODULE_PATH this project has
  asked CMake to find a package configuration file provided by "GTSAM", but
  CMake did not find one.

  Could not find a package configuration file provided by "GTSAM" with any of
  the following names:

    GTSAMConfig.cmake
    gtsam-config.cmake

  Add the installation prefix of "GTSAM" to CMAKE_PREFIX_PATH or set
  "GTSAM_DIR" to a directory containing one of the above files.  If "GTSAM"
  provides a separate development package or SDK, be sure it has been
  installed.
```

For noetic:
[catkin_make in ROS Noetic [Error] · Issue #206 · TixiaoShan/LIO-SAM (github.com)](https://github.com/TixiaoShan/LIO-SAM/issues/206)
```bash
sudo add-apt-repository ppa:borglab/gtsam-release-4.0.3
sudo apt update
sudo apt install libgtsam-dev libgtsam-unstable-dev
```

## 3. Go1 Basic Usage

[Go1 — Unitree_Docs 1.0rc documentation (unitree-docs.readthedocs.io)](https://unitree-docs.readthedocs.io/en/latest/get_started/Go1_Edu.html)

Connect to hotspot created by Go1 (password: 00000000)

ssh into the sports host
```bash
ssh pi@192.168.12.1
```

- **Sending Commands to Go1:**
  - Launch `real.launch` with high level control:
    ```bash
    roslaunch unitree_legged_real real.launch ctrl_level:=highlevel
    ```
  - Run `example_walk` in another terminal:
    ```bash
    rosrun unitree_legged_real example_walk
    ```

- **High Level Control Parameters (example_walk.cpp):**
  - `head`: Array of bytes for command header.
  - `levelFlag`: Always set to `HIGHLEVEL`.
  - `frameReserve`, `SN`, `version`, `bandWidth`: default values used.
  - `mode`: Control mode (e.g., idle, walk, stand).
  - `gaitType`: Type of gait (e.g., idle, trot, stair climb).
  - `speedLevel`: Walking speed level (applicable in certain modes).
  - `footRaiseHeight`: Height of foot when raised.
  - `bodyHeight`: Height of the body.
  - `position`: Target position for walking.
  - `euler`: Rotation angles (yaw, pitch, roll).
  - `velocity`: Walking speed in forward-backward and rightward-leftward directions.
  - `yawSpeed`: Yaw rotation speed.
  - `bms`: Battery management system command.
  - `led`: LED settings.
  - `wirelessRemote`: Joystick controller commands.
  - `reserve`, `crc`: default values used.

- **Available Modes:**
  - **Mode 0**: Idle (stand).
  - **Mode 1**: Force stand (body height and pose).
  - **Mode 2**: Walk at specified velocity (gait type, body height, foot height, velocity, yaw speed).
  - **Mode 3**: Walk toward specified position (gait type, speed level, position, yaw rotation).
  - **Mode 4**: Path mode walking (not implemented).
  - **Mode 5**: Stand down.
  - **Mode 6**: Stand up (correct posture).
  - **Mode 7**: Damping (software emergency, no commands accepted).
  - **Mode 8**: Recovery stand.
  - **Mode 9**: Back flip.
  - **Mode 10**: Yaw 90 degree rotation with a jump.
  - **Mode 11**: Put hands up (praying).
  - **Mode 12, 13**: Dance.

## 4. Integration Method
![[Pasted image 20240719011452.png]]
### 4.1. gazebo -> scan 
- comes from lidar scan 
- can connect lidar directly to external computer and read data from there, reducing overload from internal controllers in go1
### 4.2. gazebo -> tf , joint states
- can be build using urdf file (lidar position be added) #todo 

---

The ==gray section== from the image above is to be replaced with robot provided data
data packets are sent to and from the Go1 with external devices (within LAN) using UDP protocal
### 4.3. cmd_vel -> gazebo
following parameters could be modified from `highCmd`

```cpp
uint8_t speedLevel;            // reserve
float footRaiseHeight;         // (unit: m, range: -0.06~0.03m, default: 0.09m), foot up height while walking, delta value
float bodyHeight;              // (unit: m, range: -0.13~0.03m, default: 0.31m), delta value
std::array<float, 2> position; // (unit: m), desired position in inertial frame, reserve
std::array<float, 3> euler;    // (unit: rad), roll pitch yaw in stand mode
							   // (range: roll : -0.75~0.75rad)
							   // (range: pitch: -0.75~0.75rad)
							   // (range: yaw  : -0.6~0.6rad)
std::array<float, 2> velocity; // (unit: m/s), forwardSpeed, sideSpeed in body frame
							   // (range: trot : vx:-1.1~1.5m/s,  vy:-1.0~1.0m/s)
							   // (range: run  : vx:-2.5~3.5m/s,  vy:-1.0~1.0m/s)
							   // (range: stair: vx:-0.2~0.25m/s, vy:-0.15~0.15m/s)
float yawSpeed;                // (unit: rad/s), rotateSpeed in body frame
							   // (range: trot : -4.0~4.0rad/s)
							   // (range: run  : -4.0~4.0rad/s)
							   // (range: stair: -0.7~0.7rad/s)
```

cmd_vel can be translated into cmds that the robot can understand and sent via udp:

```cpp
void callback(const geometry_msgs::Twist::ConstPtr &msg) {
	custom.high_cmd = rosMsg2Cmd(msg);
	unitree_legged_msgs::HighState high_state_ros;
	high_state_ros = state2rosMsg(custom.high_state);
	pub_high.publish(high_state_ros);
}
```

### 4.4. gazebo -> odom / imu
To implement slam, and acquire the position of the robot, the highState udp data packet could be 'subscibed' and republished as `/odom` and `/imu`

E.g.
```cpp
msg_imu.orientation.w = custom.high_state.imu.quaternion[0];
msg_imu.orientation.x = custom.high_state.imu.quaternion[1];
msg_imu.orientation.y = custom.high_state.imu.quaternion[2];
msg_imu.orientation.z = custom.high_state.imu.quaternion[3];

msg_imu.orientation.w = custom.high_state.imu.quaternion[0];
msg_imu.orientation.x = custom.high_state.imu.quaternion[1];
msg_imu.orientation.y = custom.high_state.imu.quaternion[2];
msg_imu.orientation.z = custom.high_state.imu.quaternion[3];
```

reference: [aatb-ch/go1_republisher: Publish camera/imu/odometry as ROS topics on the Unitree Go1 dogs. (github.com)](https://github.com/aatb-ch/go1_republisher)



Navigation (still learning)

see: [ngmor/unitree_nav: Setting up the Unitree Go1 with an RS-Helios-16P Lidar to work with the Nav2 stack for SLAM and autonomous navigation. (github.com)](https://github.com/ngmor/unitree_nav)
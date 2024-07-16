# Go1 Basic Usage
#1-projects/FURP 
[Go1 — Unitree_Docs 1.0rc documentation (unitree-docs.readthedocs.io)](https://unitree-docs.readthedocs.io/en/latest/get_started/Go1_Edu.html)

Connect to hotspot created by Go1 (password: 00000000)

ssh into the sports host
```bash
ssh pi@192.168.12.1
```


192.168.123.161

## 1. Core Differences From Gazebo Simuation:
- lacks imu data and odom
	

sample custiom message for dog info:
```
float64 stamp
uint8 mode
uint8 gait_type
uint8 speed_level
float32 foot_raise_height
float32 body height
float32[3] position
float32[3] euler
float32[2] velocity
float32 yaw_speed
```

## 2. Understand and Use the Given sdk (`comm.h`)
### 2.1. `HIGH_STATE`
```cpp
  typedef struct
  {
    std::array<uint8_t, 2> head; // reserve
    uint8_t levelFlag;           // reserve
    uint8_t frameReserve;        // reserve

    std::array<uint32_t, 2> SN;      // reserve
    std::array<uint32_t, 2> version; // reserve
    uint16_t bandWidth;
    IMU imu;
    std::array<MotorState, 20> motorState;
    BmsState bms;
    std::array<int16_t, 4> footForce;           // Data from foot airbag sensor
    std::array<int16_t, 4> footForceEst;        // reserve，typically zero
    uint8_t mode;                               // The current mode of the robot
    float progress;                             // reserve
    uint8_t gaitType;                           // 0.idle  1.trot  2.trot running  3.climb stair  4.trot obstacle
    float footRaiseHeight;                      // (unit: m, default: 0.08m), foot up height while walking
    std::array<float, 3> position;              // (unit: m), from own odometry in inertial frame, usually drift
    float bodyHeight;                           // (unit: m, default: 0.28m),
    std::array<float, 3> velocity;              // (unit: m/s), forwardSpeed, sideSpeed, rotateSpeed in body frame
    float yawSpeed;                             // (unit: rad/s), rotateSpeed in body frame
    std::array<float, 4> rangeObstacle;         // Distance to nearest obstacle
    std::array<Cartesian, 4> footPosition2Body; // foot position relative to body
    std::array<Cartesian, 4> footSpeed2Body;    // foot speed relative to body
    std::array<uint8_t, 40> wirelessRemote;     // Data from Unitree Joystick.
    uint32_t reserve;

    uint32_t crc;
  } HighState; // high level feedback
```

### 2.2. `HIGH_CMD`
```cpp
  typedef struct
  {
    std::array<uint8_t, 2> head; // reserve, no need to set.
    uint8_t levelFlag;           // reserve. No need to set, only need to set UDP class.
    uint8_t frameReserve;        // reserve

    std::array<uint32_t, 2> SN;      // reserve
    std::array<uint32_t, 2> version; // reserve
    uint16_t bandWidth;              // reserve
    uint8_t mode;                    // 0. idle, default stand
                                     // 1. force stand (controlled by dBodyHeight + ypr)
                                     // 2. target velocity walking (controlled by velocity + yawSpeed)
                                     // 3. target position walking (controlled by position + ypr[0]), reserve
                                     // 4. path mode walking (reserve for future release), reserve
                                     // 5. position stand down.
                                     // 6. position stand up
                                     // 7. damping mode
                                     // 8. recovery stand
                                     // 9. backflip, reserve
                                     // 10. jumpYaw, only left direction. Note, to use this mode, you need to set mode = 1 first.
                                     // 11. straightHand. Note, to use this mode, you need to set mode = 1 first.

    uint8_t gaitType;              // 0.idle
                                   // 1.trot
                                   // 2.trot running
                                   // 3.climb stair
                                   // 4.trot obstacle
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
    BmsCmd bms;
    std::array<LED, 4> led;                 // reserve
    std::array<uint8_t, 40> wirelessRemote; // reserve
    uint32_t reserve;

    uint32_t crc;
  } HighCmd; // high level control
```

### 2.3. `LOW_STATE`
### 2.4. `LOW_CMD`
### 2.5. `IMU`

```cpp
  typedef struct
  {
    std::array<float, 4> quaternion;    // quaternion, normalized, (w,x,y,z)
    std::array<float, 3> gyroscope;     // angular velocity （unit: rad/s)    (raw data)
    std::array<float, 3> accelerometer; // acceleration （unit: m/(s2))       (raw data)
    std::array<float, 3> rpy;           // euler angle（unit: rad)
    int8_t temperature;                 // the temperature of imu (unit: °C)
  } IMU;                                // when under accelerated motion, the attitude of the robot calculated by IMU will drift.
```

## 3. `loop.h`
set the frequency of cpu etc.


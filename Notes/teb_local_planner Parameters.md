# teb_local_planner Parameters
#3-resources/ROS/LocalPlanner #1-projects/FURP 

- odom_topic
    - The topic name for the robot's odometry data, which provides the robot's current position and orientation.

- teb_autosize
    - If set to `True`, the time horizon of the TebLocalPlanner will automatically adjust based on the robot's current velocity, allowing for dynamic adaptation to different speeds.

- dt_ref
    - The default time step for the TebLocalPlanner, which defines the interval between planned poses.

- dt_hysteresis
    - A threshold to adjust the time step based on the robot's velocity changes, ensuring that the planning is responsive to changes in speed.

- global_plan_overwrite_orientation
    - If set to `True`, the global path orientation will be overwritten by the local planner, which can help in following the path more accurately.

- max_global_plan_lookahead_dist
    - The maximum distance the local planner will look ahead in the global path, affecting how far ahead the planner considers the global plan.

- feasibility_check_no_poses
    - The number of poses in the global path to check for feasibility, which influences the thoroughness of the feasibility checks.

- max_vel_x
    - The maximum linear velocity of the robot in the x-direction, setting an upper limit for how fast the robot can move forward.

- max_vel_x_backwards
    - The maximum linear velocity of the robot when moving backwards, allowing different speeds for forward and reverse motion.

- max_vel_theta
    - The maximum angular velocity of the robot, determining how fast the robot can rotate.

- acc_lim_x
    - The maximum linear acceleration of the robot, which limits how quickly the robot can change its speed.

- acc_lim_theta
    - The maximum angular acceleration of the robot, limiting how quickly the robot can change its rotation speed.

- min_turning_radius
    - The minimum turning radius of the robot, which is the smallest circle the robot can make while turning.

- wheelbase
    - The distance between the robot's center of gravity and the wheels, which can affect the robot's turning dynamics.

- cmd_angle_instead_rotvel
    - If set to `True`, the command angle will be used instead of the rotation velocity, allowing for more precise rotational control.

- footprint_model
    - The model used to represent the robot's footprint, which can affect how the robot's shape is considered in path planning.

- xy_goal_tolerance
    - The tolerance for the robot to reach the goal in the xy-plane, determining how close the robot needs to be to consider the goal reached.

- yaw_goal_tolerance
    - The tolerance for the robot to reach the goal in the yaw angle, which sets the angular precision required to reach the goal orientation.

- min_obstacle_dist
    - The minimum distance the robot should maintain from obstacles, ensuring a safe buffer zone around the robot.

- inflation_dist
    - The distance by which obstacles are inflated to account for the robot's size, which helps in avoiding collisions by considering the robot's dimensions.

- include_costmap_obstacles
    - If set to `True`, the costmap will be used to detect obstacles, integrating additional sensor data into the planning process.

- costmap_obstacles_behind_robot_dist
    - The distance behind the robot where obstacles will still be considered, which can affect rear collision avoidance.

- obstacle_poses_affected
    - The number of key points affected by an obstacle, which influences how the presence of obstacles impacts the planned path.

- costmap_converter_plugin
    - The costmap converter plugin to use, which can affect how costmap data is interpreted and used in planning.

- no_inner_iterations
    - The number of inner iterations for the optimization process, which can affect the quality of the planned path.

- no_outer_iterations
    - The number of outer iterations for the optimization process, which can influence the overall performance and efficiency of the planner.

- weight_max_vel_x
    - The weight for the maximum velocity in the x-direction, which influences how much the planner prioritizes reaching the maximum forward speed.

- weight_max_vel_theta
    - The weight for the maximum velocity in the theta-direction, affecting how much the planner prioritizes reaching the maximum angular speed.

- weight_acc_lim_x
    - The weight for the linear acceleration limit, which affects how much the planner considers the robot's acceleration capabilities.

- weight_acc_lim_theta
    - The weight for the angular acceleration limit, influencing how much the planner accounts for the robot's ability to change angular speed.

- weight_kinematics_nh
    - The weight for non-holonomic kinematics, which affects how the planner handles the robot's movement constraints.

- weight_kinematics_forward_drive
    - The weight for forward driving, which can prioritize moving the robot forward in the planning process.

- weight_optimaltime
    - The weight for the time cost, which influences how much the planner aims to minimize the time to reach the goal.

- weight_obstacle
    - The weight for obstacle avoidance, which determines how much the planner prioritizes avoiding obstacles in the path.

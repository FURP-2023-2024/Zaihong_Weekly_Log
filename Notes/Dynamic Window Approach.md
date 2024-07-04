# Dynamic Window Approach
#1-projects/FURP 

considers the robot's current velocity and the velocities of nearby obstacles to predict their future positions.

 The algorithm dynamically generates a set of possible velocity commands for the robot, each of which is evaluated based on how well it avoids collisions while also moving the robot towards its goal.

 The velocities are scored on a cost function that typically includes factors such as distance to obstacles, the robot's distance from its goal, and the robot's path efficiency.

 The DWA then selects the velocity command with the lowest cost as the next action for the robot, allowing it to navigate safely and efficiently through dynamic environments where obstacles may move or appear unexpectedly.
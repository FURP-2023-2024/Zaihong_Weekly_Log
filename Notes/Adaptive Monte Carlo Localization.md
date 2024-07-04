# Adaptive Monte Carlo Localization
#1-projects/FURP 

It adapts to the uncertainty in the robot's position by using a set of random *samples*, known as particles, to represent the robot's possible locations.

These particles are then weighted according to the likelihood of the robot being at that location, given the sensor readings and the map of the environment.

The weights are updated as the robot moves and receives new sensor data, allowing the algorithm to converge on the most probable location of the robot.

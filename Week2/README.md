# Week 2 - ROS 2 Turtlesim LAB
-------------------------------------------------
## Steps Performed
-------------------------------------------------
### 1. Environment Setup
- Opened terminal and sourced ROS 2:
  source /opt/ros/humble/setup.bash

### 2. Launching Turtlesim
- Ran:
  ros2 run turtlesim turtlesim_node
- Observed turtle simulation window.

### 3. Controlling the Turtle
- Executed:
  ros2 run turtlesim turtle_teleop_key
- Controlled movement using keyboard.

### 4. Exploring Topics
- Listed topics:
  ros2 topic list
- Checked position data:
  ros2 topic echo /turtle1/pose

### 5. Sending Velocity Commands
- Published velocity commands:
  ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0}, angular: {z: 1.8}}"

### 6. Using Services
- Reset simulation:
  ros2 service call /reset std_srvs/srv/Empty

### 7. Using RQT
- Launched GUI tool:
  rqt
- Explored nodes, topics, and services visually.

### 8. Spawning Second Turtle
- Used /spawn service to create another turtle.
- Controlled it via /turtle2/cmd_vel.

------------------------------------------------------

## Observations

- ROS 2 works on a distributed system of nodes communicating via topics and services.
- Topics are used for continuous data exchange (e.g., position, velocity).
- Services are used for one-time actions like reset and spawn.
- Real-time updates from /turtle1/pose confirmed dynamic system behavior.
- Manual velocity publishing directly controls robot motion.
- RQT simplifies visualization of ROS architecture.
- Multiple turtles operate independently, showing multi-agent capability.

-----------------------------------------------------

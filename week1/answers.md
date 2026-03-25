# Week 1 - Post Lab Questions
**Submitted By:** Rohma Masood
**Submitted To:** Dr. Maria Akram

## Q1. Define: node, topic, package, workspace.

- **Node:** A node is a single executable process in ROS 2 that performs a specific computation, such as reading a sensor, controlling a motor, or processing data.

- **Topic:** A topic is a named communication channel over which nodes exchange messages in a publisher-subscriber pattern.

- **Package:** A package is a folder that contains ROS 2 source code, dependencies, and build configuration files needed to build and run one or more nodes.

- **Workspace:** A workspace is a directory (e.g., ~/ros2_ws) that contains one or more ROS 2 packages along with their build and install outputs.-

## Q2. Explain why sourcing is required. What happens if you do not source a workspace?

Sourcing a workspace (using `source install/setup.bash`) updates the environment variables in the current terminal so that ROS 2 can locate the installed packages and executables. If you do not source the workspace, ROS 2 will not be able to find your packages and commands like `ros2 run` or `ros2 pkg list` will either fail or not show your package.

## Q3. What is the purpose of colcon build? What folders does it generate?

`colcon build` compiles and installs all ROS 2 packages found in the `src/` directory of the workspace. It generates the following folders:
- **build/** - Contains intermediate build artifacts for each package.
- **install/** - Contains the installed packages and executables ready to be sourced and run.
- **log/** - Contains log files from the build process for debugging.

## Q4. In your own words, explain what the entry_points console script does in setup.py.

The `entry_points` console script in `setup.py` registers a command name that maps to a specific Python function inside your package. For example:
```
'simple_node = my_first_pkg.simple_node:main'
```
This tells ROS 2 that when you run `ros2 run my_first_pkg simple_node`, it should execute the `main()` function inside the `simple_node.py` file of the `my_first_pkg` package.

## Q5. Draw a diagram showing one publisher and one subscriber connected by a topic.
```
+-------------------+        /chatter topic        +-------------------+
|     Node A        |   -------------------------> |     Node B        |
|   (Publisher)     |                              |   (Subscriber)    |
|                   |   publishes String messages  |                   |
| publishes at 10Hz |   =========================> | receives and      |
|                   |                              | processes msgs    |
+-------------------+                              +-------------------+
```

- **Node A** publishes messages on the `/chatter` topic.
- **Node B** subscribes to the `/chatter` topic and receives those messages.
- The topic acts as the communication channel between them.

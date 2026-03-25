# Week 1 - ROS 2 Lab
**submitted By:** Rohma Masood
**Submitted To:** Dr. Maria Akram
---------------------------------------

## Description
This lab covers Linux basics, ROS 2 concepts, workspace setup, 
and creation of a first ROS 2 Python package and node.
----------------------------------------

## Commands Used
```bash
# Create workspace
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws
colcon build
source install/setup.bash

# Create package
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python my_first_pkg

# Build and run node
colcon build
source install/setup.bash
ros2 run my_first_pkg simple_node
------------------------------------------

## Problems Faced and Solutions

- **Could not create workspace:** In the beginning I faced issues 
  creating the ros2_ws directory. Fixed by using the correct command 
  `mkdir -p ~/ros2_ws/src` which creates all folders at once.

- **Directory navigation problems:** I faced confusion navigating 
  between directories in the terminal. Fixed by using `cd ~` to go 
  home first and then navigating step by step.

- **IndentationError in simple_node.py:** The class body was not 
  properly indented. Fixed by correcting the 4-space indentation 
  inside the class definition.

- **Workspace not sourced:** After building, the package was not 
  found until I ran `source install/setup.bash` in the same terminal.

- **GitHub repository not found:** When cloning, the repository URL 
  had a wrong username. Fixed by using the correct GitHub username 
  Rohma1805.

------------------------------------------
## Reflection
This lab was a great introduction to ROS 2 and Linux terminal usage. 
I learned how ROS 2 uses nodes and topics to build robot software. 
Setting up the workspace and creating my first package helped me 
understand how ROS 2 organizes code. The entry_points concept in 
setup.py was new to me but now I understand how ROS 2 maps commands 
to Python functions. Fixing the indentation error taught me to be 
careful with Python syntax. Overall this lab gave me a strong 
foundation for the coming weeks.

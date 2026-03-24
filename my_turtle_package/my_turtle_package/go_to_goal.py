import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

# SET YOUR TARGET LOCATION HERE
TARGET_X = 8.0
TARGET_Y = 8.0

class GoToGoal(Node):
    def __init__(self):
        super().__init__('go_to_goal')
        self.publisher_ = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.subscription = self.create_subscription(
            Pose,
            'turtle1/pose',
            self.pose_callback,
            10)
        self.pose = None

    def pose_callback(self, msg):
        self.pose = msg
        self.move_to_goal()

    def move_to_goal(self):
        if self.pose is None:
            return

        msg = Twist()

        # Calculate distance to target
        dist_x = TARGET_X - self.pose.x
        dist_y = TARGET_Y - self.pose.y
        distance = math.sqrt(dist_x**2 + dist_y**2)

        # Calculate angle to target
        angle_to_goal = math.atan2(dist_y, dist_x)
        angle_diff = angle_to_goal - self.pose.theta

        if distance > 0.1:  # Keep moving until close enough
            msg.linear.x = 1.5 * distance
            msg.angular.z = 4.0 * angle_diff
        else:
            msg.linear.x = 0.0  # Stop when reached
            msg.angular.z = 0.0
            self.get_logger().info('Target reached!')

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = GoToGoal()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

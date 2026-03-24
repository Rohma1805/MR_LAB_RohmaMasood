import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn
import time

class MultiTurtleNode(Node):
    def __init__(self):
        super().__init__('multi_turtle_node')

        # Spawn turtle2
        self.spawn_turtle(2.0, 2.0, 0.0, 'turtle2')
        # Spawn turtle3
        self.spawn_turtle(8.0, 2.0, 0.0, 'turtle3')
        # Spawn turtle4
        self.spawn_turtle(5.0, 8.0, 0.0, 'turtle4')

        # Publishers for each turtle
        self.pub2 = self.create_publisher(Twist, 'turtle2/cmd_vel', 10)
        self.pub3 = self.create_publisher(Twist, 'turtle3/cmd_vel', 10)
        self.pub4 = self.create_publisher(Twist, 'turtle4/cmd_vel', 10)

        self.timer = self.create_timer(0.5, self.timer_callback)

    def spawn_turtle(self, x, y, theta, name):
        client = self.create_client(Spawn, '/spawn')
        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for spawn service...')
        request = Spawn.Request()
        request.x = x
        request.y = y
        request.theta = theta
        request.name = name
        client.call_async(request)
        time.sleep(1)

    def timer_callback(self):
        # turtle2 moves in a circle
        msg2 = Twist()
        msg2.linear.x = 2.0
        msg2.angular.z = 1.0
        self.pub2.publish(msg2)

        # turtle3 moves straight
        msg3 = Twist()
        msg3.linear.x = 1.0
        msg3.angular.z = 0.0
        self.pub3.publish(msg3)

        # turtle4 spins in place
        msg4 = Twist()
        msg4.linear.x = 0.0
        msg4.angular.z = 2.0
        self.pub4.publish(msg4)

def main(args=None):
    rclpy.init(args=args)
    node = MultiTurtleNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen
from functools import partial


class turtleControlNode(Node):
    def __init__(self):
        super().__init__("turtle_controller")
        self.get_logger().info("Successfully started turtle_controller node")
        self.pose_subscriber = self.create_subscription(Pose, "/turtle1/pose", self.controller_node, 10)
        self.cmd_vel_publisher = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.previous_x = 0

    def controller_node(self, pose:Pose):
        cmd = Twist()
        if pose.x > 9.0 or pose.x < 2.0 or pose.y > 9.0 or pose.y < 2.0:
            cmd.linear.x = 1.0
            cmd.angular.z = 0.9 #goes counterclockwise, think unit circle
        else:
            cmd.linear.x = 4.0
            cmd.angular.z = 0.0
        self.cmd_vel_publisher.publish(cmd)

        if pose.x > 5.5 and self.previous_x <= 5.5:
            self.previous_x = pose.x
            self.call_set_pen_service(255, 0, 0, 5, 0)
            self.get_logger().info("Set Color to Red")
        elif pose.x <=5.5 and self.previous_x > 5.5:
            self.previous_x = pose.x
            self.call_set_pen_service(0, 0, 255, 5, 0)
            self.get_logger().info("Set Color to Blue")

    def call_set_pen_service(self, r, g, b, width, off):
        client = self.create_client(SetPen, "/turtle1/set_pen")
        while not client.wait_for_service(1.0):
            self.get_logger().info("Waiting for Server...")
        
        request = SetPen.Request()
        request.r = r
        request.g = g
        request.b = b
        request.width = width
        request.off = off

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_set_pen))

    def callback_set_pen(self, future):
        try:
            response = future.result()
        except Exception as e:
            self.get_logger().error("Service call failed: %r" % (e,))


def main(args=None):
    rclpy.init(args=args)
    node = turtleControlNode()
    rclpy.spin(node)
    rclpy.shutdown()

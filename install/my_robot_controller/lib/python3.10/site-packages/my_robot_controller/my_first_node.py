#!/usr/bin/env python3
import rclpy

from rclpy.node import Node

class MyNode(Node): #our class MyNode inherits the Node class created
    def __init__(self):
        super().__init__('first_node') #name of node
        self.counter_ = 1
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Hello " + str(self.counter_))
        self.counter_ += 1


def main(args=None):
    rclpy.init(args=args)
    node = MyNode() #this object has attribute of a name 'first node'
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__': #built in var __name__ equals main when script is run
    main() #so basically just runs main function when script is run




#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from math import sin, cos, pi
from geometry_msgs.msg import Quaternion
from sensor_msgs.msg import JointState
from rclpy.qos import QoSProfile
from tf2_ros import TransformBroadcaster, TransformStamped

class StatePublisher(Node):

    def __init__(self):
        rclpy.init() #doing this here instead of in main function
        super().__init__('state_publisher')
        
        qos_profile = QoSProfile(depth=10)
        self.joint_pub = self.create_publisher(JointState, "joint_states", qos_profile)
        self.broadcaster = TransformBroadcaster(self, qos=qos_profile)
        self.nodeName = self.get_name()
        self.get_logger().info("{0} started".format(self.nodeName))

        degree = pi / 180.0
        loop_rate = self.create_rate(30) #creates the time interval we wait between each loop (30 hz)

        tilt = 0.
        tinc = degree #amount we move each time
        swivel = 0.
        angle = 0.
        height = 0.
        hinc = 0.005

        odom_trans = TransformStamped()
        odom_trans.header.frame_id = 'odom'
        odom_trans.child_frame_id = 'axis'
        joint_state = JointState()


        try:
            while rclpy.ok():
                rclpy.spin_once(self) #self is the node, which is why we pass it in here.

                now = self.get_clock().now() #gives time, idk why important
                joint_state.header.stamp = now.to_msg()
                joint_state.name = ['swivel', 'tilt', 'periscope']
                joint_state.position = [swivel, tilt, height]

                odom_trans.header.stamp = now.to_msg() #again gives time, idk why important
                odom_trans.transform.translation.x = cos(angle)*2
                odom_trans.transform.translation.y = sin(angle)*2
                odom_trans.transform.translation.z = 0.7
                odom_trans.transform.rotation = \
                    euler_to_quaternion(0,0, angle + pi/2)
                
                self.joint_pub.publish(joint_state)
                self.broadcaster.sendTransform(odom_trans)

                tilt += tinc
                if tilt < -0.5 or tilt > 0.0:
                    tinc*-1
                height += hinc
                if height > 0.2 or height < 0.0:
                    hinc *= -1

                swivel += degree
                angle += degree/4

                loop_rate.sleep() #pauses program for the 30 hz before beginning again


        except KeyboardInterrupt:
            pass        

def euler_to_quaternion(roll, pitch, yaw):
    qx = sin(roll/2) * cos(pitch/2) * cos(yaw/2) - cos(roll/2) * sin(pitch/2) * sin(yaw/2)
    qy = cos(roll/2) * sin(pitch/2) * cos(yaw/2) + sin(roll/2) * cos(pitch/2) * sin(yaw/2)
    qz = cos(roll/2) * cos(pitch/2) * sin(yaw/2) - sin(roll/2) * sin(pitch/2) * cos(yaw/2)
    qw = cos(roll/2) * cos(pitch/2) * cos(yaw/2) + sin(roll/2) * sin(pitch/2) * sin(yaw/2)
    return Quaternion(x=qx, y=qy, z=qz, w=qw)

def main(args=None):
    state_publisher = StatePublisher()

if __name__ == '__main__':
    main()
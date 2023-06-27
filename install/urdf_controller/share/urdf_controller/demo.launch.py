from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    ld = LaunchDescription()
    package_dir = get_package_share_directory('urdf_controller')
    urdf_file = os.path.join(package_dir, 'myfirst.urdf')
    rviz_config_file = os.path.join(package_dir, 'urdf.rviz')


    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{'robot_description': open(urdf_file, 'r').read()}]
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        arguments=['-d', rviz_config_file],
        output="screen"
    )

    joint_state_publisher_gui_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui"
    )

    ld.add_action(robot_state_publisher_node)
    ld.add_action(rviz_node)
    ld.add_action(joint_state_publisher_gui_node)
    return ld
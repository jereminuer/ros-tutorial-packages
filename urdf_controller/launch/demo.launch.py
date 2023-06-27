from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    ld = LaunchDescription()
    package_dir = get_package_share_directory('urdf_controller')
    urdf_file = os.path.join(package_dir, 'myfirst.urdf')


    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{'robot_description': open(urdf_file, 'r').read()}]
    )

    state_publisher_node = Node(
        package="urdf_controller",
        executable="state_publisher",
        name="state_publisher",
        output="screen"
    )

    ld.add_action(robot_state_publisher_node)
    ld.add_action(state_publisher_node)
    return ld
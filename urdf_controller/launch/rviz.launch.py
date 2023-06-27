from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    ld = LaunchDescription()
    package_dir = get_package_share_directory('urdf_controller')
    rviz_config = os.path.join(package_dir, 'urdf.rviz')

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        arguments=['-d', rviz_config],
        output="screen"
    )

    ld.add_action(rviz_node)
    return ld
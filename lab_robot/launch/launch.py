from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os
import xacro
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    ld = LaunchDescription()
    package_dir = get_package_share_directory('lab_robot')
    xacro_file = os.path.join(package_dir, 'test3.urdf')
    rviz_config = os.path.join(package_dir, 'turtlebot.rviz')

    #model_arg = DeclareLaunchArgument(name='model', default_value=str(xacro_file))
    #robot_description = ParameterValue(Command(['xacro', LaunchConfiguration('model')]),
                                       #value_type=str)
    #robot_description_config = xacro.process_file(xacro_file)
    #robot_description = robot_description_config.toxml()

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{'robot_description': open(xacro_file, 'r').read()}]
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        arguments=['-d', rviz_config],
        output="screen"
    )

    ld.add_action(robot_state_publisher_node)
    ld.add_action(rviz_node)
    return ld
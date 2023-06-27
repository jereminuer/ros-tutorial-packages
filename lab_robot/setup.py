from setuptools import setup

package_name = 'lab_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['urdf/turtlebot3_waffle.urdf.xacro']),
        ('share/' + package_name, ['urdf/turtlebot3_waffle.gazebo.xacro']),
        ('share/' + package_name, ['urdf/common_properties.xacro']),
        ('share/' + package_name, ['rviz/turtlebot.rviz']),
        ('share/' + package_name, ['launch/launch.py']),
        ('share/' + package_name, ['urdf/test3.urdf']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jeremi',
    maintainer_email='jeremi@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)

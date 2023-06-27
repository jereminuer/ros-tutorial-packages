from setuptools import setup

package_name = 'urdf_controller'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['launch/demo.launch.py']),
        ('share/' + package_name, ['launch/rviz.launch.py']),
        ('share/' + package_name, ['urdf/myfirst.urdf']),
        ('share/' + package_name, ['rviz/urdf.rviz']),
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
            "state_publisher = urdf_controller.state_publisher:main"
        ],
    },
)

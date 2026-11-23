import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # 1. Запуск стандартного мира TurtleBot3 (включает Gazebo и спавн робота)
    turtlebot3_gazebo_pkg = get_package_share_directory('turtlebot3_gazebo')
    world_launch_file = os.path.join(turtlebot3_gazebo_pkg, 'launch', 'turtlebot3_world.launch.py')
    
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(world_launch_file)
    )

    # 2. Запуск RViz с нашим конфигом
    pkg_dir = get_package_share_directory('my_project_bringup')
    rviz_config_path = os.path.join(pkg_dir, 'rviz', 'config.rviz')
    
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_path],
        output='screen'
    )

    return LaunchDescription([
        gazebo_launch,
        rviz_node
    ])

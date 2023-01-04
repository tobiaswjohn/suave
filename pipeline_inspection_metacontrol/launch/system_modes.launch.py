from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node, LifecycleNode

import os


def generate_launch_description():

    shm_model_path = os.path.join(
        get_package_share_directory('pipeline_inspection_metacontrol'),
        'config',
        'pipeline_inspection_modes.yaml')

    mode_manager_node = Node(
        package='system_modes',
        executable='mode_manager',
        parameters=[{'modelfile': shm_model_path}],
        output='screen')

    return LaunchDescription([
        mode_manager_node,
    ])

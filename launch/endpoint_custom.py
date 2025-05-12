from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            "tcp_ip",
            default_value="0.0.0.0",
            description="IP address to bind the TCP server to"
        ),
        DeclareLaunchArgument(
            "tcp_port",
            default_value="10000",
            description="TCP port for Unity connection"
        ),

        Node(
            package="ros_tcp_endpoint",
            executable="default_server_endpoint",
            name="tcp_server",
            parameters=[
                {"tcp_ip": LaunchConfiguration("tcp_ip")},
                {"tcp_port": LaunchConfiguration("tcp_port")}
            ],
            emulate_tty=True,
            output="screen"
        )
    ])

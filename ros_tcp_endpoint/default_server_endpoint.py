#!/usr/bin/env python

import rclpy
from rclpy.parameter import Parameter
from rclpy.node import Node
from ros_tcp_endpoint import TcpServer


def main(args=None):
    rclpy.init(args=args)

    node = Node("tcp_server_param_loader")
    node.declare_parameter("tcp_ip", "0.0.0.0")
    node.declare_parameter("tcp_port", 10000)

    tcp_ip = node.get_parameter("tcp_ip").get_parameter_value().string_value
    tcp_port = node.get_parameter("tcp_port").get_parameter_value().integer_value

    node.get_logger().info(f"[main] Launching TCP Server with IP: {tcp_ip}, PORT: {tcp_port}")

    # Pass the values to the TcpServer constructor
    tcp_server = TcpServer("UnityEndpoint", tcp_ip=tcp_ip, tcp_port=tcp_port)

    tcp_server.start()
    tcp_server.setup_executor()

    tcp_server.destroy_nodes()
    rclpy.shutdown()


if __name__ == "__main__":
    main()

from model import KubeConfig, ConnectionParameters
from kubernetes import client, config


def parse_kubeconfig(data: str) -> KubeConfig:
    """
    This function parses a kubeconfig file into a KubeConfig data structure.
    :param data: The KubeConfig data structure.
    :return:
    """
    pass


def kubeconfig_to_connection(data: KubeConfig) -> ConnectionParameters:
    """
    This function converts a KubeConfig structure into ConnectionParameters.
    :param data: The parsed KubeConfig data structure.
    :return: The Kubernetes connection parameters.
    :raises Exception: If the KubeConfig does not contain enough data to create the connection parameters
    (e.g. no context is set).
    """
    pass


def connection_to_kubeconfig(data: ConnectionParameters) -> KubeConfig:
    """
    This function converts the ConnectionParameters into an artificial KubeConfig for tools that can only work with that
    type of structure.
    :param data:
    :return:
    """
    pass


def connect(connection: ConnectionParameters) -> client.ApiClient:
    """
    This function creates a usable Kubernetes connection from the connection parameters.
    :param connection:
    :return:
    """
    pass

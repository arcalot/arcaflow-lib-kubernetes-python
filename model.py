import enum
import typing
from dataclasses import dataclass
from arcaflow_plugin_sdk import schema


@dataclass
class ConnectionParameters:
    """
    This is a connection specification matching the Go connection structure.
    """
    host: typing.Annotated[
        str,
        schema.name("Server"),
        schema.description("Kubernetes API URL"),
    ]
    path: typing.Annotated[
        typing.Optional[str],
        schema.name("API path"),
        schema.description("Kubernetes API path"),
    ] = None
    username: typing.Annotated[
        typing.Optional[str],
        schema.name("Username"),
        schema.description("Username to authenticate with."),
    ] = None
    password: typing.Annotated[
        typing.Optional[str],
        schema.name("Password"),
        schema.description("Password to authenticate with."),
    ] = None
    serverName: typing.Annotated[
        typing.Optional[str],
        schema.name("TLS server name"),
        schema.description("Server name to verify TLS certificate against.")
    ] = None
    cert: typing.Annotated[
        typing.Optional[str],
        schema.name("Client certificate"),
        schema.description("Client cert data in PEM format"),
    ] = None
    key: typing.Annotated[
        typing.Optional[str],
        schema.name("Client key"),
        schema.description("Client key in PEM format")
    ] = None
    cacert: typing.Annotated[
        typing.Optional[str],
        schema.name("CA certificate"),
        schema.description("CA certificate in PEM format")
    ] = None
    bearerToken: typing.Annotated[
        typing.Optional[str],
        schema.name("Token"),
        schema.description("Secret token of the user/service account"),
    ] = None


@dataclass
class KubeConfigClusterParams:
    server: typing.Annotated[str, schema.id("server"), schema.name("Server")]
    client_certificate: typing.Annotated[
        str,
        schema.id("certificate-authority"),
        schema.name("Certificate authority path"),
        schema.description(
            "Path to the certificate authority file. This path may not be portable across plugins, use with care."
        ),
        schema.conflicts("certificate-authority-data"),
        schema.required_if_not("insecure-skip-tls-verify")
    ]
    client_certificate_data: typing.Annotated[
        str,
        schema.id("certificate-authority-data"),
        schema.name("Certificate authority data"),
        schema.description(
            "Base64-encoded PEM data for the certificate authority."
        ),
        schema.conflicts("certificate-authority"),
        schema.required_if_not("insecure-skip-tls-verify")
    ]
    insecure_skip_tls_verify: typing.Annotated[
        typing.Optional[bool],
        schema.id("insecure-skip-tls-verify"),
        schema.name("Disable TLS certificate verification"),
        schema.description("Disables checking for the Kubernetes server certificate validity. Not recommended.")
    ] = False



@dataclass
class KubeConfigCluster:
    name: typing.Annotated[str, schema.name("Name")]
    cluster: typing.Annotated[KubeConfigClusterParams, schema.name("cluster")]


@dataclass
class KubeConfigContextParameters:
    cluster: typing.Annotated[str, schema.name("Cluster")]
    user: typing.Annotated[str, schema.name("User")]
    namespace: typing.Annotated[
        typing.Optional[str],
        schema.name("Namespace"),
        schema.description("Default namespace for operations. Often ignored."),
    ] = None


@dataclass
class KubeConfigContext:
    name: typing.Annotated[str, schema.name("Name")]
    context: typing.Annotated[KubeConfigContextParameters, schema.name("context")]


@dataclass
class KubeConfigUserParameters:
    token: typing.Annotated[
        str,
        schema.required_if_not("client-certificate"),
        schema.required_if_not("client-certificate-data"),
        schema.required_if_not("client-key"),
        schema.required_if_not("client-key-data"),
    ] = None
    client_certificate: typing.Annotated[
        str,
        schema.id("client-certificate"),
        schema.name("Client certificate path"),
        schema.description(
            "Path to the client certificate file. This path may not be portable across plugins, use with care."
        ),
    ] = None
    client_certificate_data: typing.Annotated[
        str,
        schema.id("client-certificate-data"),
        schema.name("Client certificate"),
        schema.description("Client certificate data Base64-encoded in PEM format."),
    ] = None
    client_key: typing.Annotated[
        str,
        schema.id("client-key"),
        schema.name("Client key path"),
        schema.description(
            "Path to the client key file. This path may not be portable across plugins, use with care."
        ),
    ] = None
    client_key_data: typing.Annotated[
        str,
        schema.id("client-key-data"),
        schema.name("Client key"),
        schema.description("Client key data Base64-encoded in PEM format."),
    ] = None


@dataclass
class KubeConfigUser:
    name: typing.Annotated[str, schema.name("Name")]
    user: typing.Annotated[KubeConfigUserParameters, schema.name("User")]


class KubeConfigKindEnum(enum.Enum):
    """
    This enum forces the Kind to always be "Config" for KubeConfig files.
    """
    Config="Config"


@dataclass
class KubeConfig:
    kind: typing.Annotated[KubeConfigKindEnum, schema.id("kind")]
    api_version: typing.Annotated[str, schema.id("apiVersion"), schema.min(2)]
    clusters: typing.Annotated[typing.List[KubeConfigCluster], schema.id("clusters")]
    contexts: typing.Annotated[typing.List[KubeConfigContext], schema.id("contexts")]
    users: typing.Annotated[typing.List[KubeConfigUser], schema.id("users")]
    current_context: typing.Annotated[typing.Optional[str], schema.name("current-context")] = None
    preferences: typing.Annotated[typing.Optional[any], schema.name("preferences")] = None

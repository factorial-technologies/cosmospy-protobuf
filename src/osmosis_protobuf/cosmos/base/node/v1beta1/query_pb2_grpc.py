"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from .....cosmos.base.node.v1beta1 import query_pb2 as cosmos_dot_base_dot_node_dot_v1beta1_dot_query__pb2

class ServiceStub(object):
    """Service defines the gRPC querier service for node related queries.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Config = channel.unary_unary('/cosmos.base.node.v1beta1.Service/Config', request_serializer=cosmos_dot_base_dot_node_dot_v1beta1_dot_query__pb2.ConfigRequest.SerializeToString, response_deserializer=cosmos_dot_base_dot_node_dot_v1beta1_dot_query__pb2.ConfigResponse.FromString)

class ServiceServicer(object):
    """Service defines the gRPC querier service for node related queries.
    """

    def Config(self, request, context):
        """Config queries for the operator configuration.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_ServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'Config': grpc.unary_unary_rpc_method_handler(servicer.Config, request_deserializer=cosmos_dot_base_dot_node_dot_v1beta1_dot_query__pb2.ConfigRequest.FromString, response_serializer=cosmos_dot_base_dot_node_dot_v1beta1_dot_query__pb2.ConfigResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('cosmos.base.node.v1beta1.Service', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Service(object):
    """Service defines the gRPC querier service for node related queries.
    """

    @staticmethod
    def Config(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.base.node.v1beta1.Service/Config', cosmos_dot_base_dot_node_dot_v1beta1_dot_query__pb2.ConfigRequest.SerializeToString, cosmos_dot_base_dot_node_dot_v1beta1_dot_query__pb2.ConfigResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....cosmos.autocli.v1 import query_pb2 as cosmos_dot_autocli_dot_v1_dot_query__pb2

class QueryStub(object):
    """RemoteInfoService provides clients with the information they need
    to build dynamically CLI clients for remote chains.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AppOptions = channel.unary_unary('/cosmos.autocli.v1.Query/AppOptions', request_serializer=cosmos_dot_autocli_dot_v1_dot_query__pb2.AppOptionsRequest.SerializeToString, response_deserializer=cosmos_dot_autocli_dot_v1_dot_query__pb2.AppOptionsResponse.FromString)

class QueryServicer(object):
    """RemoteInfoService provides clients with the information they need
    to build dynamically CLI clients for remote chains.
    """

    def AppOptions(self, request, context):
        """AppOptions returns the autocli options for all of the modules in an app.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'AppOptions': grpc.unary_unary_rpc_method_handler(servicer.AppOptions, request_deserializer=cosmos_dot_autocli_dot_v1_dot_query__pb2.AppOptionsRequest.FromString, response_serializer=cosmos_dot_autocli_dot_v1_dot_query__pb2.AppOptionsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('cosmos.autocli.v1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """RemoteInfoService provides clients with the information they need
    to build dynamically CLI clients for remote chains.
    """

    @staticmethod
    def AppOptions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.autocli.v1.Query/AppOptions', cosmos_dot_autocli_dot_v1_dot_query__pb2.AppOptionsRequest.SerializeToString, cosmos_dot_autocli_dot_v1_dot_query__pb2.AppOptionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....osmosis.poolmanager.v2 import query_pb2 as osmosis_dot_poolmanager_dot_v2_dot_query__pb2

class QueryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SpotPriceV2 = channel.unary_unary('/osmosis.poolmanager.v2.Query/SpotPriceV2', request_serializer=osmosis_dot_poolmanager_dot_v2_dot_query__pb2.SpotPriceRequest.SerializeToString, response_deserializer=osmosis_dot_poolmanager_dot_v2_dot_query__pb2.SpotPriceResponse.FromString)

class QueryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SpotPriceV2(self, request, context):
        """SpotPriceV2 defines a gRPC query handler that returns the spot price given
        a base denomination and a quote denomination.
        The returned spot price has 36 decimal places. However, some of
        modules perform sig fig rounding so most of the rightmost decimals can be
        zeroes.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'SpotPriceV2': grpc.unary_unary_rpc_method_handler(servicer.SpotPriceV2, request_deserializer=osmosis_dot_poolmanager_dot_v2_dot_query__pb2.SpotPriceRequest.FromString, response_serializer=osmosis_dot_poolmanager_dot_v2_dot_query__pb2.SpotPriceResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('osmosis.poolmanager.v2.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SpotPriceV2(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.poolmanager.v2.Query/SpotPriceV2', osmosis_dot_poolmanager_dot_v2_dot_query__pb2.SpotPriceRequest.SerializeToString, osmosis_dot_poolmanager_dot_v2_dot_query__pb2.SpotPriceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
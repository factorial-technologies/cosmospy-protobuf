import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import gogoproto
from .... import google
import google.protobuf.any_pb2
from .... import cosmos_proto
import google.protobuf.timestamp_pb2
from .... import osmosis

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def SpotPriceV2(self, stream: 'grpclib.server.Stream[osmosis.poolmanager.v2.query_pb2.SpotPriceRequest, osmosis.poolmanager.v2.query_pb2.SpotPriceResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/osmosis.poolmanager.v2.Query/SpotPriceV2': grpclib.const.Handler(self.SpotPriceV2, grpclib.const.Cardinality.UNARY_UNARY, osmosis.poolmanager.v2.query_pb2.SpotPriceRequest, osmosis.poolmanager.v2.query_pb2.SpotPriceResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.SpotPriceV2 = grpclib.client.UnaryUnaryMethod(channel, '/osmosis.poolmanager.v2.Query/SpotPriceV2', osmosis.poolmanager.v2.query_pb2.SpotPriceRequest, osmosis.poolmanager.v2.query_pb2.SpotPriceResponse)
import abc
import typing
import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server
from .... import gogoproto
from .... import osmosis
from .... import cosmos
from .... import google
import google.protobuf.any_pb2
from .... import cosmos_proto
import google.protobuf.timestamp_pb2
import google.protobuf.duration_pb2

class QueryBase(abc.ABC):

    @abc.abstractmethod
    async def Pools(self, stream: 'grpclib.server.Stream[osmosis.concentratedliquidity.v1beta1.query_pb2.PoolsRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.PoolsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def Params(self, stream: 'grpclib.server.Stream[osmosis.concentratedliquidity.v1beta1.query_pb2.ParamsRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.ParamsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UserPositions(self, stream: 'grpclib.server.Stream[osmosis.concentratedliquidity.v1beta1.query_pb2.UserPositionsRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.UserPositionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def LiquidityPerTickRange(self, stream: 'grpclib.server.Stream[osmosis.concentratedliquidity.v1beta1.query_pb2.LiquidityPerTickRangeRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.LiquidityPerTickRangeResponse]') -> None:
        pass

    @abc.abstractmethod
    async def LiquidityNetInDirection(self, stream: 'grpclib.server.Stream[osmosis.concentratedliquidity.v1beta1.query_pb2.LiquidityNetInDirectionRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.LiquidityNetInDirectionResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ClaimableSpreadRewards(self, stream: 'grpclib.server.Stream[osmosis.concentratedliquidity.v1beta1.query_pb2.ClaimableSpreadRewardsRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.ClaimableSpreadRewardsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def ClaimableIncentives(self, stream: 'grpclib.server.Stream[osmosis.concentratedliquidity.v1beta1.query_pb2.ClaimableIncentivesRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.ClaimableIncentivesResponse]') -> None:
        pass

    @abc.abstractmethod
    async def PositionById(self, stream: 'grpclib.server.Stream[osmosis.concentratedliquidity.v1beta1.query_pb2.PositionByIdRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.PositionByIdResponse]') -> None:
        pass

    @abc.abstractmethod
    async def PoolAccumulatorRewards(self, stream: 'grpclib.server.Stream[osmosis.concentratedliquidity.v1beta1.query_pb2.PoolAccumulatorRewardsRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.PoolAccumulatorRewardsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def IncentiveRecords(self, stream: 'grpclib.server.Stream[osmosis.concentratedliquidity.v1beta1.query_pb2.IncentiveRecordsRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.IncentiveRecordsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def TickAccumulatorTrackers(self, stream: 'grpclib.server.Stream[osmosis.concentratedliquidity.v1beta1.query_pb2.TickAccumulatorTrackersRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.TickAccumulatorTrackersResponse]') -> None:
        pass

    @abc.abstractmethod
    async def CFMMPoolIdLinkFromConcentratedPoolId(self, stream: 'grpclib.server.Stream[osmosis.concentratedliquidity.v1beta1.query_pb2.CFMMPoolIdLinkFromConcentratedPoolIdRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.CFMMPoolIdLinkFromConcentratedPoolIdResponse]') -> None:
        pass

    @abc.abstractmethod
    async def UserUnbondingPositions(self, stream: 'grpclib.server.Stream[osmosis.concentratedliquidity.v1beta1.query_pb2.UserUnbondingPositionsRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.UserUnbondingPositionsResponse]') -> None:
        pass

    @abc.abstractmethod
    async def GetTotalLiquidity(self, stream: 'grpclib.server.Stream[osmosis.concentratedliquidity.v1beta1.query_pb2.GetTotalLiquidityRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.GetTotalLiquidityResponse]') -> None:
        pass

    @abc.abstractmethod
    async def NumNextInitializedTicks(self, stream: 'grpclib.server.Stream[osmosis.concentratedliquidity.v1beta1.query_pb2.NumNextInitializedTicksRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.NumNextInitializedTicksResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {'/osmosis.concentratedliquidity.v1beta1.Query/Pools': grpclib.const.Handler(self.Pools, grpclib.const.Cardinality.UNARY_UNARY, osmosis.concentratedliquidity.v1beta1.query_pb2.PoolsRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.PoolsResponse), '/osmosis.concentratedliquidity.v1beta1.Query/Params': grpclib.const.Handler(self.Params, grpclib.const.Cardinality.UNARY_UNARY, osmosis.concentratedliquidity.v1beta1.query_pb2.ParamsRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.ParamsResponse), '/osmosis.concentratedliquidity.v1beta1.Query/UserPositions': grpclib.const.Handler(self.UserPositions, grpclib.const.Cardinality.UNARY_UNARY, osmosis.concentratedliquidity.v1beta1.query_pb2.UserPositionsRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.UserPositionsResponse), '/osmosis.concentratedliquidity.v1beta1.Query/LiquidityPerTickRange': grpclib.const.Handler(self.LiquidityPerTickRange, grpclib.const.Cardinality.UNARY_UNARY, osmosis.concentratedliquidity.v1beta1.query_pb2.LiquidityPerTickRangeRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.LiquidityPerTickRangeResponse), '/osmosis.concentratedliquidity.v1beta1.Query/LiquidityNetInDirection': grpclib.const.Handler(self.LiquidityNetInDirection, grpclib.const.Cardinality.UNARY_UNARY, osmosis.concentratedliquidity.v1beta1.query_pb2.LiquidityNetInDirectionRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.LiquidityNetInDirectionResponse), '/osmosis.concentratedliquidity.v1beta1.Query/ClaimableSpreadRewards': grpclib.const.Handler(self.ClaimableSpreadRewards, grpclib.const.Cardinality.UNARY_UNARY, osmosis.concentratedliquidity.v1beta1.query_pb2.ClaimableSpreadRewardsRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.ClaimableSpreadRewardsResponse), '/osmosis.concentratedliquidity.v1beta1.Query/ClaimableIncentives': grpclib.const.Handler(self.ClaimableIncentives, grpclib.const.Cardinality.UNARY_UNARY, osmosis.concentratedliquidity.v1beta1.query_pb2.ClaimableIncentivesRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.ClaimableIncentivesResponse), '/osmosis.concentratedliquidity.v1beta1.Query/PositionById': grpclib.const.Handler(self.PositionById, grpclib.const.Cardinality.UNARY_UNARY, osmosis.concentratedliquidity.v1beta1.query_pb2.PositionByIdRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.PositionByIdResponse), '/osmosis.concentratedliquidity.v1beta1.Query/PoolAccumulatorRewards': grpclib.const.Handler(self.PoolAccumulatorRewards, grpclib.const.Cardinality.UNARY_UNARY, osmosis.concentratedliquidity.v1beta1.query_pb2.PoolAccumulatorRewardsRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.PoolAccumulatorRewardsResponse), '/osmosis.concentratedliquidity.v1beta1.Query/IncentiveRecords': grpclib.const.Handler(self.IncentiveRecords, grpclib.const.Cardinality.UNARY_UNARY, osmosis.concentratedliquidity.v1beta1.query_pb2.IncentiveRecordsRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.IncentiveRecordsResponse), '/osmosis.concentratedliquidity.v1beta1.Query/TickAccumulatorTrackers': grpclib.const.Handler(self.TickAccumulatorTrackers, grpclib.const.Cardinality.UNARY_UNARY, osmosis.concentratedliquidity.v1beta1.query_pb2.TickAccumulatorTrackersRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.TickAccumulatorTrackersResponse), '/osmosis.concentratedliquidity.v1beta1.Query/CFMMPoolIdLinkFromConcentratedPoolId': grpclib.const.Handler(self.CFMMPoolIdLinkFromConcentratedPoolId, grpclib.const.Cardinality.UNARY_UNARY, osmosis.concentratedliquidity.v1beta1.query_pb2.CFMMPoolIdLinkFromConcentratedPoolIdRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.CFMMPoolIdLinkFromConcentratedPoolIdResponse), '/osmosis.concentratedliquidity.v1beta1.Query/UserUnbondingPositions': grpclib.const.Handler(self.UserUnbondingPositions, grpclib.const.Cardinality.UNARY_UNARY, osmosis.concentratedliquidity.v1beta1.query_pb2.UserUnbondingPositionsRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.UserUnbondingPositionsResponse), '/osmosis.concentratedliquidity.v1beta1.Query/GetTotalLiquidity': grpclib.const.Handler(self.GetTotalLiquidity, grpclib.const.Cardinality.UNARY_UNARY, osmosis.concentratedliquidity.v1beta1.query_pb2.GetTotalLiquidityRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.GetTotalLiquidityResponse), '/osmosis.concentratedliquidity.v1beta1.Query/NumNextInitializedTicks': grpclib.const.Handler(self.NumNextInitializedTicks, grpclib.const.Cardinality.UNARY_UNARY, osmosis.concentratedliquidity.v1beta1.query_pb2.NumNextInitializedTicksRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.NumNextInitializedTicksResponse)}

class QueryStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.Pools = grpclib.client.UnaryUnaryMethod(channel, '/osmosis.concentratedliquidity.v1beta1.Query/Pools', osmosis.concentratedliquidity.v1beta1.query_pb2.PoolsRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.PoolsResponse)
        self.Params = grpclib.client.UnaryUnaryMethod(channel, '/osmosis.concentratedliquidity.v1beta1.Query/Params', osmosis.concentratedliquidity.v1beta1.query_pb2.ParamsRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.ParamsResponse)
        self.UserPositions = grpclib.client.UnaryUnaryMethod(channel, '/osmosis.concentratedliquidity.v1beta1.Query/UserPositions', osmosis.concentratedliquidity.v1beta1.query_pb2.UserPositionsRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.UserPositionsResponse)
        self.LiquidityPerTickRange = grpclib.client.UnaryUnaryMethod(channel, '/osmosis.concentratedliquidity.v1beta1.Query/LiquidityPerTickRange', osmosis.concentratedliquidity.v1beta1.query_pb2.LiquidityPerTickRangeRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.LiquidityPerTickRangeResponse)
        self.LiquidityNetInDirection = grpclib.client.UnaryUnaryMethod(channel, '/osmosis.concentratedliquidity.v1beta1.Query/LiquidityNetInDirection', osmosis.concentratedliquidity.v1beta1.query_pb2.LiquidityNetInDirectionRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.LiquidityNetInDirectionResponse)
        self.ClaimableSpreadRewards = grpclib.client.UnaryUnaryMethod(channel, '/osmosis.concentratedliquidity.v1beta1.Query/ClaimableSpreadRewards', osmosis.concentratedliquidity.v1beta1.query_pb2.ClaimableSpreadRewardsRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.ClaimableSpreadRewardsResponse)
        self.ClaimableIncentives = grpclib.client.UnaryUnaryMethod(channel, '/osmosis.concentratedliquidity.v1beta1.Query/ClaimableIncentives', osmosis.concentratedliquidity.v1beta1.query_pb2.ClaimableIncentivesRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.ClaimableIncentivesResponse)
        self.PositionById = grpclib.client.UnaryUnaryMethod(channel, '/osmosis.concentratedliquidity.v1beta1.Query/PositionById', osmosis.concentratedliquidity.v1beta1.query_pb2.PositionByIdRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.PositionByIdResponse)
        self.PoolAccumulatorRewards = grpclib.client.UnaryUnaryMethod(channel, '/osmosis.concentratedliquidity.v1beta1.Query/PoolAccumulatorRewards', osmosis.concentratedliquidity.v1beta1.query_pb2.PoolAccumulatorRewardsRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.PoolAccumulatorRewardsResponse)
        self.IncentiveRecords = grpclib.client.UnaryUnaryMethod(channel, '/osmosis.concentratedliquidity.v1beta1.Query/IncentiveRecords', osmosis.concentratedliquidity.v1beta1.query_pb2.IncentiveRecordsRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.IncentiveRecordsResponse)
        self.TickAccumulatorTrackers = grpclib.client.UnaryUnaryMethod(channel, '/osmosis.concentratedliquidity.v1beta1.Query/TickAccumulatorTrackers', osmosis.concentratedliquidity.v1beta1.query_pb2.TickAccumulatorTrackersRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.TickAccumulatorTrackersResponse)
        self.CFMMPoolIdLinkFromConcentratedPoolId = grpclib.client.UnaryUnaryMethod(channel, '/osmosis.concentratedliquidity.v1beta1.Query/CFMMPoolIdLinkFromConcentratedPoolId', osmosis.concentratedliquidity.v1beta1.query_pb2.CFMMPoolIdLinkFromConcentratedPoolIdRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.CFMMPoolIdLinkFromConcentratedPoolIdResponse)
        self.UserUnbondingPositions = grpclib.client.UnaryUnaryMethod(channel, '/osmosis.concentratedliquidity.v1beta1.Query/UserUnbondingPositions', osmosis.concentratedliquidity.v1beta1.query_pb2.UserUnbondingPositionsRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.UserUnbondingPositionsResponse)
        self.GetTotalLiquidity = grpclib.client.UnaryUnaryMethod(channel, '/osmosis.concentratedliquidity.v1beta1.Query/GetTotalLiquidity', osmosis.concentratedliquidity.v1beta1.query_pb2.GetTotalLiquidityRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.GetTotalLiquidityResponse)
        self.NumNextInitializedTicks = grpclib.client.UnaryUnaryMethod(channel, '/osmosis.concentratedliquidity.v1beta1.Query/NumNextInitializedTicks', osmosis.concentratedliquidity.v1beta1.query_pb2.NumNextInitializedTicksRequest, osmosis.concentratedliquidity.v1beta1.query_pb2.NumNextInitializedTicksResponse)
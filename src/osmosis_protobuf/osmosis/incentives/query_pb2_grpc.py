"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ...osmosis.incentives import query_pb2 as osmosis_dot_incentives_dot_query__pb2

class QueryStub(object):
    """Query defines the gRPC querier service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ModuleToDistributeCoins = channel.unary_unary('/osmosis.incentives.Query/ModuleToDistributeCoins', request_serializer=osmosis_dot_incentives_dot_query__pb2.ModuleToDistributeCoinsRequest.SerializeToString, response_deserializer=osmosis_dot_incentives_dot_query__pb2.ModuleToDistributeCoinsResponse.FromString)
        self.GaugeByID = channel.unary_unary('/osmosis.incentives.Query/GaugeByID', request_serializer=osmosis_dot_incentives_dot_query__pb2.GaugeByIDRequest.SerializeToString, response_deserializer=osmosis_dot_incentives_dot_query__pb2.GaugeByIDResponse.FromString)
        self.Gauges = channel.unary_unary('/osmosis.incentives.Query/Gauges', request_serializer=osmosis_dot_incentives_dot_query__pb2.GaugesRequest.SerializeToString, response_deserializer=osmosis_dot_incentives_dot_query__pb2.GaugesResponse.FromString)
        self.ActiveGauges = channel.unary_unary('/osmosis.incentives.Query/ActiveGauges', request_serializer=osmosis_dot_incentives_dot_query__pb2.ActiveGaugesRequest.SerializeToString, response_deserializer=osmosis_dot_incentives_dot_query__pb2.ActiveGaugesResponse.FromString)
        self.ActiveGaugesPerDenom = channel.unary_unary('/osmosis.incentives.Query/ActiveGaugesPerDenom', request_serializer=osmosis_dot_incentives_dot_query__pb2.ActiveGaugesPerDenomRequest.SerializeToString, response_deserializer=osmosis_dot_incentives_dot_query__pb2.ActiveGaugesPerDenomResponse.FromString)
        self.UpcomingGauges = channel.unary_unary('/osmosis.incentives.Query/UpcomingGauges', request_serializer=osmosis_dot_incentives_dot_query__pb2.UpcomingGaugesRequest.SerializeToString, response_deserializer=osmosis_dot_incentives_dot_query__pb2.UpcomingGaugesResponse.FromString)
        self.UpcomingGaugesPerDenom = channel.unary_unary('/osmosis.incentives.Query/UpcomingGaugesPerDenom', request_serializer=osmosis_dot_incentives_dot_query__pb2.UpcomingGaugesPerDenomRequest.SerializeToString, response_deserializer=osmosis_dot_incentives_dot_query__pb2.UpcomingGaugesPerDenomResponse.FromString)
        self.RewardsEst = channel.unary_unary('/osmosis.incentives.Query/RewardsEst', request_serializer=osmosis_dot_incentives_dot_query__pb2.RewardsEstRequest.SerializeToString, response_deserializer=osmosis_dot_incentives_dot_query__pb2.RewardsEstResponse.FromString)
        self.LockableDurations = channel.unary_unary('/osmosis.incentives.Query/LockableDurations', request_serializer=osmosis_dot_incentives_dot_query__pb2.QueryLockableDurationsRequest.SerializeToString, response_deserializer=osmosis_dot_incentives_dot_query__pb2.QueryLockableDurationsResponse.FromString)
        self.AllGroups = channel.unary_unary('/osmosis.incentives.Query/AllGroups', request_serializer=osmosis_dot_incentives_dot_query__pb2.QueryAllGroupsRequest.SerializeToString, response_deserializer=osmosis_dot_incentives_dot_query__pb2.QueryAllGroupsResponse.FromString)
        self.AllGroupsGauges = channel.unary_unary('/osmosis.incentives.Query/AllGroupsGauges', request_serializer=osmosis_dot_incentives_dot_query__pb2.QueryAllGroupsGaugesRequest.SerializeToString, response_deserializer=osmosis_dot_incentives_dot_query__pb2.QueryAllGroupsGaugesResponse.FromString)
        self.AllGroupsWithGauge = channel.unary_unary('/osmosis.incentives.Query/AllGroupsWithGauge', request_serializer=osmosis_dot_incentives_dot_query__pb2.QueryAllGroupsWithGaugeRequest.SerializeToString, response_deserializer=osmosis_dot_incentives_dot_query__pb2.QueryAllGroupsWithGaugeResponse.FromString)
        self.GroupByGroupGaugeID = channel.unary_unary('/osmosis.incentives.Query/GroupByGroupGaugeID', request_serializer=osmosis_dot_incentives_dot_query__pb2.QueryGroupByGroupGaugeIDRequest.SerializeToString, response_deserializer=osmosis_dot_incentives_dot_query__pb2.QueryGroupByGroupGaugeIDResponse.FromString)
        self.CurrentWeightByGroupGaugeID = channel.unary_unary('/osmosis.incentives.Query/CurrentWeightByGroupGaugeID', request_serializer=osmosis_dot_incentives_dot_query__pb2.QueryCurrentWeightByGroupGaugeIDRequest.SerializeToString, response_deserializer=osmosis_dot_incentives_dot_query__pb2.QueryCurrentWeightByGroupGaugeIDResponse.FromString)

class QueryServicer(object):
    """Query defines the gRPC querier service
    """

    def ModuleToDistributeCoins(self, request, context):
        """ModuleToDistributeCoins returns coins that are going to be distributed
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GaugeByID(self, request, context):
        """GaugeByID returns gauges by their respective ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Gauges(self, request, context):
        """Gauges returns both upcoming and active gauges
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ActiveGauges(self, request, context):
        """ActiveGauges returns active gauges
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ActiveGaugesPerDenom(self, request, context):
        """ActiveGaugesPerDenom returns active gauges by denom
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpcomingGauges(self, request, context):
        """Returns scheduled gauges that have not yet occured
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpcomingGaugesPerDenom(self, request, context):
        """UpcomingGaugesPerDenom returns scheduled gauges that have not yet occured
        by denom
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RewardsEst(self, request, context):
        """RewardsEst returns an estimate of the rewards from now until a specified
        time in the future The querier either provides an address or a set of locks
        for which they want to find the associated rewards
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LockableDurations(self, request, context):
        """LockableDurations returns lockable durations that are valid to distribute
        incentives for
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AllGroups(self, request, context):
        """AllGroups returns all groups
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AllGroupsGauges(self, request, context):
        """AllGroupsGauges returns all group gauges
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AllGroupsWithGauge(self, request, context):
        """AllGroupsWithGauge returns all groups with their group gauge
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GroupByGroupGaugeID(self, request, context):
        """GroupByGroupGaugeID returns a group given its group gauge ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CurrentWeightByGroupGaugeID(self, request, context):
        """CurrentWeightByGroupGaugeID returns the current weight since the
        the last epoch given a group gauge ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'ModuleToDistributeCoins': grpc.unary_unary_rpc_method_handler(servicer.ModuleToDistributeCoins, request_deserializer=osmosis_dot_incentives_dot_query__pb2.ModuleToDistributeCoinsRequest.FromString, response_serializer=osmosis_dot_incentives_dot_query__pb2.ModuleToDistributeCoinsResponse.SerializeToString), 'GaugeByID': grpc.unary_unary_rpc_method_handler(servicer.GaugeByID, request_deserializer=osmosis_dot_incentives_dot_query__pb2.GaugeByIDRequest.FromString, response_serializer=osmosis_dot_incentives_dot_query__pb2.GaugeByIDResponse.SerializeToString), 'Gauges': grpc.unary_unary_rpc_method_handler(servicer.Gauges, request_deserializer=osmosis_dot_incentives_dot_query__pb2.GaugesRequest.FromString, response_serializer=osmosis_dot_incentives_dot_query__pb2.GaugesResponse.SerializeToString), 'ActiveGauges': grpc.unary_unary_rpc_method_handler(servicer.ActiveGauges, request_deserializer=osmosis_dot_incentives_dot_query__pb2.ActiveGaugesRequest.FromString, response_serializer=osmosis_dot_incentives_dot_query__pb2.ActiveGaugesResponse.SerializeToString), 'ActiveGaugesPerDenom': grpc.unary_unary_rpc_method_handler(servicer.ActiveGaugesPerDenom, request_deserializer=osmosis_dot_incentives_dot_query__pb2.ActiveGaugesPerDenomRequest.FromString, response_serializer=osmosis_dot_incentives_dot_query__pb2.ActiveGaugesPerDenomResponse.SerializeToString), 'UpcomingGauges': grpc.unary_unary_rpc_method_handler(servicer.UpcomingGauges, request_deserializer=osmosis_dot_incentives_dot_query__pb2.UpcomingGaugesRequest.FromString, response_serializer=osmosis_dot_incentives_dot_query__pb2.UpcomingGaugesResponse.SerializeToString), 'UpcomingGaugesPerDenom': grpc.unary_unary_rpc_method_handler(servicer.UpcomingGaugesPerDenom, request_deserializer=osmosis_dot_incentives_dot_query__pb2.UpcomingGaugesPerDenomRequest.FromString, response_serializer=osmosis_dot_incentives_dot_query__pb2.UpcomingGaugesPerDenomResponse.SerializeToString), 'RewardsEst': grpc.unary_unary_rpc_method_handler(servicer.RewardsEst, request_deserializer=osmosis_dot_incentives_dot_query__pb2.RewardsEstRequest.FromString, response_serializer=osmosis_dot_incentives_dot_query__pb2.RewardsEstResponse.SerializeToString), 'LockableDurations': grpc.unary_unary_rpc_method_handler(servicer.LockableDurations, request_deserializer=osmosis_dot_incentives_dot_query__pb2.QueryLockableDurationsRequest.FromString, response_serializer=osmosis_dot_incentives_dot_query__pb2.QueryLockableDurationsResponse.SerializeToString), 'AllGroups': grpc.unary_unary_rpc_method_handler(servicer.AllGroups, request_deserializer=osmosis_dot_incentives_dot_query__pb2.QueryAllGroupsRequest.FromString, response_serializer=osmosis_dot_incentives_dot_query__pb2.QueryAllGroupsResponse.SerializeToString), 'AllGroupsGauges': grpc.unary_unary_rpc_method_handler(servicer.AllGroupsGauges, request_deserializer=osmosis_dot_incentives_dot_query__pb2.QueryAllGroupsGaugesRequest.FromString, response_serializer=osmosis_dot_incentives_dot_query__pb2.QueryAllGroupsGaugesResponse.SerializeToString), 'AllGroupsWithGauge': grpc.unary_unary_rpc_method_handler(servicer.AllGroupsWithGauge, request_deserializer=osmosis_dot_incentives_dot_query__pb2.QueryAllGroupsWithGaugeRequest.FromString, response_serializer=osmosis_dot_incentives_dot_query__pb2.QueryAllGroupsWithGaugeResponse.SerializeToString), 'GroupByGroupGaugeID': grpc.unary_unary_rpc_method_handler(servicer.GroupByGroupGaugeID, request_deserializer=osmosis_dot_incentives_dot_query__pb2.QueryGroupByGroupGaugeIDRequest.FromString, response_serializer=osmosis_dot_incentives_dot_query__pb2.QueryGroupByGroupGaugeIDResponse.SerializeToString), 'CurrentWeightByGroupGaugeID': grpc.unary_unary_rpc_method_handler(servicer.CurrentWeightByGroupGaugeID, request_deserializer=osmosis_dot_incentives_dot_query__pb2.QueryCurrentWeightByGroupGaugeIDRequest.FromString, response_serializer=osmosis_dot_incentives_dot_query__pb2.QueryCurrentWeightByGroupGaugeIDResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('osmosis.incentives.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query defines the gRPC querier service
    """

    @staticmethod
    def ModuleToDistributeCoins(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.incentives.Query/ModuleToDistributeCoins', osmosis_dot_incentives_dot_query__pb2.ModuleToDistributeCoinsRequest.SerializeToString, osmosis_dot_incentives_dot_query__pb2.ModuleToDistributeCoinsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GaugeByID(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.incentives.Query/GaugeByID', osmosis_dot_incentives_dot_query__pb2.GaugeByIDRequest.SerializeToString, osmosis_dot_incentives_dot_query__pb2.GaugeByIDResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Gauges(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.incentives.Query/Gauges', osmosis_dot_incentives_dot_query__pb2.GaugesRequest.SerializeToString, osmosis_dot_incentives_dot_query__pb2.GaugesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ActiveGauges(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.incentives.Query/ActiveGauges', osmosis_dot_incentives_dot_query__pb2.ActiveGaugesRequest.SerializeToString, osmosis_dot_incentives_dot_query__pb2.ActiveGaugesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ActiveGaugesPerDenom(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.incentives.Query/ActiveGaugesPerDenom', osmosis_dot_incentives_dot_query__pb2.ActiveGaugesPerDenomRequest.SerializeToString, osmosis_dot_incentives_dot_query__pb2.ActiveGaugesPerDenomResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpcomingGauges(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.incentives.Query/UpcomingGauges', osmosis_dot_incentives_dot_query__pb2.UpcomingGaugesRequest.SerializeToString, osmosis_dot_incentives_dot_query__pb2.UpcomingGaugesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpcomingGaugesPerDenom(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.incentives.Query/UpcomingGaugesPerDenom', osmosis_dot_incentives_dot_query__pb2.UpcomingGaugesPerDenomRequest.SerializeToString, osmosis_dot_incentives_dot_query__pb2.UpcomingGaugesPerDenomResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RewardsEst(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.incentives.Query/RewardsEst', osmosis_dot_incentives_dot_query__pb2.RewardsEstRequest.SerializeToString, osmosis_dot_incentives_dot_query__pb2.RewardsEstResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LockableDurations(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.incentives.Query/LockableDurations', osmosis_dot_incentives_dot_query__pb2.QueryLockableDurationsRequest.SerializeToString, osmosis_dot_incentives_dot_query__pb2.QueryLockableDurationsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AllGroups(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.incentives.Query/AllGroups', osmosis_dot_incentives_dot_query__pb2.QueryAllGroupsRequest.SerializeToString, osmosis_dot_incentives_dot_query__pb2.QueryAllGroupsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AllGroupsGauges(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.incentives.Query/AllGroupsGauges', osmosis_dot_incentives_dot_query__pb2.QueryAllGroupsGaugesRequest.SerializeToString, osmosis_dot_incentives_dot_query__pb2.QueryAllGroupsGaugesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AllGroupsWithGauge(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.incentives.Query/AllGroupsWithGauge', osmosis_dot_incentives_dot_query__pb2.QueryAllGroupsWithGaugeRequest.SerializeToString, osmosis_dot_incentives_dot_query__pb2.QueryAllGroupsWithGaugeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GroupByGroupGaugeID(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.incentives.Query/GroupByGroupGaugeID', osmosis_dot_incentives_dot_query__pb2.QueryGroupByGroupGaugeIDRequest.SerializeToString, osmosis_dot_incentives_dot_query__pb2.QueryGroupByGroupGaugeIDResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CurrentWeightByGroupGaugeID(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/osmosis.incentives.Query/CurrentWeightByGroupGaugeID', osmosis_dot_incentives_dot_query__pb2.QueryCurrentWeightByGroupGaugeIDRequest.SerializeToString, osmosis_dot_incentives_dot_query__pb2.QueryCurrentWeightByGroupGaugeIDResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....cosmos.bank.v1beta1 import query_pb2 as cosmos_dot_bank_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Balance = channel.unary_unary('/cosmos.bank.v1beta1.Query/Balance', request_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryBalanceRequest.SerializeToString, response_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryBalanceResponse.FromString)
        self.AllBalances = channel.unary_unary('/cosmos.bank.v1beta1.Query/AllBalances', request_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryAllBalancesRequest.SerializeToString, response_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryAllBalancesResponse.FromString)
        self.SpendableBalances = channel.unary_unary('/cosmos.bank.v1beta1.Query/SpendableBalances', request_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySpendableBalancesRequest.SerializeToString, response_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySpendableBalancesResponse.FromString)
        self.SpendableBalanceByDenom = channel.unary_unary('/cosmos.bank.v1beta1.Query/SpendableBalanceByDenom', request_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySpendableBalanceByDenomRequest.SerializeToString, response_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySpendableBalanceByDenomResponse.FromString)
        self.TotalSupply = channel.unary_unary('/cosmos.bank.v1beta1.Query/TotalSupply', request_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryTotalSupplyRequest.SerializeToString, response_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryTotalSupplyResponse.FromString)
        self.SupplyOf = channel.unary_unary('/cosmos.bank.v1beta1.Query/SupplyOf', request_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySupplyOfRequest.SerializeToString, response_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySupplyOfResponse.FromString)
        self.TotalSupplyWithoutOffset = channel.unary_unary('/cosmos.bank.v1beta1.Query/TotalSupplyWithoutOffset', request_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryTotalSupplyWithoutOffsetRequest.SerializeToString, response_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryTotalSupplyWithoutOffsetResponse.FromString)
        self.SupplyOfWithoutOffset = channel.unary_unary('/cosmos.bank.v1beta1.Query/SupplyOfWithoutOffset', request_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySupplyOfWithoutOffsetRequest.SerializeToString, response_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySupplyOfWithoutOffsetResponse.FromString)
        self.Params = channel.unary_unary('/cosmos.bank.v1beta1.Query/Params', request_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, response_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString)
        self.DenomMetadata = channel.unary_unary('/cosmos.bank.v1beta1.Query/DenomMetadata', request_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryDenomMetadataRequest.SerializeToString, response_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryDenomMetadataResponse.FromString)
        self.DenomsMetadata = channel.unary_unary('/cosmos.bank.v1beta1.Query/DenomsMetadata', request_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryDenomsMetadataRequest.SerializeToString, response_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryDenomsMetadataResponse.FromString)
        self.DenomOwners = channel.unary_unary('/cosmos.bank.v1beta1.Query/DenomOwners', request_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryDenomOwnersRequest.SerializeToString, response_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryDenomOwnersResponse.FromString)
        self.SendEnabled = channel.unary_unary('/cosmos.bank.v1beta1.Query/SendEnabled', request_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySendEnabledRequest.SerializeToString, response_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySendEnabledResponse.FromString)

class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def Balance(self, request, context):
        """Balance queries the balance of a single coin for a single account.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AllBalances(self, request, context):
        """AllBalances queries the balance of all coins for a single account.

        When called from another module, this query might consume a high amount of
        gas if the pagination field is incorrectly set.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SpendableBalances(self, request, context):
        """SpendableBalances queries the spendable balance of all coins for a single
        account.

        When called from another module, this query might consume a high amount of
        gas if the pagination field is incorrectly set.

        Since: cosmos-sdk 0.46
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SpendableBalanceByDenom(self, request, context):
        """SpendableBalanceByDenom queries the spendable balance of a single denom for
        a single account.

        When called from another module, this query might consume a high amount of
        gas if the pagination field is incorrectly set.

        Since: cosmos-sdk 0.47
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TotalSupply(self, request, context):
        """TotalSupply queries the total supply of all coins.

        When called from another module, this query might consume a high amount of
        gas if the pagination field is incorrectly set.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SupplyOf(self, request, context):
        """SupplyOf queries the supply of a single coin.

        When called from another module, this query might consume a high amount of
        gas if the pagination field is incorrectly set.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TotalSupplyWithoutOffset(self, request, context):
        """TotalSupplyWithoutOffset queries the total supply of all coins.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SupplyOfWithoutOffset(self, request, context):
        """SupplyOf queries the supply of a single coin.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Params(self, request, context):
        """Params queries the parameters of x/bank module.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DenomMetadata(self, request, context):
        """DenomsMetadata queries the client metadata of a given coin denomination.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DenomsMetadata(self, request, context):
        """DenomsMetadata queries the client metadata for all registered coin
        denominations.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DenomOwners(self, request, context):
        """DenomOwners queries for all account addresses that own a particular token
        denomination.

        When called from another module, this query might consume a high amount of
        gas if the pagination field is incorrectly set.

        Since: cosmos-sdk 0.46
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendEnabled(self, request, context):
        """SendEnabled queries for SendEnabled entries.

        This query only returns denominations that have specific SendEnabled settings.
        Any denomination that does not have a specific setting will use the default
        params.default_send_enabled, and will not be returned by this query.

        Since: cosmos-sdk 0.47
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Balance': grpc.unary_unary_rpc_method_handler(servicer.Balance, request_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryBalanceRequest.FromString, response_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryBalanceResponse.SerializeToString), 'AllBalances': grpc.unary_unary_rpc_method_handler(servicer.AllBalances, request_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryAllBalancesRequest.FromString, response_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryAllBalancesResponse.SerializeToString), 'SpendableBalances': grpc.unary_unary_rpc_method_handler(servicer.SpendableBalances, request_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySpendableBalancesRequest.FromString, response_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySpendableBalancesResponse.SerializeToString), 'SpendableBalanceByDenom': grpc.unary_unary_rpc_method_handler(servicer.SpendableBalanceByDenom, request_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySpendableBalanceByDenomRequest.FromString, response_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySpendableBalanceByDenomResponse.SerializeToString), 'TotalSupply': grpc.unary_unary_rpc_method_handler(servicer.TotalSupply, request_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryTotalSupplyRequest.FromString, response_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryTotalSupplyResponse.SerializeToString), 'SupplyOf': grpc.unary_unary_rpc_method_handler(servicer.SupplyOf, request_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySupplyOfRequest.FromString, response_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySupplyOfResponse.SerializeToString), 'TotalSupplyWithoutOffset': grpc.unary_unary_rpc_method_handler(servicer.TotalSupplyWithoutOffset, request_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryTotalSupplyWithoutOffsetRequest.FromString, response_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryTotalSupplyWithoutOffsetResponse.SerializeToString), 'SupplyOfWithoutOffset': grpc.unary_unary_rpc_method_handler(servicer.SupplyOfWithoutOffset, request_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySupplyOfWithoutOffsetRequest.FromString, response_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySupplyOfWithoutOffsetResponse.SerializeToString), 'Params': grpc.unary_unary_rpc_method_handler(servicer.Params, request_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryParamsRequest.FromString, response_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryParamsResponse.SerializeToString), 'DenomMetadata': grpc.unary_unary_rpc_method_handler(servicer.DenomMetadata, request_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryDenomMetadataRequest.FromString, response_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryDenomMetadataResponse.SerializeToString), 'DenomsMetadata': grpc.unary_unary_rpc_method_handler(servicer.DenomsMetadata, request_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryDenomsMetadataRequest.FromString, response_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryDenomsMetadataResponse.SerializeToString), 'DenomOwners': grpc.unary_unary_rpc_method_handler(servicer.DenomOwners, request_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryDenomOwnersRequest.FromString, response_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryDenomOwnersResponse.SerializeToString), 'SendEnabled': grpc.unary_unary_rpc_method_handler(servicer.SendEnabled, request_deserializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySendEnabledRequest.FromString, response_serializer=cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySendEnabledResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('cosmos.bank.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def Balance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.bank.v1beta1.Query/Balance', cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryBalanceRequest.SerializeToString, cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryBalanceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AllBalances(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.bank.v1beta1.Query/AllBalances', cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryAllBalancesRequest.SerializeToString, cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryAllBalancesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SpendableBalances(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.bank.v1beta1.Query/SpendableBalances', cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySpendableBalancesRequest.SerializeToString, cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySpendableBalancesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SpendableBalanceByDenom(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.bank.v1beta1.Query/SpendableBalanceByDenom', cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySpendableBalanceByDenomRequest.SerializeToString, cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySpendableBalanceByDenomResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TotalSupply(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.bank.v1beta1.Query/TotalSupply', cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryTotalSupplyRequest.SerializeToString, cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryTotalSupplyResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SupplyOf(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.bank.v1beta1.Query/SupplyOf', cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySupplyOfRequest.SerializeToString, cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySupplyOfResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TotalSupplyWithoutOffset(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.bank.v1beta1.Query/TotalSupplyWithoutOffset', cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryTotalSupplyWithoutOffsetRequest.SerializeToString, cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryTotalSupplyWithoutOffsetResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SupplyOfWithoutOffset(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.bank.v1beta1.Query/SupplyOfWithoutOffset', cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySupplyOfWithoutOffsetRequest.SerializeToString, cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySupplyOfWithoutOffsetResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Params(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.bank.v1beta1.Query/Params', cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryParamsRequest.SerializeToString, cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DenomMetadata(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.bank.v1beta1.Query/DenomMetadata', cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryDenomMetadataRequest.SerializeToString, cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryDenomMetadataResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DenomsMetadata(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.bank.v1beta1.Query/DenomsMetadata', cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryDenomsMetadataRequest.SerializeToString, cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryDenomsMetadataResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DenomOwners(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.bank.v1beta1.Query/DenomOwners', cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryDenomOwnersRequest.SerializeToString, cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QueryDenomOwnersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendEnabled(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.bank.v1beta1.Query/SendEnabled', cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySendEnabledRequest.SerializeToString, cosmos_dot_bank_dot_v1beta1_dot_query__pb2.QuerySendEnabledResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
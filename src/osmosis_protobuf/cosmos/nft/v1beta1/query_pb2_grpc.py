"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from ....cosmos.nft.v1beta1 import query_pb2 as cosmos_dot_nft_dot_v1beta1_dot_query__pb2

class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Balance = channel.unary_unary('/cosmos.nft.v1beta1.Query/Balance', request_serializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryBalanceRequest.SerializeToString, response_deserializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryBalanceResponse.FromString)
        self.Owner = channel.unary_unary('/cosmos.nft.v1beta1.Query/Owner', request_serializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryOwnerRequest.SerializeToString, response_deserializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryOwnerResponse.FromString)
        self.Supply = channel.unary_unary('/cosmos.nft.v1beta1.Query/Supply', request_serializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QuerySupplyRequest.SerializeToString, response_deserializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QuerySupplyResponse.FromString)
        self.NFTs = channel.unary_unary('/cosmos.nft.v1beta1.Query/NFTs', request_serializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryNFTsRequest.SerializeToString, response_deserializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryNFTsResponse.FromString)
        self.NFT = channel.unary_unary('/cosmos.nft.v1beta1.Query/NFT', request_serializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryNFTRequest.SerializeToString, response_deserializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryNFTResponse.FromString)
        self.Class = channel.unary_unary('/cosmos.nft.v1beta1.Query/Class', request_serializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryClassRequest.SerializeToString, response_deserializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryClassResponse.FromString)
        self.Classes = channel.unary_unary('/cosmos.nft.v1beta1.Query/Classes', request_serializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryClassesRequest.SerializeToString, response_deserializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryClassesResponse.FromString)

class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def Balance(self, request, context):
        """Balance queries the number of NFTs of a given class owned by the owner, same as balanceOf in ERC721
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Owner(self, request, context):
        """Owner queries the owner of the NFT based on its class and id, same as ownerOf in ERC721
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Supply(self, request, context):
        """Supply queries the number of NFTs from the given class, same as totalSupply of ERC721.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NFTs(self, request, context):
        """NFTs queries all NFTs of a given class or owner,choose at least one of the two, similar to tokenByIndex in
        ERC721Enumerable
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def NFT(self, request, context):
        """NFT queries an NFT based on its class and id.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Class(self, request, context):
        """Class queries an NFT class based on its id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Classes(self, request, context):
        """Classes queries all NFT classes
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {'Balance': grpc.unary_unary_rpc_method_handler(servicer.Balance, request_deserializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryBalanceRequest.FromString, response_serializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryBalanceResponse.SerializeToString), 'Owner': grpc.unary_unary_rpc_method_handler(servicer.Owner, request_deserializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryOwnerRequest.FromString, response_serializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryOwnerResponse.SerializeToString), 'Supply': grpc.unary_unary_rpc_method_handler(servicer.Supply, request_deserializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QuerySupplyRequest.FromString, response_serializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QuerySupplyResponse.SerializeToString), 'NFTs': grpc.unary_unary_rpc_method_handler(servicer.NFTs, request_deserializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryNFTsRequest.FromString, response_serializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryNFTsResponse.SerializeToString), 'NFT': grpc.unary_unary_rpc_method_handler(servicer.NFT, request_deserializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryNFTRequest.FromString, response_serializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryNFTResponse.SerializeToString), 'Class': grpc.unary_unary_rpc_method_handler(servicer.Class, request_deserializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryClassRequest.FromString, response_serializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryClassResponse.SerializeToString), 'Classes': grpc.unary_unary_rpc_method_handler(servicer.Classes, request_deserializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryClassesRequest.FromString, response_serializer=cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryClassesResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('cosmos.nft.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))

class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def Balance(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.nft.v1beta1.Query/Balance', cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryBalanceRequest.SerializeToString, cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryBalanceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Owner(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.nft.v1beta1.Query/Owner', cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryOwnerRequest.SerializeToString, cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryOwnerResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Supply(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.nft.v1beta1.Query/Supply', cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QuerySupplyRequest.SerializeToString, cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QuerySupplyResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NFTs(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.nft.v1beta1.Query/NFTs', cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryNFTsRequest.SerializeToString, cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryNFTsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def NFT(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.nft.v1beta1.Query/NFT', cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryNFTRequest.SerializeToString, cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryNFTResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Class(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.nft.v1beta1.Query/Class', cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryClassRequest.SerializeToString, cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryClassResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Classes(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.nft.v1beta1.Query/Classes', cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryClassesRequest.SerializeToString, cosmos_dot_nft_dot_v1beta1_dot_query__pb2.QueryClassesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
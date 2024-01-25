"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....osmosis.poolmanager.v1beta1 import genesis_pb2 as osmosis_dot_poolmanager_dot_v1beta1_dot_genesis__pb2
from ....osmosis.poolmanager.v1beta1 import tx_pb2 as osmosis_dot_poolmanager_dot_v1beta1_dot_tx__pb2
from ....osmosis.poolmanager.v1beta1 import swap_route_pb2 as osmosis_dot_poolmanager_dot_v1beta1_dot_swap__route__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'osmosis/poolmanager/v1beta1/query.proto\x12\x1bosmosis.poolmanager.v1beta1\x1a\x14gogoproto/gogo.proto\x1a)osmosis/poolmanager/v1beta1/genesis.proto\x1a$osmosis/poolmanager/v1beta1/tx.proto\x1a,osmosis/poolmanager/v1beta1/swap_route.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x0f\n\rParamsRequest"K\n\x0eParamsResponse\x129\n\x06params\x18\x01 \x01(\x0b2#.osmosis.poolmanager.v1beta1.ParamsB\x04\xc8\xde\x1f\x00"\xd5\x01\n EstimateSwapExactAmountInRequest\x12%\n\x07pool_id\x18\x02 \x01(\x04B\x14\x18\x01\xf2\xde\x1f\x0eyaml:"pool_id"\x12%\n\x08token_in\x18\x03 \x01(\tB\x13\xf2\xde\x1f\x0fyaml:"token_in"\x12U\n\x06routes\x18\x04 \x03(\x0b2..osmosis.poolmanager.v1beta1.SwapAmountInRouteB\x15\xc8\xde\x1f\x00\xf2\xde\x1f\ryaml:"routes"J\x04\x08\x01\x10\x02R\x06sender"\xf8\x01\n2EstimateSwapExactAmountInWithPrimitiveTypesRequest\x12%\n\x07pool_id\x18\x01 \x01(\x04B\x14\x18\x01\xf2\xde\x1f\x0eyaml:"pool_id"\x12%\n\x08token_in\x18\x02 \x01(\tB\x13\xf2\xde\x1f\x0fyaml:"token_in"\x121\n\x0eroutes_pool_id\x18\x03 \x03(\x04B\x19\xf2\xde\x1f\x15yaml:"routes_pool_id"\x12A\n\x16routes_token_out_denom\x18\x04 \x03(\tB!\xf2\xde\x1f\x1dyaml:"routes_token_out_denom""\xad\x01\n*EstimateSinglePoolSwapExactAmountInRequest\x12#\n\x07pool_id\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x12%\n\x08token_in\x18\x02 \x01(\tB\x13\xf2\xde\x1f\x0fyaml:"token_in"\x123\n\x0ftoken_out_denom\x18\x03 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:"token_out_denom""w\n!EstimateSwapExactAmountInResponse\x12R\n\x10token_out_amount\x18\x01 \x01(\tB8\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int\xf2\xde\x1f\x17yaml:"token_out_amount""\xd9\x01\n!EstimateSwapExactAmountOutRequest\x12%\n\x07pool_id\x18\x02 \x01(\x04B\x14\x18\x01\xf2\xde\x1f\x0eyaml:"pool_id"\x12V\n\x06routes\x18\x03 \x03(\x0b2/.osmosis.poolmanager.v1beta1.SwapAmountOutRouteB\x15\xc8\xde\x1f\x00\xf2\xde\x1f\ryaml:"routes"\x12\'\n\ttoken_out\x18\x04 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"token_out"J\x04\x08\x01\x10\x02R\x06sender"\xf9\x01\n3EstimateSwapExactAmountOutWithPrimitiveTypesRequest\x12%\n\x07pool_id\x18\x01 \x01(\x04B\x14\x18\x01\xf2\xde\x1f\x0eyaml:"pool_id"\x121\n\x0eroutes_pool_id\x18\x02 \x03(\x04B\x19\xf2\xde\x1f\x15yaml:"routes_pool_id"\x12?\n\x15routes_token_in_denom\x18\x03 \x03(\tB \xf2\xde\x1f\x1cyaml:"routes_token_in_denom"\x12\'\n\ttoken_out\x18\x04 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"token_out""\xae\x01\n+EstimateSinglePoolSwapExactAmountOutRequest\x12#\n\x07pool_id\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x121\n\x0etoken_in_denom\x18\x02 \x01(\tB\x19\xf2\xde\x1f\x15yaml:"token_in_denom"\x12\'\n\ttoken_out\x18\x03 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"token_out""v\n"EstimateSwapExactAmountOutResponse\x12P\n\x0ftoken_in_amount\x18\x01 \x01(\tB7\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int\xf2\xde\x1f\x16yaml:"token_in_amount""\x11\n\x0fNumPoolsRequest";\n\x10NumPoolsResponse\x12\'\n\tnum_pools\x18\x01 \x01(\x04B\x14\xf2\xde\x1f\x10yaml:"num_pools""2\n\x0bPoolRequest\x12#\n\x07pool_id\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id""=\n\x0cPoolResponse\x12-\n\x04pool\x18\x01 \x01(\x0b2\x14.google.protobuf.AnyB\t\xca\xb4-\x05PoolI"\x11\n\x0fAllPoolsRequest"B\n\x10AllPoolsResponse\x12.\n\x05pools\x18\x01 \x03(\x0b2\x14.google.protobuf.AnyB\t\xca\xb4-\x05PoolI":\n\x17ListPoolsByDenomRequest\x12\x1f\n\x05denom\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"denom""J\n\x18ListPoolsByDenomResponse\x12.\n\x05pools\x18\x01 \x03(\x0b2\x14.google.protobuf.AnyB\t\xca\xb4-\x05PoolI"\xa7\x01\n\x10SpotPriceRequest\x12#\n\x07pool_id\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x125\n\x10base_asset_denom\x18\x02 \x01(\tB\x1b\xf2\xde\x1f\x17yaml:"base_asset_denom"\x127\n\x11quote_asset_denom\x18\x03 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"quote_asset_denom"">\n\x11SpotPriceResponse\x12)\n\nspot_price\x18\x01 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"spot_price""@\n\x19TotalPoolLiquidityRequest\x12#\n\x07pool_id\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id""\x90\x01\n\x1aTotalPoolLiquidityResponse\x12r\n\tliquidity\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBD\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"liquidity"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"\x17\n\x15TotalLiquidityRequest"\x8c\x01\n\x16TotalLiquidityResponse\x12r\n\tliquidity\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBD\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"liquidity"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"@\n\x19TotalVolumeForPoolRequest\x12#\n\x07pool_id\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id""\x8a\x01\n\x1aTotalVolumeForPoolResponse\x12l\n\x06volume\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBA\xc8\xde\x1f\x00\xf2\xde\x1f\ryaml:"volume"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"f\n\x1aTradingPairTakerFeeRequest\x12#\n\x07denom_0\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"denom_0"\x12#\n\x07denom_1\x18\x02 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"denom_1""`\n\x1bTradingPairTakerFeeResponse\x12A\n\ttaker_fee\x18\x01 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec"\x96\x02\n&EstimateTradeBasedOnPriceImpactRequest\x122\n\tfrom_coin\x18\x01 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x12\x15\n\rto_coin_denom\x18\x02 \x01(\t\x12\x0f\n\x07pool_id\x18\x03 \x01(\x04\x12H\n\x10max_price_impact\x18\x04 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec\x12F\n\x0eexternal_price\x18\x05 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec"\x94\x01\n\'EstimateTradeBasedOnPriceImpactResponse\x123\n\ninput_coin\x18\x01 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x00\x124\n\x0boutput_coin\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x04\xc8\xde\x1f\x002\x8d\x1c\n\x05Query\x12\x8e\x01\n\x06Params\x12*.osmosis.poolmanager.v1beta1.ParamsRequest\x1a+.osmosis.poolmanager.v1beta1.ParamsResponse"+\x82\xd3\xe4\x93\x02%\x12#/osmosis/poolmanager/v1beta1/Params\x12\xe8\x01\n\x19EstimateSwapExactAmountIn\x12=.osmosis.poolmanager.v1beta1.EstimateSwapExactAmountInRequest\x1a>.osmosis.poolmanager.v1beta1.EstimateSwapExactAmountInResponse"L\x82\xd3\xe4\x93\x02F\x12D/osmosis/poolmanager/v1beta1/{pool_id}/estimate/swap_exact_amount_in\x12\xa1\x02\n+EstimateSwapExactAmountInWithPrimitiveTypes\x12O.osmosis.poolmanager.v1beta1.EstimateSwapExactAmountInWithPrimitiveTypesRequest\x1a>.osmosis.poolmanager.v1beta1.EstimateSwapExactAmountInResponse"a\x82\xd3\xe4\x93\x02[\x12Y/osmosis/poolmanager/v1beta1/{pool_id}/estimate/swap_exact_amount_in_with_primitive_types\x12\x88\x02\n#EstimateSinglePoolSwapExactAmountIn\x12G.osmosis.poolmanager.v1beta1.EstimateSinglePoolSwapExactAmountInRequest\x1a>.osmosis.poolmanager.v1beta1.EstimateSwapExactAmountInResponse"X\x82\xd3\xe4\x93\x02R\x12P/osmosis/poolmanager/v1beta1/{pool_id}/estimate/single_pool_swap_exact_amount_in\x12\xec\x01\n\x1aEstimateSwapExactAmountOut\x12>.osmosis.poolmanager.v1beta1.EstimateSwapExactAmountOutRequest\x1a?.osmosis.poolmanager.v1beta1.EstimateSwapExactAmountOutResponse"M\x82\xd3\xe4\x93\x02G\x12E/osmosis/poolmanager/v1beta1/{pool_id}/estimate/swap_exact_amount_out\x12\xa5\x02\n,EstimateSwapExactAmountOutWithPrimitiveTypes\x12P.osmosis.poolmanager.v1beta1.EstimateSwapExactAmountOutWithPrimitiveTypesRequest\x1a?.osmosis.poolmanager.v1beta1.EstimateSwapExactAmountOutResponse"b\x82\xd3\xe4\x93\x02\\\x12Z/osmosis/poolmanager/v1beta1/{pool_id}/estimate/swap_exact_amount_out_with_primitive_types\x12\x90\x02\n$EstimateSinglePoolSwapExactAmountOut\x12H.osmosis.poolmanager.v1beta1.EstimateSinglePoolSwapExactAmountOutRequest\x1a?.osmosis.poolmanager.v1beta1.EstimateSwapExactAmountOutResponse"]\x82\xd3\xe4\x93\x02W\x12U/osmosis/poolmanager/v1beta1/{pool_id}/estimate_out/single_pool_swap_exact_amount_out\x12\x97\x01\n\x08NumPools\x12,.osmosis.poolmanager.v1beta1.NumPoolsRequest\x1a-.osmosis.poolmanager.v1beta1.NumPoolsResponse".\x82\xd3\xe4\x93\x02(\x12&/osmosis/poolmanager/v1beta1/num_pools\x12\x91\x01\n\x04Pool\x12(.osmosis.poolmanager.v1beta1.PoolRequest\x1a).osmosis.poolmanager.v1beta1.PoolResponse"4\x82\xd3\xe4\x93\x02.\x12,/osmosis/poolmanager/v1beta1/pools/{pool_id}\x12\x97\x01\n\x08AllPools\x12,.osmosis.poolmanager.v1beta1.AllPoolsRequest\x1a-.osmosis.poolmanager.v1beta1.AllPoolsResponse".\x82\xd3\xe4\x93\x02(\x12&/osmosis/poolmanager/v1beta1/all-pools\x12\xb9\x01\n\x10ListPoolsByDenom\x124.osmosis.poolmanager.v1beta1.ListPoolsByDenomRequest\x1a5.osmosis.poolmanager.v1beta1.ListPoolsByDenomResponse"8\x82\xd3\xe4\x93\x022\x120/osmosis/poolmanager/v1beta1/list-pools-by-denom\x12\x9f\x01\n\tSpotPrice\x12-.osmosis.poolmanager.v1beta1.SpotPriceRequest\x1a..osmosis.poolmanager.v1beta1.SpotPriceResponse"3\x82\xd3\xe4\x93\x02-\x12+/osmosis/poolmanager/pools/{pool_id}/prices\x12\xd0\x01\n\x12TotalPoolLiquidity\x126.osmosis.poolmanager.v1beta1.TotalPoolLiquidityRequest\x1a7.osmosis.poolmanager.v1beta1.TotalPoolLiquidityResponse"I\x82\xd3\xe4\x93\x02C\x12A/osmosis/poolmanager/v1beta1/pools/{pool_id}/total_pool_liquidity\x12\xb5\x01\n\x0eTotalLiquidity\x122.osmosis.poolmanager.v1beta1.TotalLiquidityRequest\x1a3.osmosis.poolmanager.v1beta1.TotalLiquidityResponse":\x82\xd3\xe4\x93\x024\x122/osmosis/poolmanager/v1beta1/pools/total_liquidity\x12\xc8\x01\n\x12TotalVolumeForPool\x126.osmosis.poolmanager.v1beta1.TotalVolumeForPoolRequest\x1a7.osmosis.poolmanager.v1beta1.TotalVolumeForPoolResponse"A\x82\xd3\xe4\x93\x02;\x129/osmosis/poolmanager/v1beta1/pools/{pool_id}/total_volume\x12\xc4\x01\n\x13TradingPairTakerFee\x127.osmosis.poolmanager.v1beta1.TradingPairTakerFeeRequest\x1a8.osmosis.poolmanager.v1beta1.TradingPairTakerFeeResponse":\x82\xd3\xe4\x93\x024\x122/osmosis/poolmanager/v1beta1/trading_pair_takerfee\x12\xeb\x01\n\x1fEstimateTradeBasedOnPriceImpact\x12C.osmosis.poolmanager.v1beta1.EstimateTradeBasedOnPriceImpactRequest\x1aD.osmosis.poolmanager.v1beta1.EstimateTradeBasedOnPriceImpactResponse"=\x82\xd3\xe4\x93\x027\x125/osmosis/poolmanager/v1beta1/{pool_id}/estimate_tradeBEZCgithub.com/osmosis-labs/osmosis/v21/x/poolmanager/client/queryprotob\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.poolmanager.v1beta1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'ZCgithub.com/osmosis-labs/osmosis/v21/x/poolmanager/client/queryproto'
    _globals['_PARAMSRESPONSE'].fields_by_name['params']._options = None
    _globals['_PARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_ESTIMATESWAPEXACTAMOUNTINREQUEST'].fields_by_name['pool_id']._options = None
    _globals['_ESTIMATESWAPEXACTAMOUNTINREQUEST'].fields_by_name['pool_id']._serialized_options = b'\x18\x01\xf2\xde\x1f\x0eyaml:"pool_id"'
    _globals['_ESTIMATESWAPEXACTAMOUNTINREQUEST'].fields_by_name['token_in']._options = None
    _globals['_ESTIMATESWAPEXACTAMOUNTINREQUEST'].fields_by_name['token_in']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"token_in"'
    _globals['_ESTIMATESWAPEXACTAMOUNTINREQUEST'].fields_by_name['routes']._options = None
    _globals['_ESTIMATESWAPEXACTAMOUNTINREQUEST'].fields_by_name['routes']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\ryaml:"routes"'
    _globals['_ESTIMATESWAPEXACTAMOUNTINWITHPRIMITIVETYPESREQUEST'].fields_by_name['pool_id']._options = None
    _globals['_ESTIMATESWAPEXACTAMOUNTINWITHPRIMITIVETYPESREQUEST'].fields_by_name['pool_id']._serialized_options = b'\x18\x01\xf2\xde\x1f\x0eyaml:"pool_id"'
    _globals['_ESTIMATESWAPEXACTAMOUNTINWITHPRIMITIVETYPESREQUEST'].fields_by_name['token_in']._options = None
    _globals['_ESTIMATESWAPEXACTAMOUNTINWITHPRIMITIVETYPESREQUEST'].fields_by_name['token_in']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"token_in"'
    _globals['_ESTIMATESWAPEXACTAMOUNTINWITHPRIMITIVETYPESREQUEST'].fields_by_name['routes_pool_id']._options = None
    _globals['_ESTIMATESWAPEXACTAMOUNTINWITHPRIMITIVETYPESREQUEST'].fields_by_name['routes_pool_id']._serialized_options = b'\xf2\xde\x1f\x15yaml:"routes_pool_id"'
    _globals['_ESTIMATESWAPEXACTAMOUNTINWITHPRIMITIVETYPESREQUEST'].fields_by_name['routes_token_out_denom']._options = None
    _globals['_ESTIMATESWAPEXACTAMOUNTINWITHPRIMITIVETYPESREQUEST'].fields_by_name['routes_token_out_denom']._serialized_options = b'\xf2\xde\x1f\x1dyaml:"routes_token_out_denom"'
    _globals['_ESTIMATESINGLEPOOLSWAPEXACTAMOUNTINREQUEST'].fields_by_name['pool_id']._options = None
    _globals['_ESTIMATESINGLEPOOLSWAPEXACTAMOUNTINREQUEST'].fields_by_name['pool_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _globals['_ESTIMATESINGLEPOOLSWAPEXACTAMOUNTINREQUEST'].fields_by_name['token_in']._options = None
    _globals['_ESTIMATESINGLEPOOLSWAPEXACTAMOUNTINREQUEST'].fields_by_name['token_in']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"token_in"'
    _globals['_ESTIMATESINGLEPOOLSWAPEXACTAMOUNTINREQUEST'].fields_by_name['token_out_denom']._options = None
    _globals['_ESTIMATESINGLEPOOLSWAPEXACTAMOUNTINREQUEST'].fields_by_name['token_out_denom']._serialized_options = b'\xf2\xde\x1f\x16yaml:"token_out_denom"'
    _globals['_ESTIMATESWAPEXACTAMOUNTINRESPONSE'].fields_by_name['token_out_amount']._options = None
    _globals['_ESTIMATESWAPEXACTAMOUNTINRESPONSE'].fields_by_name['token_out_amount']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int\xf2\xde\x1f\x17yaml:"token_out_amount"'
    _globals['_ESTIMATESWAPEXACTAMOUNTOUTREQUEST'].fields_by_name['pool_id']._options = None
    _globals['_ESTIMATESWAPEXACTAMOUNTOUTREQUEST'].fields_by_name['pool_id']._serialized_options = b'\x18\x01\xf2\xde\x1f\x0eyaml:"pool_id"'
    _globals['_ESTIMATESWAPEXACTAMOUNTOUTREQUEST'].fields_by_name['routes']._options = None
    _globals['_ESTIMATESWAPEXACTAMOUNTOUTREQUEST'].fields_by_name['routes']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\ryaml:"routes"'
    _globals['_ESTIMATESWAPEXACTAMOUNTOUTREQUEST'].fields_by_name['token_out']._options = None
    _globals['_ESTIMATESWAPEXACTAMOUNTOUTREQUEST'].fields_by_name['token_out']._serialized_options = b'\xf2\xde\x1f\x10yaml:"token_out"'
    _globals['_ESTIMATESWAPEXACTAMOUNTOUTWITHPRIMITIVETYPESREQUEST'].fields_by_name['pool_id']._options = None
    _globals['_ESTIMATESWAPEXACTAMOUNTOUTWITHPRIMITIVETYPESREQUEST'].fields_by_name['pool_id']._serialized_options = b'\x18\x01\xf2\xde\x1f\x0eyaml:"pool_id"'
    _globals['_ESTIMATESWAPEXACTAMOUNTOUTWITHPRIMITIVETYPESREQUEST'].fields_by_name['routes_pool_id']._options = None
    _globals['_ESTIMATESWAPEXACTAMOUNTOUTWITHPRIMITIVETYPESREQUEST'].fields_by_name['routes_pool_id']._serialized_options = b'\xf2\xde\x1f\x15yaml:"routes_pool_id"'
    _globals['_ESTIMATESWAPEXACTAMOUNTOUTWITHPRIMITIVETYPESREQUEST'].fields_by_name['routes_token_in_denom']._options = None
    _globals['_ESTIMATESWAPEXACTAMOUNTOUTWITHPRIMITIVETYPESREQUEST'].fields_by_name['routes_token_in_denom']._serialized_options = b'\xf2\xde\x1f\x1cyaml:"routes_token_in_denom"'
    _globals['_ESTIMATESWAPEXACTAMOUNTOUTWITHPRIMITIVETYPESREQUEST'].fields_by_name['token_out']._options = None
    _globals['_ESTIMATESWAPEXACTAMOUNTOUTWITHPRIMITIVETYPESREQUEST'].fields_by_name['token_out']._serialized_options = b'\xf2\xde\x1f\x10yaml:"token_out"'
    _globals['_ESTIMATESINGLEPOOLSWAPEXACTAMOUNTOUTREQUEST'].fields_by_name['pool_id']._options = None
    _globals['_ESTIMATESINGLEPOOLSWAPEXACTAMOUNTOUTREQUEST'].fields_by_name['pool_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _globals['_ESTIMATESINGLEPOOLSWAPEXACTAMOUNTOUTREQUEST'].fields_by_name['token_in_denom']._options = None
    _globals['_ESTIMATESINGLEPOOLSWAPEXACTAMOUNTOUTREQUEST'].fields_by_name['token_in_denom']._serialized_options = b'\xf2\xde\x1f\x15yaml:"token_in_denom"'
    _globals['_ESTIMATESINGLEPOOLSWAPEXACTAMOUNTOUTREQUEST'].fields_by_name['token_out']._options = None
    _globals['_ESTIMATESINGLEPOOLSWAPEXACTAMOUNTOUTREQUEST'].fields_by_name['token_out']._serialized_options = b'\xf2\xde\x1f\x10yaml:"token_out"'
    _globals['_ESTIMATESWAPEXACTAMOUNTOUTRESPONSE'].fields_by_name['token_in_amount']._options = None
    _globals['_ESTIMATESWAPEXACTAMOUNTOUTRESPONSE'].fields_by_name['token_in_amount']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int\xf2\xde\x1f\x16yaml:"token_in_amount"'
    _globals['_NUMPOOLSRESPONSE'].fields_by_name['num_pools']._options = None
    _globals['_NUMPOOLSRESPONSE'].fields_by_name['num_pools']._serialized_options = b'\xf2\xde\x1f\x10yaml:"num_pools"'
    _globals['_POOLREQUEST'].fields_by_name['pool_id']._options = None
    _globals['_POOLREQUEST'].fields_by_name['pool_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _globals['_POOLRESPONSE'].fields_by_name['pool']._options = None
    _globals['_POOLRESPONSE'].fields_by_name['pool']._serialized_options = b'\xca\xb4-\x05PoolI'
    _globals['_ALLPOOLSRESPONSE'].fields_by_name['pools']._options = None
    _globals['_ALLPOOLSRESPONSE'].fields_by_name['pools']._serialized_options = b'\xca\xb4-\x05PoolI'
    _globals['_LISTPOOLSBYDENOMREQUEST'].fields_by_name['denom']._options = None
    _globals['_LISTPOOLSBYDENOMREQUEST'].fields_by_name['denom']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"denom"'
    _globals['_LISTPOOLSBYDENOMRESPONSE'].fields_by_name['pools']._options = None
    _globals['_LISTPOOLSBYDENOMRESPONSE'].fields_by_name['pools']._serialized_options = b'\xca\xb4-\x05PoolI'
    _globals['_SPOTPRICEREQUEST'].fields_by_name['pool_id']._options = None
    _globals['_SPOTPRICEREQUEST'].fields_by_name['pool_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _globals['_SPOTPRICEREQUEST'].fields_by_name['base_asset_denom']._options = None
    _globals['_SPOTPRICEREQUEST'].fields_by_name['base_asset_denom']._serialized_options = b'\xf2\xde\x1f\x17yaml:"base_asset_denom"'
    _globals['_SPOTPRICEREQUEST'].fields_by_name['quote_asset_denom']._options = None
    _globals['_SPOTPRICEREQUEST'].fields_by_name['quote_asset_denom']._serialized_options = b'\xf2\xde\x1f\x18yaml:"quote_asset_denom"'
    _globals['_SPOTPRICERESPONSE'].fields_by_name['spot_price']._options = None
    _globals['_SPOTPRICERESPONSE'].fields_by_name['spot_price']._serialized_options = b'\xf2\xde\x1f\x11yaml:"spot_price"'
    _globals['_TOTALPOOLLIQUIDITYREQUEST'].fields_by_name['pool_id']._options = None
    _globals['_TOTALPOOLLIQUIDITYREQUEST'].fields_by_name['pool_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _globals['_TOTALPOOLLIQUIDITYRESPONSE'].fields_by_name['liquidity']._options = None
    _globals['_TOTALPOOLLIQUIDITYRESPONSE'].fields_by_name['liquidity']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"liquidity"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_TOTALLIQUIDITYRESPONSE'].fields_by_name['liquidity']._options = None
    _globals['_TOTALLIQUIDITYRESPONSE'].fields_by_name['liquidity']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"liquidity"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_TOTALVOLUMEFORPOOLREQUEST'].fields_by_name['pool_id']._options = None
    _globals['_TOTALVOLUMEFORPOOLREQUEST'].fields_by_name['pool_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _globals['_TOTALVOLUMEFORPOOLRESPONSE'].fields_by_name['volume']._options = None
    _globals['_TOTALVOLUMEFORPOOLRESPONSE'].fields_by_name['volume']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\ryaml:"volume"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_TRADINGPAIRTAKERFEEREQUEST'].fields_by_name['denom_0']._options = None
    _globals['_TRADINGPAIRTAKERFEEREQUEST'].fields_by_name['denom_0']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"denom_0"'
    _globals['_TRADINGPAIRTAKERFEEREQUEST'].fields_by_name['denom_1']._options = None
    _globals['_TRADINGPAIRTAKERFEEREQUEST'].fields_by_name['denom_1']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"denom_1"'
    _globals['_TRADINGPAIRTAKERFEERESPONSE'].fields_by_name['taker_fee']._options = None
    _globals['_TRADINGPAIRTAKERFEERESPONSE'].fields_by_name['taker_fee']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec'
    _globals['_ESTIMATETRADEBASEDONPRICEIMPACTREQUEST'].fields_by_name['from_coin']._options = None
    _globals['_ESTIMATETRADEBASEDONPRICEIMPACTREQUEST'].fields_by_name['from_coin']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_ESTIMATETRADEBASEDONPRICEIMPACTREQUEST'].fields_by_name['max_price_impact']._options = None
    _globals['_ESTIMATETRADEBASEDONPRICEIMPACTREQUEST'].fields_by_name['max_price_impact']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec'
    _globals['_ESTIMATETRADEBASEDONPRICEIMPACTREQUEST'].fields_by_name['external_price']._options = None
    _globals['_ESTIMATETRADEBASEDONPRICEIMPACTREQUEST'].fields_by_name['external_price']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Dec'
    _globals['_ESTIMATETRADEBASEDONPRICEIMPACTRESPONSE'].fields_by_name['input_coin']._options = None
    _globals['_ESTIMATETRADEBASEDONPRICEIMPACTRESPONSE'].fields_by_name['input_coin']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_ESTIMATETRADEBASEDONPRICEIMPACTRESPONSE'].fields_by_name['output_coin']._options = None
    _globals['_ESTIMATETRADEBASEDONPRICEIMPACTRESPONSE'].fields_by_name['output_coin']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERY'].methods_by_name['Params']._options = None
    _globals['_QUERY'].methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02%\x12#/osmosis/poolmanager/v1beta1/Params'
    _globals['_QUERY'].methods_by_name['EstimateSwapExactAmountIn']._options = None
    _globals['_QUERY'].methods_by_name['EstimateSwapExactAmountIn']._serialized_options = b'\x82\xd3\xe4\x93\x02F\x12D/osmosis/poolmanager/v1beta1/{pool_id}/estimate/swap_exact_amount_in'
    _globals['_QUERY'].methods_by_name['EstimateSwapExactAmountInWithPrimitiveTypes']._options = None
    _globals['_QUERY'].methods_by_name['EstimateSwapExactAmountInWithPrimitiveTypes']._serialized_options = b'\x82\xd3\xe4\x93\x02[\x12Y/osmosis/poolmanager/v1beta1/{pool_id}/estimate/swap_exact_amount_in_with_primitive_types'
    _globals['_QUERY'].methods_by_name['EstimateSinglePoolSwapExactAmountIn']._options = None
    _globals['_QUERY'].methods_by_name['EstimateSinglePoolSwapExactAmountIn']._serialized_options = b'\x82\xd3\xe4\x93\x02R\x12P/osmosis/poolmanager/v1beta1/{pool_id}/estimate/single_pool_swap_exact_amount_in'
    _globals['_QUERY'].methods_by_name['EstimateSwapExactAmountOut']._options = None
    _globals['_QUERY'].methods_by_name['EstimateSwapExactAmountOut']._serialized_options = b'\x82\xd3\xe4\x93\x02G\x12E/osmosis/poolmanager/v1beta1/{pool_id}/estimate/swap_exact_amount_out'
    _globals['_QUERY'].methods_by_name['EstimateSwapExactAmountOutWithPrimitiveTypes']._options = None
    _globals['_QUERY'].methods_by_name['EstimateSwapExactAmountOutWithPrimitiveTypes']._serialized_options = b'\x82\xd3\xe4\x93\x02\\\x12Z/osmosis/poolmanager/v1beta1/{pool_id}/estimate/swap_exact_amount_out_with_primitive_types'
    _globals['_QUERY'].methods_by_name['EstimateSinglePoolSwapExactAmountOut']._options = None
    _globals['_QUERY'].methods_by_name['EstimateSinglePoolSwapExactAmountOut']._serialized_options = b'\x82\xd3\xe4\x93\x02W\x12U/osmosis/poolmanager/v1beta1/{pool_id}/estimate_out/single_pool_swap_exact_amount_out'
    _globals['_QUERY'].methods_by_name['NumPools']._options = None
    _globals['_QUERY'].methods_by_name['NumPools']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/osmosis/poolmanager/v1beta1/num_pools'
    _globals['_QUERY'].methods_by_name['Pool']._options = None
    _globals['_QUERY'].methods_by_name['Pool']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/osmosis/poolmanager/v1beta1/pools/{pool_id}'
    _globals['_QUERY'].methods_by_name['AllPools']._options = None
    _globals['_QUERY'].methods_by_name['AllPools']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/osmosis/poolmanager/v1beta1/all-pools'
    _globals['_QUERY'].methods_by_name['ListPoolsByDenom']._options = None
    _globals['_QUERY'].methods_by_name['ListPoolsByDenom']._serialized_options = b'\x82\xd3\xe4\x93\x022\x120/osmosis/poolmanager/v1beta1/list-pools-by-denom'
    _globals['_QUERY'].methods_by_name['SpotPrice']._options = None
    _globals['_QUERY'].methods_by_name['SpotPrice']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/osmosis/poolmanager/pools/{pool_id}/prices'
    _globals['_QUERY'].methods_by_name['TotalPoolLiquidity']._options = None
    _globals['_QUERY'].methods_by_name['TotalPoolLiquidity']._serialized_options = b'\x82\xd3\xe4\x93\x02C\x12A/osmosis/poolmanager/v1beta1/pools/{pool_id}/total_pool_liquidity'
    _globals['_QUERY'].methods_by_name['TotalLiquidity']._options = None
    _globals['_QUERY'].methods_by_name['TotalLiquidity']._serialized_options = b'\x82\xd3\xe4\x93\x024\x122/osmosis/poolmanager/v1beta1/pools/total_liquidity'
    _globals['_QUERY'].methods_by_name['TotalVolumeForPool']._options = None
    _globals['_QUERY'].methods_by_name['TotalVolumeForPool']._serialized_options = b'\x82\xd3\xe4\x93\x02;\x129/osmosis/poolmanager/v1beta1/pools/{pool_id}/total_volume'
    _globals['_QUERY'].methods_by_name['TradingPairTakerFee']._options = None
    _globals['_QUERY'].methods_by_name['TradingPairTakerFee']._serialized_options = b'\x82\xd3\xe4\x93\x024\x122/osmosis/poolmanager/v1beta1/trading_pair_takerfee'
    _globals['_QUERY'].methods_by_name['EstimateTradeBasedOnPriceImpact']._options = None
    _globals['_QUERY'].methods_by_name['EstimateTradeBasedOnPriceImpact']._serialized_options = b'\x82\xd3\xe4\x93\x027\x125/osmosis/poolmanager/v1beta1/{pool_id}/estimate_trade'
    _globals['_PARAMSREQUEST']._serialized_start = 414
    _globals['_PARAMSREQUEST']._serialized_end = 429
    _globals['_PARAMSRESPONSE']._serialized_start = 431
    _globals['_PARAMSRESPONSE']._serialized_end = 506
    _globals['_ESTIMATESWAPEXACTAMOUNTINREQUEST']._serialized_start = 509
    _globals['_ESTIMATESWAPEXACTAMOUNTINREQUEST']._serialized_end = 722
    _globals['_ESTIMATESWAPEXACTAMOUNTINWITHPRIMITIVETYPESREQUEST']._serialized_start = 725
    _globals['_ESTIMATESWAPEXACTAMOUNTINWITHPRIMITIVETYPESREQUEST']._serialized_end = 973
    _globals['_ESTIMATESINGLEPOOLSWAPEXACTAMOUNTINREQUEST']._serialized_start = 976
    _globals['_ESTIMATESINGLEPOOLSWAPEXACTAMOUNTINREQUEST']._serialized_end = 1149
    _globals['_ESTIMATESWAPEXACTAMOUNTINRESPONSE']._serialized_start = 1151
    _globals['_ESTIMATESWAPEXACTAMOUNTINRESPONSE']._serialized_end = 1270
    _globals['_ESTIMATESWAPEXACTAMOUNTOUTREQUEST']._serialized_start = 1273
    _globals['_ESTIMATESWAPEXACTAMOUNTOUTREQUEST']._serialized_end = 1490
    _globals['_ESTIMATESWAPEXACTAMOUNTOUTWITHPRIMITIVETYPESREQUEST']._serialized_start = 1493
    _globals['_ESTIMATESWAPEXACTAMOUNTOUTWITHPRIMITIVETYPESREQUEST']._serialized_end = 1742
    _globals['_ESTIMATESINGLEPOOLSWAPEXACTAMOUNTOUTREQUEST']._serialized_start = 1745
    _globals['_ESTIMATESINGLEPOOLSWAPEXACTAMOUNTOUTREQUEST']._serialized_end = 1919
    _globals['_ESTIMATESWAPEXACTAMOUNTOUTRESPONSE']._serialized_start = 1921
    _globals['_ESTIMATESWAPEXACTAMOUNTOUTRESPONSE']._serialized_end = 2039
    _globals['_NUMPOOLSREQUEST']._serialized_start = 2041
    _globals['_NUMPOOLSREQUEST']._serialized_end = 2058
    _globals['_NUMPOOLSRESPONSE']._serialized_start = 2060
    _globals['_NUMPOOLSRESPONSE']._serialized_end = 2119
    _globals['_POOLREQUEST']._serialized_start = 2121
    _globals['_POOLREQUEST']._serialized_end = 2171
    _globals['_POOLRESPONSE']._serialized_start = 2173
    _globals['_POOLRESPONSE']._serialized_end = 2234
    _globals['_ALLPOOLSREQUEST']._serialized_start = 2236
    _globals['_ALLPOOLSREQUEST']._serialized_end = 2253
    _globals['_ALLPOOLSRESPONSE']._serialized_start = 2255
    _globals['_ALLPOOLSRESPONSE']._serialized_end = 2321
    _globals['_LISTPOOLSBYDENOMREQUEST']._serialized_start = 2323
    _globals['_LISTPOOLSBYDENOMREQUEST']._serialized_end = 2381
    _globals['_LISTPOOLSBYDENOMRESPONSE']._serialized_start = 2383
    _globals['_LISTPOOLSBYDENOMRESPONSE']._serialized_end = 2457
    _globals['_SPOTPRICEREQUEST']._serialized_start = 2460
    _globals['_SPOTPRICEREQUEST']._serialized_end = 2627
    _globals['_SPOTPRICERESPONSE']._serialized_start = 2629
    _globals['_SPOTPRICERESPONSE']._serialized_end = 2691
    _globals['_TOTALPOOLLIQUIDITYREQUEST']._serialized_start = 2693
    _globals['_TOTALPOOLLIQUIDITYREQUEST']._serialized_end = 2757
    _globals['_TOTALPOOLLIQUIDITYRESPONSE']._serialized_start = 2760
    _globals['_TOTALPOOLLIQUIDITYRESPONSE']._serialized_end = 2904
    _globals['_TOTALLIQUIDITYREQUEST']._serialized_start = 2906
    _globals['_TOTALLIQUIDITYREQUEST']._serialized_end = 2929
    _globals['_TOTALLIQUIDITYRESPONSE']._serialized_start = 2932
    _globals['_TOTALLIQUIDITYRESPONSE']._serialized_end = 3072
    _globals['_TOTALVOLUMEFORPOOLREQUEST']._serialized_start = 3074
    _globals['_TOTALVOLUMEFORPOOLREQUEST']._serialized_end = 3138
    _globals['_TOTALVOLUMEFORPOOLRESPONSE']._serialized_start = 3141
    _globals['_TOTALVOLUMEFORPOOLRESPONSE']._serialized_end = 3279
    _globals['_TRADINGPAIRTAKERFEEREQUEST']._serialized_start = 3281
    _globals['_TRADINGPAIRTAKERFEEREQUEST']._serialized_end = 3383
    _globals['_TRADINGPAIRTAKERFEERESPONSE']._serialized_start = 3385
    _globals['_TRADINGPAIRTAKERFEERESPONSE']._serialized_end = 3481
    _globals['_ESTIMATETRADEBASEDONPRICEIMPACTREQUEST']._serialized_start = 3484
    _globals['_ESTIMATETRADEBASEDONPRICEIMPACTREQUEST']._serialized_end = 3762
    _globals['_ESTIMATETRADEBASEDONPRICEIMPACTRESPONSE']._serialized_start = 3765
    _globals['_ESTIMATETRADEBASEDONPRICEIMPACTRESPONSE']._serialized_end = 3913
    _globals['_QUERY']._serialized_start = 3916
    _globals['_QUERY']._serialized_end = 7513
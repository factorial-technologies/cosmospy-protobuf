"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ......cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ......gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ......amino import amino_pb2 as amino_dot_amino__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ......cosmos.auth.v1beta1 import auth_pb2 as cosmos_dot_auth_dot_v1beta1_dot_auth__pb2
from ......cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@osmosis/gamm/poolmodels/stableswap/v1beta1/stableswap_pool.proto\x12*osmosis.gamm.poolmodels.stableswap.v1beta1\x1a\x19cosmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x11amino/amino.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1ecosmos/auth/v1beta1/auth.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\xc8\x01\n\nPoolParams\x12H\n\x08swap_fee\x18\x01 \x01(\tB6\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xf2\xde\x1f\x0fyaml:"swap_fee"\x12H\n\x08exit_fee\x18\x02 \x01(\tB6\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xf2\xde\x1f\x0fyaml:"exit_fee":&\x8a\xe7\xb0*!osmosis/gamm/StableswapPoolParams"\xd9\x04\n\x04Pool\x12#\n\x07address\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12\n\n\x02id\x18\x02 \x01(\x04\x12r\n\x0bpool_params\x18\x03 \x01(\x0b26.osmosis.gamm.poolmodels.stableswap.v1beta1.PoolParamsB%\xc8\xde\x1f\x00\xf2\xde\x1f\x1dyaml:"stableswap_pool_params"\x12=\n\x14future_pool_governor\x18\x04 \x01(\tB\x1f\xf2\xde\x1f\x1byaml:"future_pool_governor"\x12L\n\x0ctotal_shares\x18\x05 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB\x1b\xc8\xde\x1f\x00\xf2\xde\x1f\x13yaml:"total_shares"\x12c\n\x0epool_liquidity\x18\x06 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12>\n\x0fscaling_factors\x18\x07 \x03(\x04B%\xf2\xde\x1f!yaml:"stableswap_scaling_factors"\x12G\n\x19scaling_factor_controller\x18\x08 \x01(\tB$\xf2\xde\x1f yaml:"scaling_factor_controller":1\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xca\xb4-\x05PoolI\x8a\xe7\xb0*\x1bosmosis/gamm/StableswapPoolBCZAgithub.com/osmosis-labs/osmosis/v21/x/gamm/pool-models/stableswapb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.gamm.poolmodels.stableswap.v1beta1.stableswap_pool_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'ZAgithub.com/osmosis-labs/osmosis/v21/x/gamm/pool-models/stableswap'
    _globals['_POOLPARAMS'].fields_by_name['swap_fee']._options = None
    _globals['_POOLPARAMS'].fields_by_name['swap_fee']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xf2\xde\x1f\x0fyaml:"swap_fee"'
    _globals['_POOLPARAMS'].fields_by_name['exit_fee']._options = None
    _globals['_POOLPARAMS'].fields_by_name['exit_fee']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xf2\xde\x1f\x0fyaml:"exit_fee"'
    _globals['_POOLPARAMS']._options = None
    _globals['_POOLPARAMS']._serialized_options = b'\x8a\xe7\xb0*!osmosis/gamm/StableswapPoolParams'
    _globals['_POOL'].fields_by_name['address']._options = None
    _globals['_POOL'].fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _globals['_POOL'].fields_by_name['pool_params']._options = None
    _globals['_POOL'].fields_by_name['pool_params']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x1dyaml:"stableswap_pool_params"'
    _globals['_POOL'].fields_by_name['future_pool_governor']._options = None
    _globals['_POOL'].fields_by_name['future_pool_governor']._serialized_options = b'\xf2\xde\x1f\x1byaml:"future_pool_governor"'
    _globals['_POOL'].fields_by_name['total_shares']._options = None
    _globals['_POOL'].fields_by_name['total_shares']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x13yaml:"total_shares"'
    _globals['_POOL'].fields_by_name['pool_liquidity']._options = None
    _globals['_POOL'].fields_by_name['pool_liquidity']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_POOL'].fields_by_name['scaling_factors']._options = None
    _globals['_POOL'].fields_by_name['scaling_factors']._serialized_options = b'\xf2\xde\x1f!yaml:"stableswap_scaling_factors"'
    _globals['_POOL'].fields_by_name['scaling_factor_controller']._options = None
    _globals['_POOL'].fields_by_name['scaling_factor_controller']._serialized_options = b'\xf2\xde\x1f yaml:"scaling_factor_controller"'
    _globals['_POOL']._options = None
    _globals['_POOL']._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xca\xb4-\x05PoolI\x8a\xe7\xb0*\x1bosmosis/gamm/StableswapPool'
    _globals['_POOLPARAMS']._serialized_start = 310
    _globals['_POOLPARAMS']._serialized_end = 510
    _globals['_POOL']._serialized_start = 513
    _globals['_POOL']._serialized_end = 1114
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4osmosis/concentratedliquidity/v1beta1/tickInfo.proto\x12%osmosis.concentratedliquidity.v1beta1\x1a\x19cosmos_proto/cosmos.proto\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\xbd\x03\n\x08TickInfo\x12V\n\x0fliquidity_gross\x18\x01 \x01(\tB=\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xf2\xde\x1f\x16yaml:"liquidity_gross"\x12R\n\rliquidity_net\x18\x02 \x01(\tB;\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xf2\xde\x1f\x14yaml:"liquidity_net"\x12\x94\x01\n9spread_reward_growth_opposite_direction_of_last_traversal\x18\x03 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins\x12n\n\x0fuptime_trackers\x18\x04 \x01(\x0b25.osmosis.concentratedliquidity.v1beta1.UptimeTrackersB\x1e\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:"uptime_trackers""i\n\x0eUptimeTrackers\x12W\n\x04list\x18\x01 \x03(\x0b24.osmosis.concentratedliquidity.v1beta1.UptimeTrackerB\x13\xc8\xde\x1f\x00\xf2\xde\x1f\x0byaml:"list""\x81\x01\n\rUptimeTracker\x12p\n\x15uptime_growth_outside\x18\x01 \x03(\x0b2\x1c.cosmos.base.v1beta1.DecCoinB3\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoinsBDZBgithub.com/osmosis-labs/osmosis/v21/x/concentrated-liquidity/modelb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.concentratedliquidity.v1beta1.tickInfo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'ZBgithub.com/osmosis-labs/osmosis/v21/x/concentrated-liquidity/model'
    _globals['_TICKINFO'].fields_by_name['liquidity_gross']._options = None
    _globals['_TICKINFO'].fields_by_name['liquidity_gross']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xf2\xde\x1f\x16yaml:"liquidity_gross"'
    _globals['_TICKINFO'].fields_by_name['liquidity_net']._options = None
    _globals['_TICKINFO'].fields_by_name['liquidity_net']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xf2\xde\x1f\x14yaml:"liquidity_net"'
    _globals['_TICKINFO'].fields_by_name['spread_reward_growth_opposite_direction_of_last_traversal']._options = None
    _globals['_TICKINFO'].fields_by_name['spread_reward_growth_opposite_direction_of_last_traversal']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _globals['_TICKINFO'].fields_by_name['uptime_trackers']._options = None
    _globals['_TICKINFO'].fields_by_name['uptime_trackers']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:"uptime_trackers"'
    _globals['_UPTIMETRACKERS'].fields_by_name['list']._options = None
    _globals['_UPTIMETRACKERS'].fields_by_name['list']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x0byaml:"list"'
    _globals['_UPTIMETRACKER'].fields_by_name['uptime_growth_outside']._options = None
    _globals['_UPTIMETRACKER'].fields_by_name['uptime_growth_outside']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f+github.com/cosmos/cosmos-sdk/types.DecCoins'
    _globals['_TICKINFO']._serialized_start = 177
    _globals['_TICKINFO']._serialized_end = 622
    _globals['_UPTIMETRACKERS']._serialized_start = 624
    _globals['_UPTIMETRACKERS']._serialized_end = 729
    _globals['_UPTIMETRACKER']._serialized_start = 732
    _globals['_UPTIMETRACKER']._serialized_end = 861
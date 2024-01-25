"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ...cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ...osmosis.lockup import lock_pb2 as osmosis_dot_lockup_dot_lock__pb2
from ...osmosis.incentives import gauge_pb2 as osmosis_dot_incentives_dot_gauge__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eosmosis/incentives/group.proto\x12\x12osmosis.incentives\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x19osmosis/lockup/lock.proto\x1a\x1eosmosis/incentives/gauge.proto"\xa5\x01\n\x11InternalGaugeInfo\x12J\n\x0ctotal_weight\x18\x01 \x01(\tB4\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int\xf2\xde\x1f\x13yaml:"total_weight"\x12D\n\rgauge_records\x18\x02 \x03(\x0b2\'.osmosis.incentives.InternalGaugeRecordB\x04\xc8\xde\x1f\x00"\xb3\x01\n\x13InternalGaugeRecord\x12%\n\x08gauge_id\x18\x01 \x01(\x04B\x13\xf2\xde\x1f\x0fyaml:"gauge_id"\x125\n\x0ecurrent_weight\x18\x02 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int\x128\n\x11cumulative_weight\x18\x03 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int:\x04\xe8\xa0\x1f\x01"\xa8\x01\n\x05Group\x12\x16\n\x0egroup_gauge_id\x18\x01 \x01(\x04\x12H\n\x13internal_gauge_info\x18\x02 \x01(\x0b2%.osmosis.incentives.InternalGaugeInfoB\x04\xc8\xde\x1f\x00\x12=\n\x10splitting_policy\x18\x03 \x01(\x0e2#.osmosis.incentives.SplittingPolicy"\x1f\n\x0bCreateGroup\x12\x10\n\x08pool_ids\x18\x01 \x03(\x04"q\n\x0fGroupsWithGauge\x12.\n\x05group\x18\x01 \x01(\x0b2\x19.osmosis.incentives.GroupB\x04\xc8\xde\x1f\x00\x12.\n\x05gauge\x18\x02 \x01(\x0b2\x19.osmosis.incentives.GaugeB\x04\xc8\xde\x1f\x00*%\n\x0fSplittingPolicy\x12\x0c\n\x08ByVolume\x10\x00\x1a\x04\x88\xa3\x1e\x00B8Z6github.com/osmosis-labs/osmosis/v21/x/incentives/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.incentives.group_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z6github.com/osmosis-labs/osmosis/v21/x/incentives/types'
    _globals['_SPLITTINGPOLICY']._options = None
    _globals['_SPLITTINGPOLICY']._serialized_options = b'\x88\xa3\x1e\x00'
    _globals['_INTERNALGAUGEINFO'].fields_by_name['total_weight']._options = None
    _globals['_INTERNALGAUGEINFO'].fields_by_name['total_weight']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int\xf2\xde\x1f\x13yaml:"total_weight"'
    _globals['_INTERNALGAUGEINFO'].fields_by_name['gauge_records']._options = None
    _globals['_INTERNALGAUGEINFO'].fields_by_name['gauge_records']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_INTERNALGAUGERECORD'].fields_by_name['gauge_id']._options = None
    _globals['_INTERNALGAUGERECORD'].fields_by_name['gauge_id']._serialized_options = b'\xf2\xde\x1f\x0fyaml:"gauge_id"'
    _globals['_INTERNALGAUGERECORD'].fields_by_name['current_weight']._options = None
    _globals['_INTERNALGAUGERECORD'].fields_by_name['current_weight']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int'
    _globals['_INTERNALGAUGERECORD'].fields_by_name['cumulative_weight']._options = None
    _globals['_INTERNALGAUGERECORD'].fields_by_name['cumulative_weight']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int'
    _globals['_INTERNALGAUGERECORD']._options = None
    _globals['_INTERNALGAUGERECORD']._serialized_options = b'\xe8\xa0\x1f\x01'
    _globals['_GROUP'].fields_by_name['internal_gauge_info']._options = None
    _globals['_GROUP'].fields_by_name['internal_gauge_info']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GROUPSWITHGAUGE'].fields_by_name['group']._options = None
    _globals['_GROUPSWITHGAUGE'].fields_by_name['group']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GROUPSWITHGAUGE'].fields_by_name['gauge']._options = None
    _globals['_GROUPSWITHGAUGE'].fields_by_name['gauge']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_SPLITTINGPOLICY']._serialized_start = 901
    _globals['_SPLITTINGPOLICY']._serialized_end = 938
    _globals['_INTERNALGAUGEINFO']._serialized_start = 233
    _globals['_INTERNALGAUGEINFO']._serialized_end = 398
    _globals['_INTERNALGAUGERECORD']._serialized_start = 401
    _globals['_INTERNALGAUGERECORD']._serialized_end = 580
    _globals['_GROUP']._serialized_start = 583
    _globals['_GROUP']._serialized_end = 751
    _globals['_CREATEGROUP']._serialized_start = 753
    _globals['_CREATEGROUP']._serialized_end = 784
    _globals['_GROUPSWITHGAUGE']._serialized_start = 786
    _globals['_GROUPSWITHGAUGE']._serialized_end = 899
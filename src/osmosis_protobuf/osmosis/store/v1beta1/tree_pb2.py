"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n osmosis/store/v1beta1/tree.proto\x12\x15osmosis.store.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"6\n\x04Node\x12.\n\x08children\x18\x01 \x03(\x0b2\x1c.osmosis.store.v1beta1.Child"K\n\x05Child\x12\r\n\x05index\x18\x01 \x01(\x0c\x123\n\x0caccumulation\x18\x02 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int"2\n\x04Leaf\x12*\n\x04leaf\x18\x01 \x01(\x0b2\x1c.osmosis.store.v1beta1.ChildB3Z1github.com/osmosis-labs/osmosis/osmoutils/sumtreeb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.store.v1beta1.tree_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z1github.com/osmosis-labs/osmosis/osmoutils/sumtree'
    _globals['_CHILD'].fields_by_name['accumulation']._options = None
    _globals['_CHILD'].fields_by_name['accumulation']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int'
    _globals['_NODE']._serialized_start = 113
    _globals['_NODE']._serialized_end = 167
    _globals['_CHILD']._serialized_start = 169
    _globals['_CHILD']._serialized_end = 244
    _globals['_LEAF']._serialized_start = 246
    _globals['_LEAF']._serialized_end = 296
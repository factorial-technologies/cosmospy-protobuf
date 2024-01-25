"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ...cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dosmosis/ibchooks/params.proto\x12\x10osmosis.ibchooks\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1egoogle/protobuf/duration.proto"U\n\x06Params\x12K\n\x1ballowed_async_ack_contracts\x18\x01 \x03(\tB&\xf2\xde\x1f"yaml:"allowed_async_ack_contracts"B7Z5github.com/osmosis-labs/osmosis/v21/x/ibc-hooks/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.ibchooks.params_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z5github.com/osmosis-labs/osmosis/v21/x/ibc-hooks/types'
    _globals['_PARAMS'].fields_by_name['allowed_async_ack_contracts']._options = None
    _globals['_PARAMS'].fields_by_name['allowed_async_ack_contracts']._serialized_options = b'\xf2\xde\x1f"yaml:"allowed_async_ack_contracts"'
    _globals['_PARAMS']._serialized_start = 132
    _globals['_PARAMS']._serialized_end = 217
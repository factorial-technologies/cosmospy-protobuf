"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....cosmos.app.v1alpha1 import module_pb2 as cosmos_dot_app_dot_v1alpha1_dot_module__pb2
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from .....amino import amino_pb2 as amino_dot_amino__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#cosmos/group/module/v1/module.proto\x12\x16cosmos.group.module.v1\x1a cosmos/app/v1alpha1/module.proto\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x11amino/amino.proto"\x98\x01\n\x06Module\x12F\n\x14max_execution_period\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationB\r\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xa8\xe7\xb0*\x01\x12\x18\n\x10max_metadata_len\x18\x02 \x01(\x04:,\xba\xc0\x96\xda\x01&\n$github.com/cosmos/cosmos-sdk/x/groupb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.group.module.v1.module_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals['_MODULE'].fields_by_name['max_execution_period']._options = None
    _globals['_MODULE'].fields_by_name['max_execution_period']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xa8\xe7\xb0*\x01'
    _globals['_MODULE']._options = None
    _globals['_MODULE']._serialized_options = b'\xba\xc0\x96\xda\x01&\n$github.com/cosmos/cosmos-sdk/x/group'
    _globals['_MODULE']._serialized_start = 171
    _globals['_MODULE']._serialized_end = 323
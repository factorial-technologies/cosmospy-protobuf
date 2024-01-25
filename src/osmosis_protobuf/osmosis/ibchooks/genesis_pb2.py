"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ...cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ...osmosis.ibchooks import params_pb2 as osmosis_dot_ibchooks_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eosmosis/ibchooks/genesis.proto\x12\x10osmosis.ibchooks\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1dosmosis/ibchooks/params.proto">\n\x0cGenesisState\x12.\n\x06params\x18\x01 \x01(\x0b2\x18.osmosis.ibchooks.ParamsB\x04\xc8\xde\x1f\x00B7Z5github.com/osmosis-labs/osmosis/v21/x/ibc-hooks/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.ibchooks.genesis_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z5github.com/osmosis-labs/osmosis/v21/x/ibc-hooks/types'
    _globals['_GENESISSTATE'].fields_by_name['params']._options = None
    _globals['_GENESISSTATE'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GENESISSTATE']._serialized_start = 132
    _globals['_GENESISSTATE']._serialized_end = 194
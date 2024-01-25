"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ...osmosis.incentives import group_pb2 as osmosis_dot_incentives_dot_group__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cosmosis/incentives/gov.proto\x12\x12osmosis.incentives\x1a\x14gogoproto/gogo.proto\x1a\x1eosmosis/incentives/group.proto"\x82\x01\n\x14CreateGroupsProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12<\n\rcreate_groups\x18\x03 \x03(\x0b2\x1f.osmosis.incentives.CreateGroupB\x04\xc8\xde\x1f\x00:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00B8Z6github.com/osmosis-labs/osmosis/v21/x/incentives/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.incentives.gov_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z6github.com/osmosis-labs/osmosis/v21/x/incentives/types'
    _globals['_CREATEGROUPSPROPOSAL'].fields_by_name['create_groups']._options = None
    _globals['_CREATEGROUPSPROPOSAL'].fields_by_name['create_groups']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_CREATEGROUPSPROPOSAL']._options = None
    _globals['_CREATEGROUPSPROPOSAL']._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _globals['_CREATEGROUPSPROPOSAL']._serialized_start = 107
    _globals['_CREATEGROUPSPROPOSAL']._serialized_end = 237
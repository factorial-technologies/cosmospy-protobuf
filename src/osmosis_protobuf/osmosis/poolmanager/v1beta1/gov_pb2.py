"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....osmosis.poolmanager.v1beta1 import tx_pb2 as osmosis_dot_poolmanager_dot_v1beta1_dot_tx__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%osmosis/poolmanager/v1beta1/gov.proto\x12\x1bosmosis.poolmanager.v1beta1\x1a\x14gogoproto/gogo.proto\x1a$osmosis/poolmanager/v1beta1/tx.proto"\x9d\x01\n\x19DenomPairTakerFeeProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12R\n\x14denom_pair_taker_fee\x18\x03 \x03(\x0b2..osmosis.poolmanager.v1beta1.DenomPairTakerFeeB\x04\xc8\xde\x1f\x00:\x08\x88\xa0\x1f\x00\x98\xa0\x1f\x00B9Z7github.com/osmosis-labs/osmosis/v21/x/poolmanager/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.poolmanager.v1beta1.gov_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/osmosis-labs/osmosis/v21/x/poolmanager/types'
    _globals['_DENOMPAIRTAKERFEEPROPOSAL'].fields_by_name['denom_pair_taker_fee']._options = None
    _globals['_DENOMPAIRTAKERFEEPROPOSAL'].fields_by_name['denom_pair_taker_fee']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_DENOMPAIRTAKERFEEPROPOSAL']._options = None
    _globals['_DENOMPAIRTAKERFEEPROPOSAL']._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00'
    _globals['_DENOMPAIRTAKERFEEPROPOSAL']._serialized_start = 131
    _globals['_DENOMPAIRTAKERFEEPROPOSAL']._serialized_end = 288
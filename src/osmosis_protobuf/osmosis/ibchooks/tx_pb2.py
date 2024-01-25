"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19osmosis/ibchooks/tx.proto\x12\x10osmosis.ibchooks\x1a\x14gogoproto/gogo.proto"\x8c\x01\n\rMsgEmitIBCAck\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x123\n\x0fpacket_sequence\x18\x02 \x01(\x04B\x1a\xf2\xde\x1f\x16yaml:"packet_sequence"\x12#\n\x07channel\x18\x03 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"channel""q\n\x15MsgEmitIBCAckResponse\x123\n\x0fcontract_result\x18\x01 \x01(\tB\x1a\xf2\xde\x1f\x16yaml:"contract_result"\x12#\n\x07ibc_ack\x18\x02 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"ibc_ack"2]\n\x03Msg\x12V\n\nEmitIBCAck\x12\x1f.osmosis.ibchooks.MsgEmitIBCAck\x1a\'.osmosis.ibchooks.MsgEmitIBCAckResponseB7Z5github.com/osmosis-labs/osmosis/v21/x/ibc-hooks/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.ibchooks.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z5github.com/osmosis-labs/osmosis/v21/x/ibc-hooks/types'
    _globals['_MSGEMITIBCACK'].fields_by_name['sender']._options = None
    _globals['_MSGEMITIBCACK'].fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _globals['_MSGEMITIBCACK'].fields_by_name['packet_sequence']._options = None
    _globals['_MSGEMITIBCACK'].fields_by_name['packet_sequence']._serialized_options = b'\xf2\xde\x1f\x16yaml:"packet_sequence"'
    _globals['_MSGEMITIBCACK'].fields_by_name['channel']._options = None
    _globals['_MSGEMITIBCACK'].fields_by_name['channel']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"channel"'
    _globals['_MSGEMITIBCACKRESPONSE'].fields_by_name['contract_result']._options = None
    _globals['_MSGEMITIBCACKRESPONSE'].fields_by_name['contract_result']._serialized_options = b'\xf2\xde\x1f\x16yaml:"contract_result"'
    _globals['_MSGEMITIBCACKRESPONSE'].fields_by_name['ibc_ack']._options = None
    _globals['_MSGEMITIBCACKRESPONSE'].fields_by_name['ibc_ack']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"ibc_ack"'
    _globals['_MSGEMITIBCACK']._serialized_start = 70
    _globals['_MSGEMITIBCACK']._serialized_end = 210
    _globals['_MSGEMITIBCACKRESPONSE']._serialized_start = 212
    _globals['_MSGEMITIBCACKRESPONSE']._serialized_end = 325
    _globals['_MSG']._serialized_start = 327
    _globals['_MSG']._serialized_end = 420
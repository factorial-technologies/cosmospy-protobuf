"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....tendermint.abci import types_pb2 as tendermint_dot_abci_dot_types__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#cosmos/base/abci/v1beta1/abci.proto\x12\x18cosmos.base.abci.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1btendermint/abci/types.proto\x1a\x19google/protobuf/any.proto"\xe6\x02\n\nTxResponse\x12\x0e\n\x06height\x18\x01 \x01(\x03\x12\x1a\n\x06txhash\x18\x02 \x01(\tB\n\xe2\xde\x1f\x06TxHash\x12\x11\n\tcodespace\x18\x03 \x01(\t\x12\x0c\n\x04code\x18\x04 \x01(\r\x12\x0c\n\x04data\x18\x05 \x01(\t\x12\x0f\n\x07raw_log\x18\x06 \x01(\t\x12O\n\x04logs\x18\x07 \x03(\x0b2(.cosmos.base.abci.v1beta1.ABCIMessageLogB\x17\xc8\xde\x1f\x00\xaa\xdf\x1f\x0fABCIMessageLogs\x12\x0c\n\x04info\x18\x08 \x01(\t\x12\x12\n\ngas_wanted\x18\t \x01(\x03\x12\x10\n\x08gas_used\x18\n \x01(\x03\x12 \n\x02tx\x18\x0b \x01(\x0b2\x14.google.protobuf.Any\x12\x11\n\ttimestamp\x18\x0c \x01(\t\x12,\n\x06events\x18\r \x03(\x0b2\x16.tendermint.abci.EventB\x04\xc8\xde\x1f\x00:\x04\x88\xa0\x1f\x00"\x92\x01\n\x0eABCIMessageLog\x12 \n\tmsg_index\x18\x01 \x01(\rB\r\xea\xde\x1f\tmsg_index\x12\x0b\n\x03log\x18\x02 \x01(\t\x12K\n\x06events\x18\x03 \x03(\x0b2%.cosmos.base.abci.v1beta1.StringEventB\x14\xc8\xde\x1f\x00\xaa\xdf\x1f\x0cStringEvents:\x04\x80\xdc \x01"`\n\x0bStringEvent\x12\x0c\n\x04type\x18\x01 \x01(\t\x12=\n\nattributes\x18\x02 \x03(\x0b2#.cosmos.base.abci.v1beta1.AttributeB\x04\xc8\xde\x1f\x00:\x04\x80\xdc \x01"\'\n\tAttribute\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t"/\n\x07GasInfo\x12\x12\n\ngas_wanted\x18\x01 \x01(\x04\x12\x10\n\x08gas_used\x18\x02 \x01(\x04"\x88\x01\n\x06Result\x12\x10\n\x04data\x18\x01 \x01(\x0cB\x02\x18\x01\x12\x0b\n\x03log\x18\x02 \x01(\t\x12,\n\x06events\x18\x03 \x03(\x0b2\x16.tendermint.abci.EventB\x04\xc8\xde\x1f\x00\x12+\n\rmsg_responses\x18\x04 \x03(\x0b2\x14.google.protobuf.Any:\x04\x88\xa0\x1f\x00"\x85\x01\n\x12SimulationResponse\x12=\n\x08gas_info\x18\x01 \x01(\x0b2!.cosmos.base.abci.v1beta1.GasInfoB\x08\xc8\xde\x1f\x00\xd0\xde\x1f\x01\x120\n\x06result\x18\x02 \x01(\x0b2 .cosmos.base.abci.v1beta1.Result"1\n\x07MsgData\x12\x10\n\x08msg_type\x18\x01 \x01(\t\x12\x0c\n\x04data\x18\x02 \x01(\x0c:\x06\x18\x01\x80\xdc \x01"s\n\tTxMsgData\x123\n\x04data\x18\x01 \x03(\x0b2!.cosmos.base.abci.v1beta1.MsgDataB\x02\x18\x01\x12+\n\rmsg_responses\x18\x02 \x03(\x0b2\x14.google.protobuf.Any:\x04\x80\xdc \x01"\xa6\x01\n\x0fSearchTxsResult\x12\x13\n\x0btotal_count\x18\x01 \x01(\x04\x12\r\n\x05count\x18\x02 \x01(\x04\x12\x13\n\x0bpage_number\x18\x03 \x01(\x04\x12\x12\n\npage_total\x18\x04 \x01(\x04\x12\r\n\x05limit\x18\x05 \x01(\x04\x121\n\x03txs\x18\x06 \x03(\x0b2$.cosmos.base.abci.v1beta1.TxResponse:\x04\x80\xdc \x01B(Z"github.com/cosmos/cosmos-sdk/types\xd8\xe1\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.base.abci.v1beta1.abci_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z"github.com/cosmos/cosmos-sdk/types\xd8\xe1\x1e\x00'
    _globals['_TXRESPONSE'].fields_by_name['txhash']._options = None
    _globals['_TXRESPONSE'].fields_by_name['txhash']._serialized_options = b'\xe2\xde\x1f\x06TxHash'
    _globals['_TXRESPONSE'].fields_by_name['logs']._options = None
    _globals['_TXRESPONSE'].fields_by_name['logs']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f\x0fABCIMessageLogs'
    _globals['_TXRESPONSE'].fields_by_name['events']._options = None
    _globals['_TXRESPONSE'].fields_by_name['events']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_TXRESPONSE']._options = None
    _globals['_TXRESPONSE']._serialized_options = b'\x88\xa0\x1f\x00'
    _globals['_ABCIMESSAGELOG'].fields_by_name['msg_index']._options = None
    _globals['_ABCIMESSAGELOG'].fields_by_name['msg_index']._serialized_options = b'\xea\xde\x1f\tmsg_index'
    _globals['_ABCIMESSAGELOG'].fields_by_name['events']._options = None
    _globals['_ABCIMESSAGELOG'].fields_by_name['events']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f\x0cStringEvents'
    _globals['_ABCIMESSAGELOG']._options = None
    _globals['_ABCIMESSAGELOG']._serialized_options = b'\x80\xdc \x01'
    _globals['_STRINGEVENT'].fields_by_name['attributes']._options = None
    _globals['_STRINGEVENT'].fields_by_name['attributes']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_STRINGEVENT']._options = None
    _globals['_STRINGEVENT']._serialized_options = b'\x80\xdc \x01'
    _globals['_RESULT'].fields_by_name['data']._options = None
    _globals['_RESULT'].fields_by_name['data']._serialized_options = b'\x18\x01'
    _globals['_RESULT'].fields_by_name['events']._options = None
    _globals['_RESULT'].fields_by_name['events']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_RESULT']._options = None
    _globals['_RESULT']._serialized_options = b'\x88\xa0\x1f\x00'
    _globals['_SIMULATIONRESPONSE'].fields_by_name['gas_info']._options = None
    _globals['_SIMULATIONRESPONSE'].fields_by_name['gas_info']._serialized_options = b'\xc8\xde\x1f\x00\xd0\xde\x1f\x01'
    _globals['_MSGDATA']._options = None
    _globals['_MSGDATA']._serialized_options = b'\x18\x01\x80\xdc \x01'
    _globals['_TXMSGDATA'].fields_by_name['data']._options = None
    _globals['_TXMSGDATA'].fields_by_name['data']._serialized_options = b'\x18\x01'
    _globals['_TXMSGDATA']._options = None
    _globals['_TXMSGDATA']._serialized_options = b'\x80\xdc \x01'
    _globals['_SEARCHTXSRESULT']._options = None
    _globals['_SEARCHTXSRESULT']._serialized_options = b'\x80\xdc \x01'
    _globals['_TXRESPONSE']._serialized_start = 144
    _globals['_TXRESPONSE']._serialized_end = 502
    _globals['_ABCIMESSAGELOG']._serialized_start = 505
    _globals['_ABCIMESSAGELOG']._serialized_end = 651
    _globals['_STRINGEVENT']._serialized_start = 653
    _globals['_STRINGEVENT']._serialized_end = 749
    _globals['_ATTRIBUTE']._serialized_start = 751
    _globals['_ATTRIBUTE']._serialized_end = 790
    _globals['_GASINFO']._serialized_start = 792
    _globals['_GASINFO']._serialized_end = 839
    _globals['_RESULT']._serialized_start = 842
    _globals['_RESULT']._serialized_end = 978
    _globals['_SIMULATIONRESPONSE']._serialized_start = 981
    _globals['_SIMULATIONRESPONSE']._serialized_end = 1114
    _globals['_MSGDATA']._serialized_start = 1116
    _globals['_MSGDATA']._serialized_end = 1165
    _globals['_TXMSGDATA']._serialized_start = 1167
    _globals['_TXMSGDATA']._serialized_end = 1282
    _globals['_SEARCHTXSRESULT']._serialized_start = 1285
    _globals['_SEARCHTXSRESULT']._serialized_end = 1451
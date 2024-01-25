"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ......gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ......cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEosmosis/concentratedliquidity/poolmodel/concentrated/v1beta1/tx.proto\x12<osmosis.concentratedliquidity.poolmodel.concentrated.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto"\x87\x02\n\x19MsgCreateConcentratedPool\x12!\n\x06sender\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"sender"\x12!\n\x06denom0\x18\x02 \x01(\tB\x11\xf2\xde\x1f\ryaml:"denom0"\x12!\n\x06denom1\x18\x03 \x01(\tB\x11\xf2\xde\x1f\ryaml:"denom1"\x12-\n\x0ctick_spacing\x18\x04 \x01(\x04B\x17\xf2\xde\x1f\x13yaml:"tick_spacing"\x12R\n\rspread_factor\x18\x05 \x01(\tB;\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xf2\xde\x1f\x14yaml:"spread_factor""@\n!MsgCreateConcentratedPoolResponse\x12\x1b\n\x07pool_id\x18\x01 \x01(\x04B\n\xe2\xde\x1f\x06PoolID2\xda\x01\n\x03Msg\x12\xd2\x01\n\x16CreateConcentratedPool\x12W.osmosis.concentratedliquidity.poolmodel.concentrated.v1beta1.MsgCreateConcentratedPool\x1a_.osmosis.concentratedliquidity.poolmodel.concentrated.v1beta1.MsgCreateConcentratedPoolResponseBDZBgithub.com/osmosis-labs/osmosis/v21/x/concentrated-liquidity/modelb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.concentratedliquidity.poolmodel.concentrated.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'ZBgithub.com/osmosis-labs/osmosis/v21/x/concentrated-liquidity/model'
    _globals['_MSGCREATECONCENTRATEDPOOL'].fields_by_name['sender']._options = None
    _globals['_MSGCREATECONCENTRATEDPOOL'].fields_by_name['sender']._serialized_options = b'\xf2\xde\x1f\ryaml:"sender"'
    _globals['_MSGCREATECONCENTRATEDPOOL'].fields_by_name['denom0']._options = None
    _globals['_MSGCREATECONCENTRATEDPOOL'].fields_by_name['denom0']._serialized_options = b'\xf2\xde\x1f\ryaml:"denom0"'
    _globals['_MSGCREATECONCENTRATEDPOOL'].fields_by_name['denom1']._options = None
    _globals['_MSGCREATECONCENTRATEDPOOL'].fields_by_name['denom1']._serialized_options = b'\xf2\xde\x1f\ryaml:"denom1"'
    _globals['_MSGCREATECONCENTRATEDPOOL'].fields_by_name['tick_spacing']._options = None
    _globals['_MSGCREATECONCENTRATEDPOOL'].fields_by_name['tick_spacing']._serialized_options = b'\xf2\xde\x1f\x13yaml:"tick_spacing"'
    _globals['_MSGCREATECONCENTRATEDPOOL'].fields_by_name['spread_factor']._options = None
    _globals['_MSGCREATECONCENTRATEDPOOL'].fields_by_name['spread_factor']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xf2\xde\x1f\x14yaml:"spread_factor"'
    _globals['_MSGCREATECONCENTRATEDPOOLRESPONSE'].fields_by_name['pool_id']._options = None
    _globals['_MSGCREATECONCENTRATEDPOOLRESPONSE'].fields_by_name['pool_id']._serialized_options = b'\xe2\xde\x1f\x06PoolID'
    _globals['_MSGCREATECONCENTRATEDPOOL']._serialized_start = 190
    _globals['_MSGCREATECONCENTRATEDPOOL']._serialized_end = 453
    _globals['_MSGCREATECONCENTRATEDPOOLRESPONSE']._serialized_start = 455
    _globals['_MSGCREATECONCENTRATEDPOOLRESPONSE']._serialized_end = 519
    _globals['_MSG']._serialized_start = 522
    _globals['_MSG']._serialized_end = 740
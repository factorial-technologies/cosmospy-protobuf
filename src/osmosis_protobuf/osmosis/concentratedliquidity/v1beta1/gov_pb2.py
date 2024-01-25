"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/osmosis/concentratedliquidity/v1beta1/gov.proto\x12%osmosis.concentratedliquidity.v1beta1\x1a\x14gogoproto/gogo.proto"\xc2\x01\n(CreateConcentratedLiquidityPoolsProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12d\n\x0cpool_records\x18\x03 \x03(\x0b21.osmosis.concentratedliquidity.v1beta1.PoolRecordB\x1b\xc8\xde\x1f\x00\xf2\xde\x1f\x13yaml:"pool_records":\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x01"\xc0\x01\n\x1bTickSpacingDecreaseProposal\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12o\n\x1fpool_id_to_tick_spacing_records\x18\x03 \x03(\x0b2@.osmosis.concentratedliquidity.v1beta1.PoolIdToTickSpacingRecordB\x04\xc8\xde\x1f\x00:\x0c\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x01"L\n\x19PoolIdToTickSpacingRecord\x12\x0f\n\x07pool_id\x18\x01 \x01(\x04\x12\x18\n\x10new_tick_spacing\x18\x02 \x01(\x04:\x04\xe8\xa0\x1f\x01"\xe1\x01\n\nPoolRecord\x12!\n\x06denom0\x18\x01 \x01(\tB\x11\xf2\xde\x1f\ryaml:"denom0"\x12!\n\x06denom1\x18\x02 \x01(\tB\x11\xf2\xde\x1f\ryaml:"denom1"\x12-\n\x0ctick_spacing\x18\x03 \x01(\x04B\x17\xf2\xde\x1f\x13yaml:"tick_spacing"\x12R\n\rspread_factor\x18\x05 \x01(\tB;\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xf2\xde\x1f\x14yaml:"spread_factor":\x04\xe8\xa0\x1f\x01J\x04\x08\x04\x10\x05BDZBgithub.com/osmosis-labs/osmosis/v21/x/concentrated-liquidity/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.concentratedliquidity.v1beta1.gov_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'ZBgithub.com/osmosis-labs/osmosis/v21/x/concentrated-liquidity/types'
    _globals['_CREATECONCENTRATEDLIQUIDITYPOOLSPROPOSAL'].fields_by_name['pool_records']._options = None
    _globals['_CREATECONCENTRATEDLIQUIDITYPOOLSPROPOSAL'].fields_by_name['pool_records']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x13yaml:"pool_records"'
    _globals['_CREATECONCENTRATEDLIQUIDITYPOOLSPROPOSAL']._options = None
    _globals['_CREATECONCENTRATEDLIQUIDITYPOOLSPROPOSAL']._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x01'
    _globals['_TICKSPACINGDECREASEPROPOSAL'].fields_by_name['pool_id_to_tick_spacing_records']._options = None
    _globals['_TICKSPACINGDECREASEPROPOSAL'].fields_by_name['pool_id_to_tick_spacing_records']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_TICKSPACINGDECREASEPROPOSAL']._options = None
    _globals['_TICKSPACINGDECREASEPROPOSAL']._serialized_options = b'\x88\xa0\x1f\x00\x98\xa0\x1f\x00\xe8\xa0\x1f\x01'
    _globals['_POOLIDTOTICKSPACINGRECORD']._options = None
    _globals['_POOLIDTOTICKSPACINGRECORD']._serialized_options = b'\xe8\xa0\x1f\x01'
    _globals['_POOLRECORD'].fields_by_name['denom0']._options = None
    _globals['_POOLRECORD'].fields_by_name['denom0']._serialized_options = b'\xf2\xde\x1f\ryaml:"denom0"'
    _globals['_POOLRECORD'].fields_by_name['denom1']._options = None
    _globals['_POOLRECORD'].fields_by_name['denom1']._serialized_options = b'\xf2\xde\x1f\ryaml:"denom1"'
    _globals['_POOLRECORD'].fields_by_name['tick_spacing']._options = None
    _globals['_POOLRECORD'].fields_by_name['tick_spacing']._serialized_options = b'\xf2\xde\x1f\x13yaml:"tick_spacing"'
    _globals['_POOLRECORD'].fields_by_name['spread_factor']._options = None
    _globals['_POOLRECORD'].fields_by_name['spread_factor']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xf2\xde\x1f\x14yaml:"spread_factor"'
    _globals['_POOLRECORD']._options = None
    _globals['_POOLRECORD']._serialized_options = b'\xe8\xa0\x1f\x01'
    _globals['_CREATECONCENTRATEDLIQUIDITYPOOLSPROPOSAL']._serialized_start = 113
    _globals['_CREATECONCENTRATEDLIQUIDITYPOOLSPROPOSAL']._serialized_end = 307
    _globals['_TICKSPACINGDECREASEPROPOSAL']._serialized_start = 310
    _globals['_TICKSPACINGDECREASEPROPOSAL']._serialized_end = 502
    _globals['_POOLIDTOTICKSPACINGRECORD']._serialized_start = 504
    _globals['_POOLIDTOTICKSPACINGRECORD']._serialized_end = 580
    _globals['_POOLRECORD']._serialized_start = 583
    _globals['_POOLRECORD']._serialized_end = 808
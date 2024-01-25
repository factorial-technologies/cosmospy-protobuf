"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"osmosis/poolmanager/v2/query.proto\x12\x16osmosis.poolmanager.v2\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x19google/protobuf/any.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa7\x01\n\x10SpotPriceRequest\x12#\n\x07pool_id\x18\x01 \x01(\x04B\x12\xf2\xde\x1f\x0eyaml:"pool_id"\x125\n\x10base_asset_denom\x18\x02 \x01(\tB\x1b\xf2\xde\x1f\x17yaml:"base_asset_denom"\x127\n\x11quote_asset_denom\x18\x03 \x01(\tB\x1c\xf2\xde\x1f\x18yaml:"quote_asset_denom""u\n\x11SpotPriceResponse\x12`\n\nspot_price\x18\x01 \x01(\tBL\xc8\xde\x1f\x00\xda\xde\x1f/github.com/osmosis-labs/osmosis/osmomath.BigDec\xf2\xde\x1f\x11yaml:"spot_price"2\xa4\x01\n\x05Query\x12\x9a\x01\n\x0bSpotPriceV2\x12(.osmosis.poolmanager.v2.SpotPriceRequest\x1a).osmosis.poolmanager.v2.SpotPriceResponse"6\x82\xd3\xe4\x93\x020\x12./osmosis/poolmanager/v2/pools/{pool_id}/pricesBGZEgithub.com/osmosis-labs/osmosis/v21/x/poolmanager/client/queryprotov2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.poolmanager.v2.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'ZEgithub.com/osmosis-labs/osmosis/v21/x/poolmanager/client/queryprotov2'
    _globals['_SPOTPRICEREQUEST'].fields_by_name['pool_id']._options = None
    _globals['_SPOTPRICEREQUEST'].fields_by_name['pool_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"pool_id"'
    _globals['_SPOTPRICEREQUEST'].fields_by_name['base_asset_denom']._options = None
    _globals['_SPOTPRICEREQUEST'].fields_by_name['base_asset_denom']._serialized_options = b'\xf2\xde\x1f\x17yaml:"base_asset_denom"'
    _globals['_SPOTPRICEREQUEST'].fields_by_name['quote_asset_denom']._options = None
    _globals['_SPOTPRICEREQUEST'].fields_by_name['quote_asset_denom']._serialized_options = b'\xf2\xde\x1f\x18yaml:"quote_asset_denom"'
    _globals['_SPOTPRICERESPONSE'].fields_by_name['spot_price']._options = None
    _globals['_SPOTPRICERESPONSE'].fields_by_name['spot_price']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f/github.com/osmosis-labs/osmosis/osmomath.BigDec\xf2\xde\x1f\x11yaml:"spot_price"'
    _globals['_QUERY'].methods_by_name['SpotPriceV2']._options = None
    _globals['_QUERY'].methods_by_name['SpotPriceV2']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./osmosis/poolmanager/v2/pools/{pool_id}/prices'
    _globals['_SPOTPRICEREQUEST']._serialized_start = 202
    _globals['_SPOTPRICEREQUEST']._serialized_end = 369
    _globals['_SPOTPRICERESPONSE']._serialized_start = 371
    _globals['_SPOTPRICERESPONSE']._serialized_end = 488
    _globals['_QUERY']._serialized_start = 491
    _globals['_QUERY']._serialized_end = 655
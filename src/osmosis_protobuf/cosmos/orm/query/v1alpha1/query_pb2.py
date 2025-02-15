"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from .....cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%cosmos/orm/query/v1alpha1/query.proto\x12\x19cosmos.orm.query.v1alpha1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x19google/protobuf/any.proto\x1a*cosmos/base/query/v1beta1/pagination.proto"h\n\nGetRequest\x12\x14\n\x0cmessage_name\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\t\x125\n\x06values\x18\x03 \x03(\x0b2%.cosmos.orm.query.v1alpha1.IndexValue"3\n\x0bGetResponse\x12$\n\x06result\x18\x01 \x01(\x0b2\x14.google.protobuf.Any"\xab\x03\n\x0bListRequest\x12\x14\n\x0cmessage_name\x18\x01 \x01(\t\x12\r\n\x05index\x18\x02 \x01(\t\x12?\n\x06prefix\x18\x03 \x01(\x0b2-.cosmos.orm.query.v1alpha1.ListRequest.PrefixH\x00\x12=\n\x05range\x18\x04 \x01(\x0b2,.cosmos.orm.query.v1alpha1.ListRequest.RangeH\x00\x12:\n\npagination\x18\x05 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest\x1a?\n\x06Prefix\x125\n\x06values\x18\x01 \x03(\x0b2%.cosmos.orm.query.v1alpha1.IndexValue\x1aq\n\x05Range\x124\n\x05start\x18\x01 \x03(\x0b2%.cosmos.orm.query.v1alpha1.IndexValue\x122\n\x03end\x18\x02 \x03(\x0b2%.cosmos.orm.query.v1alpha1.IndexValueB\x07\n\x05query"r\n\x0cListResponse\x12%\n\x07results\x18\x01 \x03(\x0b2\x14.google.protobuf.Any\x12;\n\npagination\x18\x05 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"\xd4\x01\n\nIndexValue\x12\x0e\n\x04uint\x18\x01 \x01(\x04H\x00\x12\r\n\x03int\x18\x02 \x01(\x03H\x00\x12\r\n\x03str\x18\x03 \x01(\tH\x00\x12\x0f\n\x05bytes\x18\x04 \x01(\x0cH\x00\x12\x0e\n\x04enum\x18\x05 \x01(\tH\x00\x12\x0e\n\x04bool\x18\x06 \x01(\x08H\x00\x12/\n\ttimestamp\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00\x12-\n\x08duration\x18\x08 \x01(\x0b2\x19.google.protobuf.DurationH\x00B\x07\n\x05value2\xb6\x01\n\x05Query\x12T\n\x03Get\x12%.cosmos.orm.query.v1alpha1.GetRequest\x1a&.cosmos.orm.query.v1alpha1.GetResponse\x12W\n\x04List\x12&.cosmos.orm.query.v1alpha1.ListRequest\x1a\'.cosmos.orm.query.v1alpha1.ListResponseb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.orm.query.v1alpha1.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    _globals['_GETREQUEST']._serialized_start = 204
    _globals['_GETREQUEST']._serialized_end = 308
    _globals['_GETRESPONSE']._serialized_start = 310
    _globals['_GETRESPONSE']._serialized_end = 361
    _globals['_LISTREQUEST']._serialized_start = 364
    _globals['_LISTREQUEST']._serialized_end = 791
    _globals['_LISTREQUEST_PREFIX']._serialized_start = 604
    _globals['_LISTREQUEST_PREFIX']._serialized_end = 667
    _globals['_LISTREQUEST_RANGE']._serialized_start = 669
    _globals['_LISTREQUEST_RANGE']._serialized_end = 782
    _globals['_LISTRESPONSE']._serialized_start = 793
    _globals['_LISTRESPONSE']._serialized_end = 907
    _globals['_INDEXVALUE']._serialized_start = 910
    _globals['_INDEXVALUE']._serialized_end = 1122
    _globals['_QUERY']._serialized_start = 1125
    _globals['_QUERY']._serialized_end = 1307
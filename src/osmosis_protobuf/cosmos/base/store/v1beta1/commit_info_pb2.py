"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+cosmos/base/store/v1beta1/commit_info.proto\x12\x19cosmos.base.store.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x97\x01\n\nCommitInfo\x12\x0f\n\x07version\x18\x01 \x01(\x03\x12?\n\x0bstore_infos\x18\x02 \x03(\x0b2$.cosmos.base.store.v1beta1.StoreInfoB\x04\xc8\xde\x1f\x00\x127\n\ttimestamp\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01"W\n\tStoreInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12<\n\tcommit_id\x18\x02 \x01(\x0b2#.cosmos.base.store.v1beta1.CommitIDB\x04\xc8\xde\x1f\x00"/\n\x08CommitID\x12\x0f\n\x07version\x18\x01 \x01(\x03\x12\x0c\n\x04hash\x18\x02 \x01(\x0c:\x04\x98\xa0\x1f\x00B*Z(github.com/cosmos/cosmos-sdk/store/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.base.store.v1beta1.commit_info_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z(github.com/cosmos/cosmos-sdk/store/types'
    _globals['_COMMITINFO'].fields_by_name['store_infos']._options = None
    _globals['_COMMITINFO'].fields_by_name['store_infos']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_COMMITINFO'].fields_by_name['timestamp']._options = None
    _globals['_COMMITINFO'].fields_by_name['timestamp']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _globals['_STOREINFO'].fields_by_name['commit_id']._options = None
    _globals['_STOREINFO'].fields_by_name['commit_id']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_COMMITID']._options = None
    _globals['_COMMITID']._serialized_options = b'\x98\xa0\x1f\x00'
    _globals['_COMMITINFO']._serialized_start = 130
    _globals['_COMMITINFO']._serialized_end = 281
    _globals['_STOREINFO']._serialized_start = 283
    _globals['_STOREINFO']._serialized_end = 370
    _globals['_COMMITID']._serialized_start = 372
    _globals['_COMMITID']._serialized_end = 419
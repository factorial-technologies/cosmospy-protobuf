"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1etendermint/mempool/types.proto\x12\x12tendermint.mempool"\x12\n\x03Txs\x12\x0b\n\x03txs\x18\x01 \x03(\x0c"8\n\x07Message\x12&\n\x03txs\x18\x01 \x01(\x0b2\x17.tendermint.mempool.TxsH\x00B\x05\n\x03sumB7Z5github.com/cometbft/cometbft/proto/tendermint/mempoolb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tendermint.mempool.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z5github.com/cometbft/cometbft/proto/tendermint/mempool'
    _globals['_TXS']._serialized_start = 54
    _globals['_TXS']._serialized_end = 72
    _globals['_MESSAGE']._serialized_start = 74
    _globals['_MESSAGE']._serialized_end = 130
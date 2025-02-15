"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from .....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....ibc.core.channel.v1 import channel_pb2 as ibc_dot_core_dot_channel_dot_v1_dot_channel__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!ibc/applications/fee/v1/fee.proto\x12\x17ibc.applications.fee.v1\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a!ibc/core/channel/v1/channel.proto"\xdf\x02\n\x03Fee\x12p\n\x08recv_fee\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBC\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"recv_fee"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12n\n\x07ack_fee\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBB\xc8\xde\x1f\x00\xf2\xde\x1f\x0eyaml:"ack_fee"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12v\n\x0btimeout_fee\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinBF\xc8\xde\x1f\x00\xf2\xde\x1f\x12yaml:"timeout_fee"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"\x81\x01\n\tPacketFee\x12/\n\x03fee\x18\x01 \x01(\x0b2\x1c.ibc.applications.fee.v1.FeeB\x04\xc8\xde\x1f\x00\x121\n\x0erefund_address\x18\x02 \x01(\tB\x19\xf2\xde\x1f\x15yaml:"refund_address"\x12\x10\n\x08relayers\x18\x03 \x03(\t"a\n\nPacketFees\x12S\n\x0bpacket_fees\x18\x01 \x03(\x0b2".ibc.applications.fee.v1.PacketFeeB\x1a\xc8\xde\x1f\x00\xf2\xde\x1f\x12yaml:"packet_fees""\xb7\x01\n\x14IdentifiedPacketFees\x12J\n\tpacket_id\x18\x01 \x01(\x0b2\x1d.ibc.core.channel.v1.PacketIdB\x18\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"packet_id"\x12S\n\x0bpacket_fees\x18\x02 \x03(\x0b2".ibc.applications.fee.v1.PacketFeeB\x1a\xc8\xde\x1f\x00\xf2\xde\x1f\x12yaml:"packet_fees"B7Z5github.com/cosmos/ibc-go/v4/modules/apps/29-fee/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.fee.v1.fee_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z5github.com/cosmos/ibc-go/v4/modules/apps/29-fee/types'
    _globals['_FEE'].fields_by_name['recv_fee']._options = None
    _globals['_FEE'].fields_by_name['recv_fee']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"recv_fee"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_FEE'].fields_by_name['ack_fee']._options = None
    _globals['_FEE'].fields_by_name['ack_fee']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x0eyaml:"ack_fee"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_FEE'].fields_by_name['timeout_fee']._options = None
    _globals['_FEE'].fields_by_name['timeout_fee']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x12yaml:"timeout_fee"\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_PACKETFEE'].fields_by_name['fee']._options = None
    _globals['_PACKETFEE'].fields_by_name['fee']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_PACKETFEE'].fields_by_name['refund_address']._options = None
    _globals['_PACKETFEE'].fields_by_name['refund_address']._serialized_options = b'\xf2\xde\x1f\x15yaml:"refund_address"'
    _globals['_PACKETFEES'].fields_by_name['packet_fees']._options = None
    _globals['_PACKETFEES'].fields_by_name['packet_fees']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x12yaml:"packet_fees"'
    _globals['_IDENTIFIEDPACKETFEES'].fields_by_name['packet_id']._options = None
    _globals['_IDENTIFIEDPACKETFEES'].fields_by_name['packet_id']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"packet_id"'
    _globals['_IDENTIFIEDPACKETFEES'].fields_by_name['packet_fees']._options = None
    _globals['_IDENTIFIEDPACKETFEES'].fields_by_name['packet_fees']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x12yaml:"packet_fees"'
    _globals['_FEE']._serialized_start = 152
    _globals['_FEE']._serialized_end = 503
    _globals['_PACKETFEE']._serialized_start = 506
    _globals['_PACKETFEE']._serialized_end = 635
    _globals['_PACKETFEES']._serialized_start = 637
    _globals['_PACKETFEES']._serialized_end = 734
    _globals['_IDENTIFIEDPACKETFEES']._serialized_start = 737
    _globals['_IDENTIFIEDPACKETFEES']._serialized_end = 920
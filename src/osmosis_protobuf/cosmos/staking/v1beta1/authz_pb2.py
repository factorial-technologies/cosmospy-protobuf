"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....amino import amino_pb2 as amino_dot_amino__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"cosmos/staking/v1beta1/authz.proto\x12\x16cosmos.staking.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x11amino/amino.proto"\xe1\x03\n\x12StakeAuthorization\x12Z\n\nmax_tokens\x18\x01 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB+\xaa\xdf\x1f\'github.com/cosmos/cosmos-sdk/types.Coin\x12K\n\nallow_list\x18\x02 \x01(\x0b25.cosmos.staking.v1beta1.StakeAuthorization.ValidatorsH\x00\x12J\n\tdeny_list\x18\x03 \x01(\x0b25.cosmos.staking.v1beta1.StakeAuthorization.ValidatorsH\x00\x12E\n\x12authorization_type\x18\x04 \x01(\x0e2).cosmos.staking.v1beta1.AuthorizationType\x1a7\n\nValidators\x12)\n\x07address\x18\x01 \x03(\tB\x18\xd2\xb4-\x14cosmos.AddressString:H\xca\xb4-"cosmos.authz.v1beta1.Authorization\x8a\xe7\xb0*\x1dcosmos-sdk/StakeAuthorizationB\x0c\n\nvalidators*\x9e\x01\n\x11AuthorizationType\x12"\n\x1eAUTHORIZATION_TYPE_UNSPECIFIED\x10\x00\x12\x1f\n\x1bAUTHORIZATION_TYPE_DELEGATE\x10\x01\x12!\n\x1dAUTHORIZATION_TYPE_UNDELEGATE\x10\x02\x12!\n\x1dAUTHORIZATION_TYPE_REDELEGATE\x10\x03B.Z,github.com/cosmos/cosmos-sdk/x/staking/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.staking.v1beta1.authz_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z,github.com/cosmos/cosmos-sdk/x/staking/types'
    _globals['_STAKEAUTHORIZATION_VALIDATORS'].fields_by_name['address']._options = None
    _globals['_STAKEAUTHORIZATION_VALIDATORS'].fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_STAKEAUTHORIZATION'].fields_by_name['max_tokens']._options = None
    _globals['_STAKEAUTHORIZATION'].fields_by_name['max_tokens']._serialized_options = b"\xaa\xdf\x1f'github.com/cosmos/cosmos-sdk/types.Coin"
    _globals['_STAKEAUTHORIZATION']._options = None
    _globals['_STAKEAUTHORIZATION']._serialized_options = b'\xca\xb4-"cosmos.authz.v1beta1.Authorization\x8a\xe7\xb0*\x1dcosmos-sdk/StakeAuthorization'
    _globals['_AUTHORIZATIONTYPE']._serialized_start = 647
    _globals['_AUTHORIZATIONTYPE']._serialized_end = 805
    _globals['_STAKEAUTHORIZATION']._serialized_start = 163
    _globals['_STAKEAUTHORIZATION']._serialized_end = 644
    _globals['_STAKEAUTHORIZATION_VALIDATORS']._serialized_start = 501
    _globals['_STAKEAUTHORIZATION_VALIDATORS']._serialized_end = 556
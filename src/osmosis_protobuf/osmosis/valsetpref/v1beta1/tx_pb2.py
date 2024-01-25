"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....amino import amino_pb2 as amino_dot_amino__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....osmosis.valsetpref.v1beta1 import state_pb2 as osmosis_dot_valsetpref_dot_v1beta1_dot_state__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#osmosis/valsetpref/v1beta1/tx.proto\x12\x1aosmosis.valsetpref.v1beta1\x1a\x14gogoproto/gogo.proto\x1a\x11amino/amino.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a&osmosis/valsetpref/v1beta1/state.proto"\xd4\x01\n\x1cMsgSetValidatorSetPreference\x12\'\n\tdelegator\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"delegator"\x12`\n\x0bpreferences\x18\x02 \x03(\x0b2/.osmosis.valsetpref.v1beta1.ValidatorPreferenceB\x1a\xc8\xde\x1f\x00\xf2\xde\x1f\x12yaml:"preferences":)\x8a\xe7\xb0*$osmosis/MsgSetValidatorSetPreference"&\n$MsgSetValidatorSetPreferenceResponse"\xc6\x01\n\x19MsgDelegateToValidatorSet\x12\'\n\tdelegator\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"delegator"\x12X\n\x04coin\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB/\xc8\xde\x1f\x00\xaa\xdf\x1f\'github.com/cosmos/cosmos-sdk/types.Coin:&\x8a\xe7\xb0*!osmosis/MsgDelegateToValidatorSet"#\n!MsgDelegateToValidatorSetResponse"\xce\x01\n\x1dMsgUndelegateFromValidatorSet\x12\'\n\tdelegator\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"delegator"\x12X\n\x04coin\x18\x03 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB/\xc8\xde\x1f\x00\xaa\xdf\x1f\'github.com/cosmos/cosmos-sdk/types.Coin:*\x8a\xe7\xb0*%osmosis/MsgUndelegateFromValidatorSet"\'\n%MsgUndelegateFromValidatorSetResponse"\xd7\x01\n\'MsgUndelegateFromRebalancedValidatorSet\x12\'\n\tdelegator\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"delegator"\x12X\n\x04coin\x18\x02 \x01(\x0b2\x19.cosmos.base.v1beta1.CoinB/\xc8\xde\x1f\x00\xaa\xdf\x1f\'github.com/cosmos/cosmos-sdk/types.Coin:)\x8a\xe7\xb0*$osmosis/MsgUndelegateFromRebalValset"1\n/MsgUndelegateFromRebalancedValidatorSetResponse"\xce\x01\n\x19MsgRedelegateValidatorSet\x12\'\n\tdelegator\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"delegator"\x12`\n\x0bpreferences\x18\x02 \x03(\x0b2/.osmosis.valsetpref.v1beta1.ValidatorPreferenceB\x1a\xc8\xde\x1f\x00\xf2\xde\x1f\x12yaml:"preferences":&\x8a\xe7\xb0*!osmosis/MsgRedelegateValidatorSet"#\n!MsgRedelegateValidatorSetResponse"r\n\x1cMsgWithdrawDelegationRewards\x12\'\n\tdelegator\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"delegator":)\x8a\xe7\xb0*$osmosis/MsgWithdrawDelegationRewards"&\n$MsgWithdrawDelegationRewardsResponse"R\n\x17MsgDelegateBondedTokens\x12\'\n\tdelegator\x18\x01 \x01(\tB\x14\xf2\xde\x1f\x10yaml:"delegator"\x12\x0e\n\x06lockID\x18\x02 \x01(\x04"!\n\x1fMsgDelegateBondedTokensResponse2\xbe\x08\n\x03Msg\x12\x97\x01\n\x19SetValidatorSetPreference\x128.osmosis.valsetpref.v1beta1.MsgSetValidatorSetPreference\x1a@.osmosis.valsetpref.v1beta1.MsgSetValidatorSetPreferenceResponse\x12\x8e\x01\n\x16DelegateToValidatorSet\x125.osmosis.valsetpref.v1beta1.MsgDelegateToValidatorSet\x1a=.osmosis.valsetpref.v1beta1.MsgDelegateToValidatorSetResponse\x12\x9a\x01\n\x1aUndelegateFromValidatorSet\x129.osmosis.valsetpref.v1beta1.MsgUndelegateFromValidatorSet\x1aA.osmosis.valsetpref.v1beta1.MsgUndelegateFromValidatorSetResponse\x12\xb8\x01\n$UndelegateFromRebalancedValidatorSet\x12C.osmosis.valsetpref.v1beta1.MsgUndelegateFromRebalancedValidatorSet\x1aK.osmosis.valsetpref.v1beta1.MsgUndelegateFromRebalancedValidatorSetResponse\x12\x8e\x01\n\x16RedelegateValidatorSet\x125.osmosis.valsetpref.v1beta1.MsgRedelegateValidatorSet\x1a=.osmosis.valsetpref.v1beta1.MsgRedelegateValidatorSetResponse\x12\x97\x01\n\x19WithdrawDelegationRewards\x128.osmosis.valsetpref.v1beta1.MsgWithdrawDelegationRewards\x1a@.osmosis.valsetpref.v1beta1.MsgWithdrawDelegationRewardsResponse\x12\x88\x01\n\x14DelegateBondedTokens\x123.osmosis.valsetpref.v1beta1.MsgDelegateBondedTokens\x1a;.osmosis.valsetpref.v1beta1.MsgDelegateBondedTokensResponseB9Z7github.com/osmosis-labs/osmosis/v21/x/valset-pref/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.valsetpref.v1beta1.tx_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z7github.com/osmosis-labs/osmosis/v21/x/valset-pref/types'
    _globals['_MSGSETVALIDATORSETPREFERENCE'].fields_by_name['delegator']._options = None
    _globals['_MSGSETVALIDATORSETPREFERENCE'].fields_by_name['delegator']._serialized_options = b'\xf2\xde\x1f\x10yaml:"delegator"'
    _globals['_MSGSETVALIDATORSETPREFERENCE'].fields_by_name['preferences']._options = None
    _globals['_MSGSETVALIDATORSETPREFERENCE'].fields_by_name['preferences']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x12yaml:"preferences"'
    _globals['_MSGSETVALIDATORSETPREFERENCE']._options = None
    _globals['_MSGSETVALIDATORSETPREFERENCE']._serialized_options = b'\x8a\xe7\xb0*$osmosis/MsgSetValidatorSetPreference'
    _globals['_MSGDELEGATETOVALIDATORSET'].fields_by_name['delegator']._options = None
    _globals['_MSGDELEGATETOVALIDATORSET'].fields_by_name['delegator']._serialized_options = b'\xf2\xde\x1f\x10yaml:"delegator"'
    _globals['_MSGDELEGATETOVALIDATORSET'].fields_by_name['coin']._options = None
    _globals['_MSGDELEGATETOVALIDATORSET'].fields_by_name['coin']._serialized_options = b"\xc8\xde\x1f\x00\xaa\xdf\x1f'github.com/cosmos/cosmos-sdk/types.Coin"
    _globals['_MSGDELEGATETOVALIDATORSET']._options = None
    _globals['_MSGDELEGATETOVALIDATORSET']._serialized_options = b'\x8a\xe7\xb0*!osmosis/MsgDelegateToValidatorSet'
    _globals['_MSGUNDELEGATEFROMVALIDATORSET'].fields_by_name['delegator']._options = None
    _globals['_MSGUNDELEGATEFROMVALIDATORSET'].fields_by_name['delegator']._serialized_options = b'\xf2\xde\x1f\x10yaml:"delegator"'
    _globals['_MSGUNDELEGATEFROMVALIDATORSET'].fields_by_name['coin']._options = None
    _globals['_MSGUNDELEGATEFROMVALIDATORSET'].fields_by_name['coin']._serialized_options = b"\xc8\xde\x1f\x00\xaa\xdf\x1f'github.com/cosmos/cosmos-sdk/types.Coin"
    _globals['_MSGUNDELEGATEFROMVALIDATORSET']._options = None
    _globals['_MSGUNDELEGATEFROMVALIDATORSET']._serialized_options = b'\x8a\xe7\xb0*%osmosis/MsgUndelegateFromValidatorSet'
    _globals['_MSGUNDELEGATEFROMREBALANCEDVALIDATORSET'].fields_by_name['delegator']._options = None
    _globals['_MSGUNDELEGATEFROMREBALANCEDVALIDATORSET'].fields_by_name['delegator']._serialized_options = b'\xf2\xde\x1f\x10yaml:"delegator"'
    _globals['_MSGUNDELEGATEFROMREBALANCEDVALIDATORSET'].fields_by_name['coin']._options = None
    _globals['_MSGUNDELEGATEFROMREBALANCEDVALIDATORSET'].fields_by_name['coin']._serialized_options = b"\xc8\xde\x1f\x00\xaa\xdf\x1f'github.com/cosmos/cosmos-sdk/types.Coin"
    _globals['_MSGUNDELEGATEFROMREBALANCEDVALIDATORSET']._options = None
    _globals['_MSGUNDELEGATEFROMREBALANCEDVALIDATORSET']._serialized_options = b'\x8a\xe7\xb0*$osmosis/MsgUndelegateFromRebalValset'
    _globals['_MSGREDELEGATEVALIDATORSET'].fields_by_name['delegator']._options = None
    _globals['_MSGREDELEGATEVALIDATORSET'].fields_by_name['delegator']._serialized_options = b'\xf2\xde\x1f\x10yaml:"delegator"'
    _globals['_MSGREDELEGATEVALIDATORSET'].fields_by_name['preferences']._options = None
    _globals['_MSGREDELEGATEVALIDATORSET'].fields_by_name['preferences']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x12yaml:"preferences"'
    _globals['_MSGREDELEGATEVALIDATORSET']._options = None
    _globals['_MSGREDELEGATEVALIDATORSET']._serialized_options = b'\x8a\xe7\xb0*!osmosis/MsgRedelegateValidatorSet'
    _globals['_MSGWITHDRAWDELEGATIONREWARDS'].fields_by_name['delegator']._options = None
    _globals['_MSGWITHDRAWDELEGATIONREWARDS'].fields_by_name['delegator']._serialized_options = b'\xf2\xde\x1f\x10yaml:"delegator"'
    _globals['_MSGWITHDRAWDELEGATIONREWARDS']._options = None
    _globals['_MSGWITHDRAWDELEGATIONREWARDS']._serialized_options = b'\x8a\xe7\xb0*$osmosis/MsgWithdrawDelegationRewards'
    _globals['_MSGDELEGATEBONDEDTOKENS'].fields_by_name['delegator']._options = None
    _globals['_MSGDELEGATEBONDEDTOKENS'].fields_by_name['delegator']._serialized_options = b'\xf2\xde\x1f\x10yaml:"delegator"'
    _globals['_MSGSETVALIDATORSETPREFERENCE']._serialized_start = 214
    _globals['_MSGSETVALIDATORSETPREFERENCE']._serialized_end = 426
    _globals['_MSGSETVALIDATORSETPREFERENCERESPONSE']._serialized_start = 428
    _globals['_MSGSETVALIDATORSETPREFERENCERESPONSE']._serialized_end = 466
    _globals['_MSGDELEGATETOVALIDATORSET']._serialized_start = 469
    _globals['_MSGDELEGATETOVALIDATORSET']._serialized_end = 667
    _globals['_MSGDELEGATETOVALIDATORSETRESPONSE']._serialized_start = 669
    _globals['_MSGDELEGATETOVALIDATORSETRESPONSE']._serialized_end = 704
    _globals['_MSGUNDELEGATEFROMVALIDATORSET']._serialized_start = 707
    _globals['_MSGUNDELEGATEFROMVALIDATORSET']._serialized_end = 913
    _globals['_MSGUNDELEGATEFROMVALIDATORSETRESPONSE']._serialized_start = 915
    _globals['_MSGUNDELEGATEFROMVALIDATORSETRESPONSE']._serialized_end = 954
    _globals['_MSGUNDELEGATEFROMREBALANCEDVALIDATORSET']._serialized_start = 957
    _globals['_MSGUNDELEGATEFROMREBALANCEDVALIDATORSET']._serialized_end = 1172
    _globals['_MSGUNDELEGATEFROMREBALANCEDVALIDATORSETRESPONSE']._serialized_start = 1174
    _globals['_MSGUNDELEGATEFROMREBALANCEDVALIDATORSETRESPONSE']._serialized_end = 1223
    _globals['_MSGREDELEGATEVALIDATORSET']._serialized_start = 1226
    _globals['_MSGREDELEGATEVALIDATORSET']._serialized_end = 1432
    _globals['_MSGREDELEGATEVALIDATORSETRESPONSE']._serialized_start = 1434
    _globals['_MSGREDELEGATEVALIDATORSETRESPONSE']._serialized_end = 1469
    _globals['_MSGWITHDRAWDELEGATIONREWARDS']._serialized_start = 1471
    _globals['_MSGWITHDRAWDELEGATIONREWARDS']._serialized_end = 1585
    _globals['_MSGWITHDRAWDELEGATIONREWARDSRESPONSE']._serialized_start = 1587
    _globals['_MSGWITHDRAWDELEGATIONREWARDSRESPONSE']._serialized_end = 1625
    _globals['_MSGDELEGATEBONDEDTOKENS']._serialized_start = 1627
    _globals['_MSGDELEGATEBONDEDTOKENS']._serialized_end = 1709
    _globals['_MSGDELEGATEBONDEDTOKENSRESPONSE']._serialized_start = 1711
    _globals['_MSGDELEGATEBONDEDTOKENSRESPONSE']._serialized_end = 1744
    _globals['_MSG']._serialized_start = 1747
    _globals['_MSG']._serialized_end = 2833
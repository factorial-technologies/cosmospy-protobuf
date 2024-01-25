"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ...cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ...google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ...osmosis.lockup import lock_pb2 as osmosis_dot_lockup_dot_lock__pb2
from ...osmosis.lockup import params_pb2 as osmosis_dot_lockup_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aosmosis/lockup/query.proto\x12\x0eosmosis.lockup\x1a\x14gogoproto/gogo.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x19osmosis/lockup/lock.proto\x1a\x1bosmosis/lockup/params.proto"\x16\n\x14ModuleBalanceRequest"s\n\x15ModuleBalanceResponse\x12Z\n\x05coins\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"\x1b\n\x19ModuleLockedAmountRequest"x\n\x1aModuleLockedAmountResponse\x12Z\n\x05coins\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"@\n\x1dAccountUnlockableCoinsRequest\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner""|\n\x1eAccountUnlockableCoinsResponse\x12Z\n\x05coins\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"?\n\x1cAccountUnlockingCoinsRequest\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner""{\n\x1dAccountUnlockingCoinsResponse\x12Z\n\x05coins\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"<\n\x19AccountLockedCoinsRequest\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner""x\n\x1aAccountLockedCoinsResponse\x12Z\n\x05coins\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"\x8c\x01\n\x1cAccountLockedPastTimeRequest\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner"\x12K\n\ttimestamp\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1c\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"timestamp"\x90\xdf\x1f\x01"P\n\x1dAccountLockedPastTimeResponse\x12/\n\x05locks\x18\x01 \x03(\x0b2\x1a.osmosis.lockup.PeriodLockB\x04\xc8\xde\x1f\x00"\x9c\x01\n,AccountLockedPastTimeNotUnlockingOnlyRequest\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner"\x12K\n\ttimestamp\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1c\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"timestamp"\x90\xdf\x1f\x01"`\n-AccountLockedPastTimeNotUnlockingOnlyResponse\x12/\n\x05locks\x18\x01 \x03(\x0b2\x1a.osmosis.lockup.PeriodLockB\x04\xc8\xde\x1f\x00"\x90\x01\n AccountUnlockedBeforeTimeRequest\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner"\x12K\n\ttimestamp\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1c\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"timestamp"\x90\xdf\x1f\x01"T\n!AccountUnlockedBeforeTimeResponse\x12/\n\x05locks\x18\x01 \x03(\x0b2\x1a.osmosis.lockup.PeriodLockB\x04\xc8\xde\x1f\x00"\xa0\x01\n!AccountLockedPastTimeDenomRequest\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner"\x12K\n\ttimestamp\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x1c\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"timestamp"\x90\xdf\x1f\x01\x12\r\n\x05denom\x18\x03 \x01(\t"U\n"AccountLockedPastTimeDenomResponse\x12/\n\x05locks\x18\x01 \x03(\x0b2\x1a.osmosis.lockup.PeriodLockB\x04\xc8\xde\x1f\x00"m\n\x12LockedDenomRequest\x12\r\n\x05denom\x18\x01 \x01(\t\x12H\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x1b\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"duration"\x98\xdf\x1f\x01"U\n\x13LockedDenomResponse\x12>\n\x06amount\x18\x01 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int\xf2\xde\x1f\ryaml:"amount"" \n\rLockedRequest\x12\x0f\n\x07lock_id\x18\x01 \x01(\x04":\n\x0eLockedResponse\x12(\n\x04lock\x18\x01 \x01(\x0b2\x1a.osmosis.lockup.PeriodLock",\n\x19LockRewardReceiverRequest\x12\x0f\n\x07lock_id\x18\x01 \x01(\x04"5\n\x1aLockRewardReceiverResponse\x12\x17\n\x0freward_receiver\x18\x01 \x01(\t"\x13\n\x11NextLockIDRequest"%\n\x12NextLockIDResponse\x12\x0f\n\x07lock_id\x18\x01 \x01(\x04"8\n!SyntheticLockupsByLockupIDRequest\x12\x0f\n\x07lock_id\x18\x01 \x01(\x04:\x02\x18\x01"f\n"SyntheticLockupsByLockupIDResponse\x12<\n\x0fsynthetic_locks\x18\x01 \x03(\x0b2\x1d.osmosis.lockup.SyntheticLockB\x04\xc8\xde\x1f\x00:\x02\x18\x01"3\n SyntheticLockupByLockupIDRequest\x12\x0f\n\x07lock_id\x18\x01 \x01(\x04"`\n!SyntheticLockupByLockupIDResponse\x12;\n\x0esynthetic_lock\x18\x01 \x01(\x0b2\x1d.osmosis.lockup.SyntheticLockB\x04\xc8\xde\x1f\x00"\x8f\x01\n"AccountLockedLongerDurationRequest\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner"\x12H\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x1b\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"duration"\x98\xdf\x1f\x01"V\n#AccountLockedLongerDurationResponse\x12/\n\x05locks\x18\x01 \x03(\x0b2\x1a.osmosis.lockup.PeriodLockB\x04\xc8\xde\x1f\x00"\x89\x01\n\x1cAccountLockedDurationRequest\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner"\x12H\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x1b\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"duration"\x98\xdf\x1f\x01"P\n\x1dAccountLockedDurationResponse\x12/\n\x05locks\x18\x01 \x03(\x0b2\x1a.osmosis.lockup.PeriodLockB\x04\xc8\xde\x1f\x00"\x9f\x01\n2AccountLockedLongerDurationNotUnlockingOnlyRequest\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner"\x12H\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x1b\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"duration"\x98\xdf\x1f\x01"f\n3AccountLockedLongerDurationNotUnlockingOnlyResponse\x12/\n\x05locks\x18\x01 \x03(\x0b2\x1a.osmosis.lockup.PeriodLockB\x04\xc8\xde\x1f\x00"\xa3\x01\n\'AccountLockedLongerDurationDenomRequest\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner"\x12H\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x1b\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"duration"\x98\xdf\x1f\x01\x12\r\n\x05denom\x18\x03 \x01(\t"[\n(AccountLockedLongerDurationDenomResponse\x12/\n\x05locks\x18\x01 \x03(\x0b2\x1a.osmosis.lockup.PeriodLockB\x04\xc8\xde\x1f\x00"\x14\n\x12QueryParamsRequest"C\n\x13QueryParamsResponse\x12,\n\x06params\x18\x01 \x01(\x0b2\x16.osmosis.lockup.ParamsB\x04\xc8\xde\x1f\x002\xfb\x1c\n\x05Query\x12\x8c\x01\n\rModuleBalance\x12$.osmosis.lockup.ModuleBalanceRequest\x1a%.osmosis.lockup.ModuleBalanceResponse".\x82\xd3\xe4\x93\x02(\x12&/osmosis/lockup/v1beta1/module_balance\x12\xa1\x01\n\x12ModuleLockedAmount\x12).osmosis.lockup.ModuleLockedAmountRequest\x1a*.osmosis.lockup.ModuleLockedAmountResponse"4\x82\xd3\xe4\x93\x02.\x12,/osmosis/lockup/v1beta1/module_locked_amount\x12\xb9\x01\n\x16AccountUnlockableCoins\x12-.osmosis.lockup.AccountUnlockableCoinsRequest\x1a..osmosis.lockup.AccountUnlockableCoinsResponse"@\x82\xd3\xe4\x93\x02:\x128/osmosis/lockup/v1beta1/account_unlockable_coins/{owner}\x12\xb5\x01\n\x15AccountUnlockingCoins\x12,.osmosis.lockup.AccountUnlockingCoinsRequest\x1a-.osmosis.lockup.AccountUnlockingCoinsResponse"?\x82\xd3\xe4\x93\x029\x127/osmosis/lockup/v1beta1/account_unlocking_coins/{owner}\x12\xa9\x01\n\x12AccountLockedCoins\x12).osmosis.lockup.AccountLockedCoinsRequest\x1a*.osmosis.lockup.AccountLockedCoinsResponse"<\x82\xd3\xe4\x93\x026\x124/osmosis/lockup/v1beta1/account_locked_coins/{owner}\x12\xb5\x01\n\x15AccountLockedPastTime\x12,.osmosis.lockup.AccountLockedPastTimeRequest\x1a-.osmosis.lockup.AccountLockedPastTimeResponse"?\x82\xd3\xe4\x93\x029\x127/osmosis/lockup/v1beta1/account_locked_pasttime/{owner}\x12\xf8\x01\n%AccountLockedPastTimeNotUnlockingOnly\x12<.osmosis.lockup.AccountLockedPastTimeNotUnlockingOnlyRequest\x1a=.osmosis.lockup.AccountLockedPastTimeNotUnlockingOnlyResponse"R\x82\xd3\xe4\x93\x02L\x12J/osmosis/lockup/v1beta1/account_locked_pasttime_not_unlocking_only/{owner}\x12\xc6\x01\n\x19AccountUnlockedBeforeTime\x120.osmosis.lockup.AccountUnlockedBeforeTimeRequest\x1a1.osmosis.lockup.AccountUnlockedBeforeTimeResponse"D\x82\xd3\xe4\x93\x02>\x12</osmosis/lockup/v1beta1/account_unlocked_before_time/{owner}\x12\xca\x01\n\x1aAccountLockedPastTimeDenom\x121.osmosis.lockup.AccountLockedPastTimeDenomRequest\x1a2.osmosis.lockup.AccountLockedPastTimeDenomResponse"E\x82\xd3\xe4\x93\x02?\x12=/osmosis/lockup/v1beta1/account_locked_pasttime_denom/{owner}\x12\x84\x01\n\x0bLockedDenom\x12".osmosis.lockup.LockedDenomRequest\x1a#.osmosis.lockup.LockedDenomResponse",\x82\xd3\xe4\x93\x02&\x12$/osmosis/lockup/v1beta1/locked_denom\x12\x83\x01\n\nLockedByID\x12\x1d.osmosis.lockup.LockedRequest\x1a\x1e.osmosis.lockup.LockedResponse"6\x82\xd3\xe4\x93\x020\x12./osmosis/lockup/v1beta1/locked_by_id/{lock_id}\x12\xab\x01\n\x12LockRewardReceiver\x12).osmosis.lockup.LockRewardReceiverRequest\x1a*.osmosis.lockup.LockRewardReceiverResponse">\x82\xd3\xe4\x93\x028\x126/osmosis/lockup/v1beta1/lock_reward_receiver/{lock_id}\x12\x81\x01\n\nNextLockID\x12!.osmosis.lockup.NextLockIDRequest\x1a".osmosis.lockup.NextLockIDResponse",\x82\xd3\xe4\x93\x02&\x12$/osmosis/lockup/v1beta1/next_lock_id\x12\xce\x01\n\x1aSyntheticLockupsByLockupID\x121.osmosis.lockup.SyntheticLockupsByLockupIDRequest\x1a2.osmosis.lockup.SyntheticLockupsByLockupIDResponse"I\x88\x02\x01\x82\xd3\xe4\x93\x02@\x12>/osmosis/lockup/v1beta1/synthetic_lockups_by_lock_id/{lock_id}\x12\xc7\x01\n\x19SyntheticLockupByLockupID\x120.osmosis.lockup.SyntheticLockupByLockupIDRequest\x1a1.osmosis.lockup.SyntheticLockupByLockupIDResponse"E\x82\xd3\xe4\x93\x02?\x12=/osmosis/lockup/v1beta1/synthetic_lockup_by_lock_id/{lock_id}\x12\xce\x01\n\x1bAccountLockedLongerDuration\x122.osmosis.lockup.AccountLockedLongerDurationRequest\x1a3.osmosis.lockup.AccountLockedLongerDurationResponse"F\x82\xd3\xe4\x93\x02@\x12>/osmosis/lockup/v1beta1/account_locked_longer_duration/{owner}\x12\xb5\x01\n\x15AccountLockedDuration\x12,.osmosis.lockup.AccountLockedDurationRequest\x1a-.osmosis.lockup.AccountLockedDurationResponse"?\x82\xd3\xe4\x93\x029\x127/osmosis/lockup/v1beta1/account_locked_duration/{owner}\x12\x91\x02\n+AccountLockedLongerDurationNotUnlockingOnly\x12B.osmosis.lockup.AccountLockedLongerDurationNotUnlockingOnlyRequest\x1aC.osmosis.lockup.AccountLockedLongerDurationNotUnlockingOnlyResponse"Y\x82\xd3\xe4\x93\x02S\x12Q/osmosis/lockup/v1beta1/account_locked_longer_duration_not_unlocking_only/{owner}\x12\xe3\x01\n AccountLockedLongerDurationDenom\x127.osmosis.lockup.AccountLockedLongerDurationDenomRequest\x1a8.osmosis.lockup.AccountLockedLongerDurationDenomResponse"L\x82\xd3\xe4\x93\x02F\x12D/osmosis/lockup/v1beta1/account_locked_longer_duration_denom/{owner}\x12y\n\x06Params\x12".osmosis.lockup.QueryParamsRequest\x1a#.osmosis.lockup.QueryParamsResponse"&\x82\xd3\xe4\x93\x02 \x12\x1e/osmosis/lockup/v1beta1/paramsB4Z2github.com/osmosis-labs/osmosis/v21/x/lockup/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.lockup.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z2github.com/osmosis-labs/osmosis/v21/x/lockup/types'
    _globals['_MODULEBALANCERESPONSE'].fields_by_name['coins']._options = None
    _globals['_MODULEBALANCERESPONSE'].fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_MODULELOCKEDAMOUNTRESPONSE'].fields_by_name['coins']._options = None
    _globals['_MODULELOCKEDAMOUNTRESPONSE'].fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_ACCOUNTUNLOCKABLECOINSREQUEST'].fields_by_name['owner']._options = None
    _globals['_ACCOUNTUNLOCKABLECOINSREQUEST'].fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _globals['_ACCOUNTUNLOCKABLECOINSRESPONSE'].fields_by_name['coins']._options = None
    _globals['_ACCOUNTUNLOCKABLECOINSRESPONSE'].fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_ACCOUNTUNLOCKINGCOINSREQUEST'].fields_by_name['owner']._options = None
    _globals['_ACCOUNTUNLOCKINGCOINSREQUEST'].fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _globals['_ACCOUNTUNLOCKINGCOINSRESPONSE'].fields_by_name['coins']._options = None
    _globals['_ACCOUNTUNLOCKINGCOINSRESPONSE'].fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_ACCOUNTLOCKEDCOINSREQUEST'].fields_by_name['owner']._options = None
    _globals['_ACCOUNTLOCKEDCOINSREQUEST'].fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _globals['_ACCOUNTLOCKEDCOINSRESPONSE'].fields_by_name['coins']._options = None
    _globals['_ACCOUNTLOCKEDCOINSRESPONSE'].fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_ACCOUNTLOCKEDPASTTIMEREQUEST'].fields_by_name['owner']._options = None
    _globals['_ACCOUNTLOCKEDPASTTIMEREQUEST'].fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _globals['_ACCOUNTLOCKEDPASTTIMEREQUEST'].fields_by_name['timestamp']._options = None
    _globals['_ACCOUNTLOCKEDPASTTIMEREQUEST'].fields_by_name['timestamp']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"timestamp"\x90\xdf\x1f\x01'
    _globals['_ACCOUNTLOCKEDPASTTIMERESPONSE'].fields_by_name['locks']._options = None
    _globals['_ACCOUNTLOCKEDPASTTIMERESPONSE'].fields_by_name['locks']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_ACCOUNTLOCKEDPASTTIMENOTUNLOCKINGONLYREQUEST'].fields_by_name['owner']._options = None
    _globals['_ACCOUNTLOCKEDPASTTIMENOTUNLOCKINGONLYREQUEST'].fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _globals['_ACCOUNTLOCKEDPASTTIMENOTUNLOCKINGONLYREQUEST'].fields_by_name['timestamp']._options = None
    _globals['_ACCOUNTLOCKEDPASTTIMENOTUNLOCKINGONLYREQUEST'].fields_by_name['timestamp']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"timestamp"\x90\xdf\x1f\x01'
    _globals['_ACCOUNTLOCKEDPASTTIMENOTUNLOCKINGONLYRESPONSE'].fields_by_name['locks']._options = None
    _globals['_ACCOUNTLOCKEDPASTTIMENOTUNLOCKINGONLYRESPONSE'].fields_by_name['locks']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_ACCOUNTUNLOCKEDBEFORETIMEREQUEST'].fields_by_name['owner']._options = None
    _globals['_ACCOUNTUNLOCKEDBEFORETIMEREQUEST'].fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _globals['_ACCOUNTUNLOCKEDBEFORETIMEREQUEST'].fields_by_name['timestamp']._options = None
    _globals['_ACCOUNTUNLOCKEDBEFORETIMEREQUEST'].fields_by_name['timestamp']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"timestamp"\x90\xdf\x1f\x01'
    _globals['_ACCOUNTUNLOCKEDBEFORETIMERESPONSE'].fields_by_name['locks']._options = None
    _globals['_ACCOUNTUNLOCKEDBEFORETIMERESPONSE'].fields_by_name['locks']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_ACCOUNTLOCKEDPASTTIMEDENOMREQUEST'].fields_by_name['owner']._options = None
    _globals['_ACCOUNTLOCKEDPASTTIMEDENOMREQUEST'].fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _globals['_ACCOUNTLOCKEDPASTTIMEDENOMREQUEST'].fields_by_name['timestamp']._options = None
    _globals['_ACCOUNTLOCKEDPASTTIMEDENOMREQUEST'].fields_by_name['timestamp']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"timestamp"\x90\xdf\x1f\x01'
    _globals['_ACCOUNTLOCKEDPASTTIMEDENOMRESPONSE'].fields_by_name['locks']._options = None
    _globals['_ACCOUNTLOCKEDPASTTIMEDENOMRESPONSE'].fields_by_name['locks']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_LOCKEDDENOMREQUEST'].fields_by_name['duration']._options = None
    _globals['_LOCKEDDENOMREQUEST'].fields_by_name['duration']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"duration"\x98\xdf\x1f\x01'
    _globals['_LOCKEDDENOMRESPONSE'].fields_by_name['amount']._options = None
    _globals['_LOCKEDDENOMRESPONSE'].fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int\xf2\xde\x1f\ryaml:"amount"'
    _globals['_SYNTHETICLOCKUPSBYLOCKUPIDREQUEST']._options = None
    _globals['_SYNTHETICLOCKUPSBYLOCKUPIDREQUEST']._serialized_options = b'\x18\x01'
    _globals['_SYNTHETICLOCKUPSBYLOCKUPIDRESPONSE'].fields_by_name['synthetic_locks']._options = None
    _globals['_SYNTHETICLOCKUPSBYLOCKUPIDRESPONSE'].fields_by_name['synthetic_locks']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_SYNTHETICLOCKUPSBYLOCKUPIDRESPONSE']._options = None
    _globals['_SYNTHETICLOCKUPSBYLOCKUPIDRESPONSE']._serialized_options = b'\x18\x01'
    _globals['_SYNTHETICLOCKUPBYLOCKUPIDRESPONSE'].fields_by_name['synthetic_lock']._options = None
    _globals['_SYNTHETICLOCKUPBYLOCKUPIDRESPONSE'].fields_by_name['synthetic_lock']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_ACCOUNTLOCKEDLONGERDURATIONREQUEST'].fields_by_name['owner']._options = None
    _globals['_ACCOUNTLOCKEDLONGERDURATIONREQUEST'].fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _globals['_ACCOUNTLOCKEDLONGERDURATIONREQUEST'].fields_by_name['duration']._options = None
    _globals['_ACCOUNTLOCKEDLONGERDURATIONREQUEST'].fields_by_name['duration']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"duration"\x98\xdf\x1f\x01'
    _globals['_ACCOUNTLOCKEDLONGERDURATIONRESPONSE'].fields_by_name['locks']._options = None
    _globals['_ACCOUNTLOCKEDLONGERDURATIONRESPONSE'].fields_by_name['locks']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_ACCOUNTLOCKEDDURATIONREQUEST'].fields_by_name['owner']._options = None
    _globals['_ACCOUNTLOCKEDDURATIONREQUEST'].fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _globals['_ACCOUNTLOCKEDDURATIONREQUEST'].fields_by_name['duration']._options = None
    _globals['_ACCOUNTLOCKEDDURATIONREQUEST'].fields_by_name['duration']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"duration"\x98\xdf\x1f\x01'
    _globals['_ACCOUNTLOCKEDDURATIONRESPONSE'].fields_by_name['locks']._options = None
    _globals['_ACCOUNTLOCKEDDURATIONRESPONSE'].fields_by_name['locks']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_ACCOUNTLOCKEDLONGERDURATIONNOTUNLOCKINGONLYREQUEST'].fields_by_name['owner']._options = None
    _globals['_ACCOUNTLOCKEDLONGERDURATIONNOTUNLOCKINGONLYREQUEST'].fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _globals['_ACCOUNTLOCKEDLONGERDURATIONNOTUNLOCKINGONLYREQUEST'].fields_by_name['duration']._options = None
    _globals['_ACCOUNTLOCKEDLONGERDURATIONNOTUNLOCKINGONLYREQUEST'].fields_by_name['duration']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"duration"\x98\xdf\x1f\x01'
    _globals['_ACCOUNTLOCKEDLONGERDURATIONNOTUNLOCKINGONLYRESPONSE'].fields_by_name['locks']._options = None
    _globals['_ACCOUNTLOCKEDLONGERDURATIONNOTUNLOCKINGONLYRESPONSE'].fields_by_name['locks']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_ACCOUNTLOCKEDLONGERDURATIONDENOMREQUEST'].fields_by_name['owner']._options = None
    _globals['_ACCOUNTLOCKEDLONGERDURATIONDENOMREQUEST'].fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _globals['_ACCOUNTLOCKEDLONGERDURATIONDENOMREQUEST'].fields_by_name['duration']._options = None
    _globals['_ACCOUNTLOCKEDLONGERDURATIONDENOMREQUEST'].fields_by_name['duration']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x0fyaml:"duration"\x98\xdf\x1f\x01'
    _globals['_ACCOUNTLOCKEDLONGERDURATIONDENOMRESPONSE'].fields_by_name['locks']._options = None
    _globals['_ACCOUNTLOCKEDLONGERDURATIONDENOMRESPONSE'].fields_by_name['locks']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._options = None
    _globals['_QUERYPARAMSRESPONSE'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERY'].methods_by_name['ModuleBalance']._options = None
    _globals['_QUERY'].methods_by_name['ModuleBalance']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/osmosis/lockup/v1beta1/module_balance'
    _globals['_QUERY'].methods_by_name['ModuleLockedAmount']._options = None
    _globals['_QUERY'].methods_by_name['ModuleLockedAmount']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/osmosis/lockup/v1beta1/module_locked_amount'
    _globals['_QUERY'].methods_by_name['AccountUnlockableCoins']._options = None
    _globals['_QUERY'].methods_by_name['AccountUnlockableCoins']._serialized_options = b'\x82\xd3\xe4\x93\x02:\x128/osmosis/lockup/v1beta1/account_unlockable_coins/{owner}'
    _globals['_QUERY'].methods_by_name['AccountUnlockingCoins']._options = None
    _globals['_QUERY'].methods_by_name['AccountUnlockingCoins']._serialized_options = b'\x82\xd3\xe4\x93\x029\x127/osmosis/lockup/v1beta1/account_unlocking_coins/{owner}'
    _globals['_QUERY'].methods_by_name['AccountLockedCoins']._options = None
    _globals['_QUERY'].methods_by_name['AccountLockedCoins']._serialized_options = b'\x82\xd3\xe4\x93\x026\x124/osmosis/lockup/v1beta1/account_locked_coins/{owner}'
    _globals['_QUERY'].methods_by_name['AccountLockedPastTime']._options = None
    _globals['_QUERY'].methods_by_name['AccountLockedPastTime']._serialized_options = b'\x82\xd3\xe4\x93\x029\x127/osmosis/lockup/v1beta1/account_locked_pasttime/{owner}'
    _globals['_QUERY'].methods_by_name['AccountLockedPastTimeNotUnlockingOnly']._options = None
    _globals['_QUERY'].methods_by_name['AccountLockedPastTimeNotUnlockingOnly']._serialized_options = b'\x82\xd3\xe4\x93\x02L\x12J/osmosis/lockup/v1beta1/account_locked_pasttime_not_unlocking_only/{owner}'
    _globals['_QUERY'].methods_by_name['AccountUnlockedBeforeTime']._options = None
    _globals['_QUERY'].methods_by_name['AccountUnlockedBeforeTime']._serialized_options = b'\x82\xd3\xe4\x93\x02>\x12</osmosis/lockup/v1beta1/account_unlocked_before_time/{owner}'
    _globals['_QUERY'].methods_by_name['AccountLockedPastTimeDenom']._options = None
    _globals['_QUERY'].methods_by_name['AccountLockedPastTimeDenom']._serialized_options = b'\x82\xd3\xe4\x93\x02?\x12=/osmosis/lockup/v1beta1/account_locked_pasttime_denom/{owner}'
    _globals['_QUERY'].methods_by_name['LockedDenom']._options = None
    _globals['_QUERY'].methods_by_name['LockedDenom']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x12$/osmosis/lockup/v1beta1/locked_denom'
    _globals['_QUERY'].methods_by_name['LockedByID']._options = None
    _globals['_QUERY'].methods_by_name['LockedByID']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./osmosis/lockup/v1beta1/locked_by_id/{lock_id}'
    _globals['_QUERY'].methods_by_name['LockRewardReceiver']._options = None
    _globals['_QUERY'].methods_by_name['LockRewardReceiver']._serialized_options = b'\x82\xd3\xe4\x93\x028\x126/osmosis/lockup/v1beta1/lock_reward_receiver/{lock_id}'
    _globals['_QUERY'].methods_by_name['NextLockID']._options = None
    _globals['_QUERY'].methods_by_name['NextLockID']._serialized_options = b'\x82\xd3\xe4\x93\x02&\x12$/osmosis/lockup/v1beta1/next_lock_id'
    _globals['_QUERY'].methods_by_name['SyntheticLockupsByLockupID']._options = None
    _globals['_QUERY'].methods_by_name['SyntheticLockupsByLockupID']._serialized_options = b'\x88\x02\x01\x82\xd3\xe4\x93\x02@\x12>/osmosis/lockup/v1beta1/synthetic_lockups_by_lock_id/{lock_id}'
    _globals['_QUERY'].methods_by_name['SyntheticLockupByLockupID']._options = None
    _globals['_QUERY'].methods_by_name['SyntheticLockupByLockupID']._serialized_options = b'\x82\xd3\xe4\x93\x02?\x12=/osmosis/lockup/v1beta1/synthetic_lockup_by_lock_id/{lock_id}'
    _globals['_QUERY'].methods_by_name['AccountLockedLongerDuration']._options = None
    _globals['_QUERY'].methods_by_name['AccountLockedLongerDuration']._serialized_options = b'\x82\xd3\xe4\x93\x02@\x12>/osmosis/lockup/v1beta1/account_locked_longer_duration/{owner}'
    _globals['_QUERY'].methods_by_name['AccountLockedDuration']._options = None
    _globals['_QUERY'].methods_by_name['AccountLockedDuration']._serialized_options = b'\x82\xd3\xe4\x93\x029\x127/osmosis/lockup/v1beta1/account_locked_duration/{owner}'
    _globals['_QUERY'].methods_by_name['AccountLockedLongerDurationNotUnlockingOnly']._options = None
    _globals['_QUERY'].methods_by_name['AccountLockedLongerDurationNotUnlockingOnly']._serialized_options = b'\x82\xd3\xe4\x93\x02S\x12Q/osmosis/lockup/v1beta1/account_locked_longer_duration_not_unlocking_only/{owner}'
    _globals['_QUERY'].methods_by_name['AccountLockedLongerDurationDenom']._options = None
    _globals['_QUERY'].methods_by_name['AccountLockedLongerDurationDenom']._serialized_options = b'\x82\xd3\xe4\x93\x02F\x12D/osmosis/lockup/v1beta1/account_locked_longer_duration_denom/{owner}'
    _globals['_QUERY'].methods_by_name['Params']._options = None
    _globals['_QUERY'].methods_by_name['Params']._serialized_options = b'\x82\xd3\xe4\x93\x02 \x12\x1e/osmosis/lockup/v1beta1/params'
    _globals['_MODULEBALANCEREQUEST']._serialized_start = 251
    _globals['_MODULEBALANCEREQUEST']._serialized_end = 273
    _globals['_MODULEBALANCERESPONSE']._serialized_start = 275
    _globals['_MODULEBALANCERESPONSE']._serialized_end = 390
    _globals['_MODULELOCKEDAMOUNTREQUEST']._serialized_start = 392
    _globals['_MODULELOCKEDAMOUNTREQUEST']._serialized_end = 419
    _globals['_MODULELOCKEDAMOUNTRESPONSE']._serialized_start = 421
    _globals['_MODULELOCKEDAMOUNTRESPONSE']._serialized_end = 541
    _globals['_ACCOUNTUNLOCKABLECOINSREQUEST']._serialized_start = 543
    _globals['_ACCOUNTUNLOCKABLECOINSREQUEST']._serialized_end = 607
    _globals['_ACCOUNTUNLOCKABLECOINSRESPONSE']._serialized_start = 609
    _globals['_ACCOUNTUNLOCKABLECOINSRESPONSE']._serialized_end = 733
    _globals['_ACCOUNTUNLOCKINGCOINSREQUEST']._serialized_start = 735
    _globals['_ACCOUNTUNLOCKINGCOINSREQUEST']._serialized_end = 798
    _globals['_ACCOUNTUNLOCKINGCOINSRESPONSE']._serialized_start = 800
    _globals['_ACCOUNTUNLOCKINGCOINSRESPONSE']._serialized_end = 923
    _globals['_ACCOUNTLOCKEDCOINSREQUEST']._serialized_start = 925
    _globals['_ACCOUNTLOCKEDCOINSREQUEST']._serialized_end = 985
    _globals['_ACCOUNTLOCKEDCOINSRESPONSE']._serialized_start = 987
    _globals['_ACCOUNTLOCKEDCOINSRESPONSE']._serialized_end = 1107
    _globals['_ACCOUNTLOCKEDPASTTIMEREQUEST']._serialized_start = 1110
    _globals['_ACCOUNTLOCKEDPASTTIMEREQUEST']._serialized_end = 1250
    _globals['_ACCOUNTLOCKEDPASTTIMERESPONSE']._serialized_start = 1252
    _globals['_ACCOUNTLOCKEDPASTTIMERESPONSE']._serialized_end = 1332
    _globals['_ACCOUNTLOCKEDPASTTIMENOTUNLOCKINGONLYREQUEST']._serialized_start = 1335
    _globals['_ACCOUNTLOCKEDPASTTIMENOTUNLOCKINGONLYREQUEST']._serialized_end = 1491
    _globals['_ACCOUNTLOCKEDPASTTIMENOTUNLOCKINGONLYRESPONSE']._serialized_start = 1493
    _globals['_ACCOUNTLOCKEDPASTTIMENOTUNLOCKINGONLYRESPONSE']._serialized_end = 1589
    _globals['_ACCOUNTUNLOCKEDBEFORETIMEREQUEST']._serialized_start = 1592
    _globals['_ACCOUNTUNLOCKEDBEFORETIMEREQUEST']._serialized_end = 1736
    _globals['_ACCOUNTUNLOCKEDBEFORETIMERESPONSE']._serialized_start = 1738
    _globals['_ACCOUNTUNLOCKEDBEFORETIMERESPONSE']._serialized_end = 1822
    _globals['_ACCOUNTLOCKEDPASTTIMEDENOMREQUEST']._serialized_start = 1825
    _globals['_ACCOUNTLOCKEDPASTTIMEDENOMREQUEST']._serialized_end = 1985
    _globals['_ACCOUNTLOCKEDPASTTIMEDENOMRESPONSE']._serialized_start = 1987
    _globals['_ACCOUNTLOCKEDPASTTIMEDENOMRESPONSE']._serialized_end = 2072
    _globals['_LOCKEDDENOMREQUEST']._serialized_start = 2074
    _globals['_LOCKEDDENOMREQUEST']._serialized_end = 2183
    _globals['_LOCKEDDENOMRESPONSE']._serialized_start = 2185
    _globals['_LOCKEDDENOMRESPONSE']._serialized_end = 2270
    _globals['_LOCKEDREQUEST']._serialized_start = 2272
    _globals['_LOCKEDREQUEST']._serialized_end = 2304
    _globals['_LOCKEDRESPONSE']._serialized_start = 2306
    _globals['_LOCKEDRESPONSE']._serialized_end = 2364
    _globals['_LOCKREWARDRECEIVERREQUEST']._serialized_start = 2366
    _globals['_LOCKREWARDRECEIVERREQUEST']._serialized_end = 2410
    _globals['_LOCKREWARDRECEIVERRESPONSE']._serialized_start = 2412
    _globals['_LOCKREWARDRECEIVERRESPONSE']._serialized_end = 2465
    _globals['_NEXTLOCKIDREQUEST']._serialized_start = 2467
    _globals['_NEXTLOCKIDREQUEST']._serialized_end = 2486
    _globals['_NEXTLOCKIDRESPONSE']._serialized_start = 2488
    _globals['_NEXTLOCKIDRESPONSE']._serialized_end = 2525
    _globals['_SYNTHETICLOCKUPSBYLOCKUPIDREQUEST']._serialized_start = 2527
    _globals['_SYNTHETICLOCKUPSBYLOCKUPIDREQUEST']._serialized_end = 2583
    _globals['_SYNTHETICLOCKUPSBYLOCKUPIDRESPONSE']._serialized_start = 2585
    _globals['_SYNTHETICLOCKUPSBYLOCKUPIDRESPONSE']._serialized_end = 2687
    _globals['_SYNTHETICLOCKUPBYLOCKUPIDREQUEST']._serialized_start = 2689
    _globals['_SYNTHETICLOCKUPBYLOCKUPIDREQUEST']._serialized_end = 2740
    _globals['_SYNTHETICLOCKUPBYLOCKUPIDRESPONSE']._serialized_start = 2742
    _globals['_SYNTHETICLOCKUPBYLOCKUPIDRESPONSE']._serialized_end = 2838
    _globals['_ACCOUNTLOCKEDLONGERDURATIONREQUEST']._serialized_start = 2841
    _globals['_ACCOUNTLOCKEDLONGERDURATIONREQUEST']._serialized_end = 2984
    _globals['_ACCOUNTLOCKEDLONGERDURATIONRESPONSE']._serialized_start = 2986
    _globals['_ACCOUNTLOCKEDLONGERDURATIONRESPONSE']._serialized_end = 3072
    _globals['_ACCOUNTLOCKEDDURATIONREQUEST']._serialized_start = 3075
    _globals['_ACCOUNTLOCKEDDURATIONREQUEST']._serialized_end = 3212
    _globals['_ACCOUNTLOCKEDDURATIONRESPONSE']._serialized_start = 3214
    _globals['_ACCOUNTLOCKEDDURATIONRESPONSE']._serialized_end = 3294
    _globals['_ACCOUNTLOCKEDLONGERDURATIONNOTUNLOCKINGONLYREQUEST']._serialized_start = 3297
    _globals['_ACCOUNTLOCKEDLONGERDURATIONNOTUNLOCKINGONLYREQUEST']._serialized_end = 3456
    _globals['_ACCOUNTLOCKEDLONGERDURATIONNOTUNLOCKINGONLYRESPONSE']._serialized_start = 3458
    _globals['_ACCOUNTLOCKEDLONGERDURATIONNOTUNLOCKINGONLYRESPONSE']._serialized_end = 3560
    _globals['_ACCOUNTLOCKEDLONGERDURATIONDENOMREQUEST']._serialized_start = 3563
    _globals['_ACCOUNTLOCKEDLONGERDURATIONDENOMREQUEST']._serialized_end = 3726
    _globals['_ACCOUNTLOCKEDLONGERDURATIONDENOMRESPONSE']._serialized_start = 3728
    _globals['_ACCOUNTLOCKEDLONGERDURATIONDENOMRESPONSE']._serialized_end = 3819
    _globals['_QUERYPARAMSREQUEST']._serialized_start = 3821
    _globals['_QUERYPARAMSREQUEST']._serialized_end = 3841
    _globals['_QUERYPARAMSRESPONSE']._serialized_start = 3843
    _globals['_QUERYPARAMSRESPONSE']._serialized_end = 3910
    _globals['_QUERY']._serialized_start = 3913
    _globals['_QUERY']._serialized_end = 7620
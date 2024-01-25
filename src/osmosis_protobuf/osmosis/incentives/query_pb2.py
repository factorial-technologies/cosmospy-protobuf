"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ...google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ...cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ...cosmos.base.query.v1beta1 import pagination_pb2 as cosmos_dot_base_dot_query_dot_v1beta1_dot_pagination__pb2
from ...osmosis.incentives import gauge_pb2 as osmosis_dot_incentives_dot_gauge__pb2
from ...osmosis.lockup import lock_pb2 as osmosis_dot_lockup_dot_lock__pb2
from ...osmosis.incentives import group_pb2 as osmosis_dot_incentives_dot_group__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eosmosis/incentives/query.proto\x12\x12osmosis.incentives\x1a\x14gogoproto/gogo.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a*cosmos/base/query/v1beta1/pagination.proto\x1a\x1eosmosis/incentives/gauge.proto\x1a\x19osmosis/lockup/lock.proto\x1a\x1eosmosis/incentives/group.proto" \n\x1eModuleToDistributeCoinsRequest"}\n\x1fModuleToDistributeCoinsResponse\x12Z\n\x05coins\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"\x1e\n\x10GaugeByIDRequest\x12\n\n\x02id\x18\x01 \x01(\x04"=\n\x11GaugeByIDResponse\x12(\n\x05gauge\x18\x01 \x01(\x0b2\x19.osmosis.incentives.Gauge"K\n\rGaugesRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"|\n\x0eGaugesResponse\x12-\n\x04data\x18\x01 \x03(\x0b2\x19.osmosis.incentives.GaugeB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"Q\n\x13ActiveGaugesRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x82\x01\n\x14ActiveGaugesResponse\x12-\n\x04data\x18\x01 \x03(\x0b2\x19.osmosis.incentives.GaugeB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"h\n\x1bActiveGaugesPerDenomRequest\x12\r\n\x05denom\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x8a\x01\n\x1cActiveGaugesPerDenomResponse\x12-\n\x04data\x18\x01 \x03(\x0b2\x19.osmosis.incentives.GaugeB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"S\n\x15UpcomingGaugesRequest\x12:\n\npagination\x18\x01 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x84\x01\n\x16UpcomingGaugesResponse\x12-\n\x04data\x18\x01 \x03(\x0b2\x19.osmosis.incentives.GaugeB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"j\n\x1dUpcomingGaugesPerDenomRequest\x12\r\n\x05denom\x18\x01 \x01(\t\x12:\n\npagination\x18\x02 \x01(\x0b2&.cosmos.base.query.v1beta1.PageRequest"\x97\x01\n\x1eUpcomingGaugesPerDenomResponse\x128\n\x0fupcoming_gauges\x18\x01 \x03(\x0b2\x19.osmosis.incentives.GaugeB\x04\xc8\xde\x1f\x00\x12;\n\npagination\x18\x02 \x01(\x0b2\'.cosmos.base.query.v1beta1.PageResponse"Y\n\x11RewardsEstRequest\x12\x1f\n\x05owner\x18\x01 \x01(\tB\x10\xf2\xde\x1f\x0cyaml:"owner"\x12\x10\n\x08lock_ids\x18\x02 \x03(\x04\x12\x11\n\tend_epoch\x18\x03 \x01(\x03"p\n\x12RewardsEstResponse\x12Z\n\x05coins\x18\x01 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"\x1f\n\x1dQueryLockableDurationsRequest"~\n\x1eQueryLockableDurationsResponse\x12\\\n\x12lockable_durations\x18\x01 \x03(\x0b2\x19.google.protobuf.DurationB%\xc8\xde\x1f\x00\xf2\xde\x1f\x19yaml:"lockable_durations"\x98\xdf\x1f\x01"\x17\n\x15QueryAllGroupsRequest"I\n\x16QueryAllGroupsResponse\x12/\n\x06groups\x18\x01 \x03(\x0b2\x19.osmosis.incentives.GroupB\x04\xc8\xde\x1f\x00"\x1d\n\x1bQueryAllGroupsGaugesRequest"O\n\x1cQueryAllGroupsGaugesResponse\x12/\n\x06gauges\x18\x01 \x03(\x0b2\x19.osmosis.incentives.GaugeB\x04\xc8\xde\x1f\x00" \n\x1eQueryAllGroupsWithGaugeRequest"g\n\x1fQueryAllGroupsWithGaugeResponse\x12D\n\x11groups_with_gauge\x18\x01 \x03(\x0b2#.osmosis.incentives.GroupsWithGaugeB\x04\xc8\xde\x1f\x00"-\n\x1fQueryGroupByGroupGaugeIDRequest\x12\n\n\x02id\x18\x01 \x01(\x04"R\n QueryGroupByGroupGaugeIDResponse\x12.\n\x05group\x18\x01 \x01(\x0b2\x19.osmosis.incentives.GroupB\x04\xc8\xde\x1f\x00"A\n\'QueryCurrentWeightByGroupGaugeIDRequest\x12\x16\n\x0egroup_gauge_id\x18\x01 \x01(\x04"g\n(QueryCurrentWeightByGroupGaugeIDResponse\x12;\n\x0cgauge_weight\x18\x01 \x03(\x0b2\x1f.osmosis.incentives.GaugeWeightB\x04\xc8\xde\x1f\x00"q\n\x0bGaugeWeight\x12\x10\n\x08gauge_id\x18\x01 \x01(\x04\x12P\n\x0cweight_ratio\x18\x02 \x01(\tB:\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xf2\xde\x1f\x13yaml:"weight_ratio"2\x8b\x13\n\x05Query\x12\xc2\x01\n\x17ModuleToDistributeCoins\x122.osmosis.incentives.ModuleToDistributeCoinsRequest\x1a3.osmosis.incentives.ModuleToDistributeCoinsResponse">\x82\xd3\xe4\x93\x028\x126/osmosis/incentives/v1beta1/module_to_distribute_coins\x12\x8e\x01\n\tGaugeByID\x12$.osmosis.incentives.GaugeByIDRequest\x1a%.osmosis.incentives.GaugeByIDResponse"4\x82\xd3\xe4\x93\x02.\x12,/osmosis/incentives/v1beta1/gauge_by_id/{id}\x12{\n\x06Gauges\x12!.osmosis.incentives.GaugesRequest\x1a".osmosis.incentives.GaugesResponse"*\x82\xd3\xe4\x93\x02$\x12"/osmosis/incentives/v1beta1/gauges\x12\x94\x01\n\x0cActiveGauges\x12\'.osmosis.incentives.ActiveGaugesRequest\x1a(.osmosis.incentives.ActiveGaugesResponse"1\x82\xd3\xe4\x93\x02+\x12)/osmosis/incentives/v1beta1/active_gauges\x12\xb6\x01\n\x14ActiveGaugesPerDenom\x12/.osmosis.incentives.ActiveGaugesPerDenomRequest\x1a0.osmosis.incentives.ActiveGaugesPerDenomResponse";\x82\xd3\xe4\x93\x025\x123/osmosis/incentives/v1beta1/active_gauges_per_denom\x12\x9c\x01\n\x0eUpcomingGauges\x12).osmosis.incentives.UpcomingGaugesRequest\x1a*.osmosis.incentives.UpcomingGaugesResponse"3\x82\xd3\xe4\x93\x02-\x12+/osmosis/incentives/v1beta1/upcoming_gauges\x12\xbe\x01\n\x16UpcomingGaugesPerDenom\x121.osmosis.incentives.UpcomingGaugesPerDenomRequest\x1a2.osmosis.incentives.UpcomingGaugesPerDenomResponse"=\x82\xd3\xe4\x93\x027\x125/osmosis/incentives/v1beta1/upcoming_gauges_per_denom\x12\x94\x01\n\nRewardsEst\x12%.osmosis.incentives.RewardsEstRequest\x1a&.osmosis.incentives.RewardsEstResponse"7\x82\xd3\xe4\x93\x021\x12//osmosis/incentives/v1beta1/rewards_est/{owner}\x12\xb2\x01\n\x11LockableDurations\x121.osmosis.incentives.QueryLockableDurationsRequest\x1a2.osmosis.incentives.QueryLockableDurationsResponse"6\x82\xd3\xe4\x93\x020\x12./osmosis/incentives/v1beta1/lockable_durations\x12\x92\x01\n\tAllGroups\x12).osmosis.incentives.QueryAllGroupsRequest\x1a*.osmosis.incentives.QueryAllGroupsResponse".\x82\xd3\xe4\x93\x02(\x12&/osmosis/incentives/v1beta1/all_groups\x12\xab\x01\n\x0fAllGroupsGauges\x12/.osmosis.incentives.QueryAllGroupsGaugesRequest\x1a0.osmosis.incentives.QueryAllGroupsGaugesResponse"5\x82\xd3\xe4\x93\x02/\x12-/osmosis/incentives/v1beta1/all_groups_gauges\x12\xb8\x01\n\x12AllGroupsWithGauge\x122.osmosis.incentives.QueryAllGroupsWithGaugeRequest\x1a3.osmosis.incentives.QueryAllGroupsWithGaugeResponse"9\x82\xd3\xe4\x93\x023\x121/osmosis/incentives/v1beta1/all_groups_with_gauge\x12\xc2\x01\n\x13GroupByGroupGaugeID\x123.osmosis.incentives.QueryGroupByGroupGaugeIDRequest\x1a4.osmosis.incentives.QueryGroupByGroupGaugeIDResponse"@\x82\xd3\xe4\x93\x02:\x128/osmosis/incentives/v1beta1/group_by_group_gauge_id/{id}\x12\xef\x01\n\x1bCurrentWeightByGroupGaugeID\x12;.osmosis.incentives.QueryCurrentWeightByGroupGaugeIDRequest\x1a<.osmosis.incentives.QueryCurrentWeightByGroupGaugeIDResponse"U\x82\xd3\xe4\x93\x02O\x12M/osmosis/incentives/v1beta1/current_weight_by_group_gauge_id/{group_gauge_id}B8Z6github.com/osmosis-labs/osmosis/v21/x/incentives/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'osmosis.incentives.query_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z6github.com/osmosis-labs/osmosis/v21/x/incentives/types'
    _globals['_MODULETODISTRIBUTECOINSRESPONSE'].fields_by_name['coins']._options = None
    _globals['_MODULETODISTRIBUTECOINSRESPONSE'].fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_GAUGESRESPONSE'].fields_by_name['data']._options = None
    _globals['_GAUGESRESPONSE'].fields_by_name['data']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_ACTIVEGAUGESRESPONSE'].fields_by_name['data']._options = None
    _globals['_ACTIVEGAUGESRESPONSE'].fields_by_name['data']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_ACTIVEGAUGESPERDENOMRESPONSE'].fields_by_name['data']._options = None
    _globals['_ACTIVEGAUGESPERDENOMRESPONSE'].fields_by_name['data']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_UPCOMINGGAUGESRESPONSE'].fields_by_name['data']._options = None
    _globals['_UPCOMINGGAUGESRESPONSE'].fields_by_name['data']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_UPCOMINGGAUGESPERDENOMRESPONSE'].fields_by_name['upcoming_gauges']._options = None
    _globals['_UPCOMINGGAUGESPERDENOMRESPONSE'].fields_by_name['upcoming_gauges']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_REWARDSESTREQUEST'].fields_by_name['owner']._options = None
    _globals['_REWARDSESTREQUEST'].fields_by_name['owner']._serialized_options = b'\xf2\xde\x1f\x0cyaml:"owner"'
    _globals['_REWARDSESTRESPONSE'].fields_by_name['coins']._options = None
    _globals['_REWARDSESTRESPONSE'].fields_by_name['coins']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_QUERYLOCKABLEDURATIONSRESPONSE'].fields_by_name['lockable_durations']._options = None
    _globals['_QUERYLOCKABLEDURATIONSRESPONSE'].fields_by_name['lockable_durations']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x19yaml:"lockable_durations"\x98\xdf\x1f\x01'
    _globals['_QUERYALLGROUPSRESPONSE'].fields_by_name['groups']._options = None
    _globals['_QUERYALLGROUPSRESPONSE'].fields_by_name['groups']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYALLGROUPSGAUGESRESPONSE'].fields_by_name['gauges']._options = None
    _globals['_QUERYALLGROUPSGAUGESRESPONSE'].fields_by_name['gauges']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYALLGROUPSWITHGAUGERESPONSE'].fields_by_name['groups_with_gauge']._options = None
    _globals['_QUERYALLGROUPSWITHGAUGERESPONSE'].fields_by_name['groups_with_gauge']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYGROUPBYGROUPGAUGEIDRESPONSE'].fields_by_name['group']._options = None
    _globals['_QUERYGROUPBYGROUPGAUGEIDRESPONSE'].fields_by_name['group']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_QUERYCURRENTWEIGHTBYGROUPGAUGEIDRESPONSE'].fields_by_name['gauge_weight']._options = None
    _globals['_QUERYCURRENTWEIGHTBYGROUPGAUGEIDRESPONSE'].fields_by_name['gauge_weight']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_GAUGEWEIGHT'].fields_by_name['weight_ratio']._options = None
    _globals['_GAUGEWEIGHT'].fields_by_name['weight_ratio']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\xf2\xde\x1f\x13yaml:"weight_ratio"'
    _globals['_QUERY'].methods_by_name['ModuleToDistributeCoins']._options = None
    _globals['_QUERY'].methods_by_name['ModuleToDistributeCoins']._serialized_options = b'\x82\xd3\xe4\x93\x028\x126/osmosis/incentives/v1beta1/module_to_distribute_coins'
    _globals['_QUERY'].methods_by_name['GaugeByID']._options = None
    _globals['_QUERY'].methods_by_name['GaugeByID']._serialized_options = b'\x82\xd3\xe4\x93\x02.\x12,/osmosis/incentives/v1beta1/gauge_by_id/{id}'
    _globals['_QUERY'].methods_by_name['Gauges']._options = None
    _globals['_QUERY'].methods_by_name['Gauges']._serialized_options = b'\x82\xd3\xe4\x93\x02$\x12"/osmosis/incentives/v1beta1/gauges'
    _globals['_QUERY'].methods_by_name['ActiveGauges']._options = None
    _globals['_QUERY'].methods_by_name['ActiveGauges']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/osmosis/incentives/v1beta1/active_gauges'
    _globals['_QUERY'].methods_by_name['ActiveGaugesPerDenom']._options = None
    _globals['_QUERY'].methods_by_name['ActiveGaugesPerDenom']._serialized_options = b'\x82\xd3\xe4\x93\x025\x123/osmosis/incentives/v1beta1/active_gauges_per_denom'
    _globals['_QUERY'].methods_by_name['UpcomingGauges']._options = None
    _globals['_QUERY'].methods_by_name['UpcomingGauges']._serialized_options = b'\x82\xd3\xe4\x93\x02-\x12+/osmosis/incentives/v1beta1/upcoming_gauges'
    _globals['_QUERY'].methods_by_name['UpcomingGaugesPerDenom']._options = None
    _globals['_QUERY'].methods_by_name['UpcomingGaugesPerDenom']._serialized_options = b'\x82\xd3\xe4\x93\x027\x125/osmosis/incentives/v1beta1/upcoming_gauges_per_denom'
    _globals['_QUERY'].methods_by_name['RewardsEst']._options = None
    _globals['_QUERY'].methods_by_name['RewardsEst']._serialized_options = b'\x82\xd3\xe4\x93\x021\x12//osmosis/incentives/v1beta1/rewards_est/{owner}'
    _globals['_QUERY'].methods_by_name['LockableDurations']._options = None
    _globals['_QUERY'].methods_by_name['LockableDurations']._serialized_options = b'\x82\xd3\xe4\x93\x020\x12./osmosis/incentives/v1beta1/lockable_durations'
    _globals['_QUERY'].methods_by_name['AllGroups']._options = None
    _globals['_QUERY'].methods_by_name['AllGroups']._serialized_options = b'\x82\xd3\xe4\x93\x02(\x12&/osmosis/incentives/v1beta1/all_groups'
    _globals['_QUERY'].methods_by_name['AllGroupsGauges']._options = None
    _globals['_QUERY'].methods_by_name['AllGroupsGauges']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/osmosis/incentives/v1beta1/all_groups_gauges'
    _globals['_QUERY'].methods_by_name['AllGroupsWithGauge']._options = None
    _globals['_QUERY'].methods_by_name['AllGroupsWithGauge']._serialized_options = b'\x82\xd3\xe4\x93\x023\x121/osmosis/incentives/v1beta1/all_groups_with_gauge'
    _globals['_QUERY'].methods_by_name['GroupByGroupGaugeID']._options = None
    _globals['_QUERY'].methods_by_name['GroupByGroupGaugeID']._serialized_options = b'\x82\xd3\xe4\x93\x02:\x128/osmosis/incentives/v1beta1/group_by_group_gauge_id/{id}'
    _globals['_QUERY'].methods_by_name['CurrentWeightByGroupGaugeID']._options = None
    _globals['_QUERY'].methods_by_name['CurrentWeightByGroupGaugeID']._serialized_options = b'\x82\xd3\xe4\x93\x02O\x12M/osmosis/incentives/v1beta1/current_weight_by_group_gauge_id/{group_gauge_id}'
    _globals['_MODULETODISTRIBUTECOINSREQUEST']._serialized_start = 305
    _globals['_MODULETODISTRIBUTECOINSREQUEST']._serialized_end = 337
    _globals['_MODULETODISTRIBUTECOINSRESPONSE']._serialized_start = 339
    _globals['_MODULETODISTRIBUTECOINSRESPONSE']._serialized_end = 464
    _globals['_GAUGEBYIDREQUEST']._serialized_start = 466
    _globals['_GAUGEBYIDREQUEST']._serialized_end = 496
    _globals['_GAUGEBYIDRESPONSE']._serialized_start = 498
    _globals['_GAUGEBYIDRESPONSE']._serialized_end = 559
    _globals['_GAUGESREQUEST']._serialized_start = 561
    _globals['_GAUGESREQUEST']._serialized_end = 636
    _globals['_GAUGESRESPONSE']._serialized_start = 638
    _globals['_GAUGESRESPONSE']._serialized_end = 762
    _globals['_ACTIVEGAUGESREQUEST']._serialized_start = 764
    _globals['_ACTIVEGAUGESREQUEST']._serialized_end = 845
    _globals['_ACTIVEGAUGESRESPONSE']._serialized_start = 848
    _globals['_ACTIVEGAUGESRESPONSE']._serialized_end = 978
    _globals['_ACTIVEGAUGESPERDENOMREQUEST']._serialized_start = 980
    _globals['_ACTIVEGAUGESPERDENOMREQUEST']._serialized_end = 1084
    _globals['_ACTIVEGAUGESPERDENOMRESPONSE']._serialized_start = 1087
    _globals['_ACTIVEGAUGESPERDENOMRESPONSE']._serialized_end = 1225
    _globals['_UPCOMINGGAUGESREQUEST']._serialized_start = 1227
    _globals['_UPCOMINGGAUGESREQUEST']._serialized_end = 1310
    _globals['_UPCOMINGGAUGESRESPONSE']._serialized_start = 1313
    _globals['_UPCOMINGGAUGESRESPONSE']._serialized_end = 1445
    _globals['_UPCOMINGGAUGESPERDENOMREQUEST']._serialized_start = 1447
    _globals['_UPCOMINGGAUGESPERDENOMREQUEST']._serialized_end = 1553
    _globals['_UPCOMINGGAUGESPERDENOMRESPONSE']._serialized_start = 1556
    _globals['_UPCOMINGGAUGESPERDENOMRESPONSE']._serialized_end = 1707
    _globals['_REWARDSESTREQUEST']._serialized_start = 1709
    _globals['_REWARDSESTREQUEST']._serialized_end = 1798
    _globals['_REWARDSESTRESPONSE']._serialized_start = 1800
    _globals['_REWARDSESTRESPONSE']._serialized_end = 1912
    _globals['_QUERYLOCKABLEDURATIONSREQUEST']._serialized_start = 1914
    _globals['_QUERYLOCKABLEDURATIONSREQUEST']._serialized_end = 1945
    _globals['_QUERYLOCKABLEDURATIONSRESPONSE']._serialized_start = 1947
    _globals['_QUERYLOCKABLEDURATIONSRESPONSE']._serialized_end = 2073
    _globals['_QUERYALLGROUPSREQUEST']._serialized_start = 2075
    _globals['_QUERYALLGROUPSREQUEST']._serialized_end = 2098
    _globals['_QUERYALLGROUPSRESPONSE']._serialized_start = 2100
    _globals['_QUERYALLGROUPSRESPONSE']._serialized_end = 2173
    _globals['_QUERYALLGROUPSGAUGESREQUEST']._serialized_start = 2175
    _globals['_QUERYALLGROUPSGAUGESREQUEST']._serialized_end = 2204
    _globals['_QUERYALLGROUPSGAUGESRESPONSE']._serialized_start = 2206
    _globals['_QUERYALLGROUPSGAUGESRESPONSE']._serialized_end = 2285
    _globals['_QUERYALLGROUPSWITHGAUGEREQUEST']._serialized_start = 2287
    _globals['_QUERYALLGROUPSWITHGAUGEREQUEST']._serialized_end = 2319
    _globals['_QUERYALLGROUPSWITHGAUGERESPONSE']._serialized_start = 2321
    _globals['_QUERYALLGROUPSWITHGAUGERESPONSE']._serialized_end = 2424
    _globals['_QUERYGROUPBYGROUPGAUGEIDREQUEST']._serialized_start = 2426
    _globals['_QUERYGROUPBYGROUPGAUGEIDREQUEST']._serialized_end = 2471
    _globals['_QUERYGROUPBYGROUPGAUGEIDRESPONSE']._serialized_start = 2473
    _globals['_QUERYGROUPBYGROUPGAUGEIDRESPONSE']._serialized_end = 2555
    _globals['_QUERYCURRENTWEIGHTBYGROUPGAUGEIDREQUEST']._serialized_start = 2557
    _globals['_QUERYCURRENTWEIGHTBYGROUPGAUGEIDREQUEST']._serialized_end = 2622
    _globals['_QUERYCURRENTWEIGHTBYGROUPGAUGEIDRESPONSE']._serialized_start = 2624
    _globals['_QUERYCURRENTWEIGHTBYGROUPGAUGEIDRESPONSE']._serialized_end = 2727
    _globals['_GAUGEWEIGHT']._serialized_start = 2729
    _globals['_GAUGEWEIGHT']._serialized_end = 2842
    _globals['_QUERY']._serialized_start = 2845
    _globals['_QUERY']._serialized_end = 5288
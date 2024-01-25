from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from cosmos.base.v1beta1 import coin_pb2 as _coin_pb2
from osmosis.lockup import lock_pb2 as _lock_pb2
from osmosis.incentives import gauge_pb2 as _gauge_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SplittingPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ByVolume: _ClassVar[SplittingPolicy]
ByVolume: SplittingPolicy

class InternalGaugeInfo(_message.Message):
    __slots__ = ('total_weight', 'gauge_records')
    TOTAL_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    GAUGE_RECORDS_FIELD_NUMBER: _ClassVar[int]
    total_weight: str
    gauge_records: _containers.RepeatedCompositeFieldContainer[InternalGaugeRecord]

    def __init__(self, total_weight: _Optional[str]=..., gauge_records: _Optional[_Iterable[_Union[InternalGaugeRecord, _Mapping]]]=...) -> None:
        ...

class InternalGaugeRecord(_message.Message):
    __slots__ = ('gauge_id', 'current_weight', 'cumulative_weight')
    GAUGE_ID_FIELD_NUMBER: _ClassVar[int]
    CURRENT_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    CUMULATIVE_WEIGHT_FIELD_NUMBER: _ClassVar[int]
    gauge_id: int
    current_weight: str
    cumulative_weight: str

    def __init__(self, gauge_id: _Optional[int]=..., current_weight: _Optional[str]=..., cumulative_weight: _Optional[str]=...) -> None:
        ...

class Group(_message.Message):
    __slots__ = ('group_gauge_id', 'internal_gauge_info', 'splitting_policy')
    GROUP_GAUGE_ID_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_GAUGE_INFO_FIELD_NUMBER: _ClassVar[int]
    SPLITTING_POLICY_FIELD_NUMBER: _ClassVar[int]
    group_gauge_id: int
    internal_gauge_info: InternalGaugeInfo
    splitting_policy: SplittingPolicy

    def __init__(self, group_gauge_id: _Optional[int]=..., internal_gauge_info: _Optional[_Union[InternalGaugeInfo, _Mapping]]=..., splitting_policy: _Optional[_Union[SplittingPolicy, str]]=...) -> None:
        ...

class CreateGroup(_message.Message):
    __slots__ = ('pool_ids',)
    POOL_IDS_FIELD_NUMBER: _ClassVar[int]
    pool_ids: _containers.RepeatedScalarFieldContainer[int]

    def __init__(self, pool_ids: _Optional[_Iterable[int]]=...) -> None:
        ...

class GroupsWithGauge(_message.Message):
    __slots__ = ('group', 'gauge')
    GROUP_FIELD_NUMBER: _ClassVar[int]
    GAUGE_FIELD_NUMBER: _ClassVar[int]
    group: Group
    gauge: _gauge_pb2.Gauge

    def __init__(self, group: _Optional[_Union[Group, _Mapping]]=..., gauge: _Optional[_Union[_gauge_pb2.Gauge, _Mapping]]=...) -> None:
        ...
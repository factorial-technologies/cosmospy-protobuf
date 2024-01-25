from gogoproto import gogo_pb2 as _gogo_pb2
from osmosis.incentives import group_pb2 as _group_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateGroupsProposal(_message.Message):
    __slots__ = ('title', 'description', 'create_groups')
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_GROUPS_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    create_groups: _containers.RepeatedCompositeFieldContainer[_group_pb2.CreateGroup]

    def __init__(self, title: _Optional[str]=..., description: _Optional[str]=..., create_groups: _Optional[_Iterable[_Union[_group_pb2.CreateGroup, _Mapping]]]=...) -> None:
        ...
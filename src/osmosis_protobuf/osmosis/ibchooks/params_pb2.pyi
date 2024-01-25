from gogoproto import gogo_pb2 as _gogo_pb2
from cosmos_proto import cosmos_pb2 as _cosmos_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class Params(_message.Message):
    __slots__ = ('allowed_async_ack_contracts',)
    ALLOWED_ASYNC_ACK_CONTRACTS_FIELD_NUMBER: _ClassVar[int]
    allowed_async_ack_contracts: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, allowed_async_ack_contracts: _Optional[_Iterable[str]]=...) -> None:
        ...
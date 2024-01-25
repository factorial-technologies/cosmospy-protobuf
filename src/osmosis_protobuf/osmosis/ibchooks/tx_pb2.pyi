from gogoproto import gogo_pb2 as _gogo_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class MsgEmitIBCAck(_message.Message):
    __slots__ = ('sender', 'packet_sequence', 'channel')
    SENDER_FIELD_NUMBER: _ClassVar[int]
    PACKET_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    sender: str
    packet_sequence: int
    channel: str

    def __init__(self, sender: _Optional[str]=..., packet_sequence: _Optional[int]=..., channel: _Optional[str]=...) -> None:
        ...

class MsgEmitIBCAckResponse(_message.Message):
    __slots__ = ('contract_result', 'ibc_ack')
    CONTRACT_RESULT_FIELD_NUMBER: _ClassVar[int]
    IBC_ACK_FIELD_NUMBER: _ClassVar[int]
    contract_result: str
    ibc_ack: str

    def __init__(self, contract_result: _Optional[str]=..., ibc_ack: _Optional[str]=...) -> None:
        ...
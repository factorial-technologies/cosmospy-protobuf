from gogoproto import gogo_pb2 as _gogo_pb2
from osmosis.poolmanager.v1beta1 import tx_pb2 as _tx_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DenomPairTakerFeeProposal(_message.Message):
    __slots__ = ('title', 'description', 'denom_pair_taker_fee')
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DENOM_PAIR_TAKER_FEE_FIELD_NUMBER: _ClassVar[int]
    title: str
    description: str
    denom_pair_taker_fee: _containers.RepeatedCompositeFieldContainer[_tx_pb2.DenomPairTakerFee]

    def __init__(self, title: _Optional[str]=..., description: _Optional[str]=..., denom_pair_taker_fee: _Optional[_Iterable[_Union[_tx_pb2.DenomPairTakerFee, _Mapping]]]=...) -> None:
        ...
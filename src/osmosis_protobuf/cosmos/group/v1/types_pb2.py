"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....cosmos_proto import cosmos_pb2 as cosmos__proto_dot_cosmos__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from ....amino import amino_pb2 as amino_dot_amino__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bcosmos/group/v1/types.proto\x12\x0fcosmos.group.v1\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19cosmos_proto/cosmos.proto\x1a\x19google/protobuf/any.proto\x1a\x11amino/amino.proto"\x92\x01\n\x06Member\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\x0e\n\x06weight\x18\x02 \x01(\t\x12\x10\n\x08metadata\x18\x03 \x01(\t\x12;\n\x08added_at\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01"\\\n\rMemberRequest\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\x0e\n\x06weight\x18\x02 \x01(\t\x12\x10\n\x08metadata\x18\x03 \x01(\t"\xb0\x01\n\x17ThresholdDecisionPolicy\x12\x11\n\tthreshold\x18\x01 \x01(\t\x127\n\x07windows\x18\x02 \x01(\x0b2&.cosmos.group.v1.DecisionPolicyWindows:I\xca\xb4-\x1ecosmos.group.v1.DecisionPolicy\x8a\xe7\xb0*"cosmos-sdk/ThresholdDecisionPolicy"\xb3\x01\n\x18PercentageDecisionPolicy\x12\x12\n\npercentage\x18\x01 \x01(\t\x127\n\x07windows\x18\x02 \x01(\x0b2&.cosmos.group.v1.DecisionPolicyWindows:J\xca\xb4-\x1ecosmos.group.v1.DecisionPolicy\x8a\xe7\xb0*#cosmos-sdk/PercentageDecisionPolicy"\xa0\x01\n\x15DecisionPolicyWindows\x12?\n\rvoting_period\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationB\r\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xa8\xe7\xb0*\x01\x12F\n\x14min_execution_period\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\r\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xa8\xe7\xb0*\x01"\xb8\x01\n\tGroupInfo\x12\n\n\x02id\x18\x01 \x01(\x04\x12\'\n\x05admin\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\x10\n\x08metadata\x18\x03 \x01(\t\x12\x0f\n\x07version\x18\x04 \x01(\x04\x12\x14\n\x0ctotal_weight\x18\x05 \x01(\t\x12=\n\ncreated_at\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01"H\n\x0bGroupMember\x12\x10\n\x08group_id\x18\x01 \x01(\x04\x12\'\n\x06member\x18\x02 \x01(\x0b2\x17.cosmos.group.v1.Member"\xb6\x02\n\x0fGroupPolicyInfo\x12)\n\x07address\x18\x01 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\x10\n\x08group_id\x18\x02 \x01(\x04\x12\'\n\x05admin\x18\x03 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\x10\n\x08metadata\x18\x04 \x01(\t\x12\x0f\n\x07version\x18\x05 \x01(\x04\x12Q\n\x0fdecision_policy\x18\x06 \x01(\x0b2\x14.google.protobuf.AnyB"\xca\xb4-\x1ecosmos.group.v1.DecisionPolicy\x12=\n\ncreated_at\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01:\x08\x88\xa0\x1f\x00\xe8\xa0\x1f\x01"\xce\x04\n\x08Proposal\x12\n\n\x02id\x18\x01 \x01(\x04\x126\n\x14group_policy_address\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12\x10\n\x08metadata\x18\x03 \x01(\t\x12+\n\tproposers\x18\x04 \x03(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12>\n\x0bsubmit_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01\x12\x15\n\rgroup_version\x18\x06 \x01(\x04\x12\x1c\n\x14group_policy_version\x18\x07 \x01(\x04\x12/\n\x06status\x18\x08 \x01(\x0e2\x1f.cosmos.group.v1.ProposalStatus\x12C\n\x12final_tally_result\x18\t \x01(\x0b2\x1c.cosmos.group.v1.TallyResultB\t\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01\x12D\n\x11voting_period_end\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01\x12@\n\x0fexecutor_result\x18\x0b \x01(\x0e2\'.cosmos.group.v1.ProposalExecutorResult\x12&\n\x08messages\x18\x0c \x03(\x0b2\x14.google.protobuf.Any\x12\r\n\x05title\x18\r \x01(\t\x12\x0f\n\x07summary\x18\x0e \x01(\t:\x04\x88\xa0\x1f\x00"k\n\x0bTallyResult\x12\x11\n\tyes_count\x18\x01 \x01(\t\x12\x15\n\rabstain_count\x18\x02 \x01(\t\x12\x10\n\x08no_count\x18\x03 \x01(\t\x12\x1a\n\x12no_with_veto_count\x18\x04 \x01(\t:\x04\x88\xa0\x1f\x00"\xc3\x01\n\x04Vote\x12\x13\n\x0bproposal_id\x18\x01 \x01(\x04\x12\'\n\x05voter\x18\x02 \x01(\tB\x18\xd2\xb4-\x14cosmos.AddressString\x12+\n\x06option\x18\x03 \x01(\x0e2\x1b.cosmos.group.v1.VoteOption\x12\x10\n\x08metadata\x18\x04 \x01(\t\x12>\n\x0bsubmit_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\r\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01*\x8f\x01\n\nVoteOption\x12\x1b\n\x17VOTE_OPTION_UNSPECIFIED\x10\x00\x12\x13\n\x0fVOTE_OPTION_YES\x10\x01\x12\x17\n\x13VOTE_OPTION_ABSTAIN\x10\x02\x12\x12\n\x0eVOTE_OPTION_NO\x10\x03\x12\x1c\n\x18VOTE_OPTION_NO_WITH_VETO\x10\x04\x1a\x04\x88\xa3\x1e\x00*\xce\x01\n\x0eProposalStatus\x12\x1f\n\x1bPROPOSAL_STATUS_UNSPECIFIED\x10\x00\x12\x1d\n\x19PROPOSAL_STATUS_SUBMITTED\x10\x01\x12\x1c\n\x18PROPOSAL_STATUS_ACCEPTED\x10\x02\x12\x1c\n\x18PROPOSAL_STATUS_REJECTED\x10\x03\x12\x1b\n\x17PROPOSAL_STATUS_ABORTED\x10\x04\x12\x1d\n\x19PROPOSAL_STATUS_WITHDRAWN\x10\x05\x1a\x04\x88\xa3\x1e\x00*\xba\x01\n\x16ProposalExecutorResult\x12(\n$PROPOSAL_EXECUTOR_RESULT_UNSPECIFIED\x10\x00\x12$\n PROPOSAL_EXECUTOR_RESULT_NOT_RUN\x10\x01\x12$\n PROPOSAL_EXECUTOR_RESULT_SUCCESS\x10\x02\x12$\n PROPOSAL_EXECUTOR_RESULT_FAILURE\x10\x03\x1a\x04\x88\xa3\x1e\x00B&Z$github.com/cosmos/cosmos-sdk/x/groupb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cosmos.group.v1.types_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
    _globals['DESCRIPTOR']._options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z$github.com/cosmos/cosmos-sdk/x/group'
    _globals['_VOTEOPTION']._options = None
    _globals['_VOTEOPTION']._serialized_options = b'\x88\xa3\x1e\x00'
    _globals['_PROPOSALSTATUS']._options = None
    _globals['_PROPOSALSTATUS']._serialized_options = b'\x88\xa3\x1e\x00'
    _globals['_PROPOSALEXECUTORRESULT']._options = None
    _globals['_PROPOSALEXECUTORRESULT']._serialized_options = b'\x88\xa3\x1e\x00'
    _globals['_MEMBER'].fields_by_name['address']._options = None
    _globals['_MEMBER'].fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_MEMBER'].fields_by_name['added_at']._options = None
    _globals['_MEMBER'].fields_by_name['added_at']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01'
    _globals['_MEMBERREQUEST'].fields_by_name['address']._options = None
    _globals['_MEMBERREQUEST'].fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_THRESHOLDDECISIONPOLICY']._options = None
    _globals['_THRESHOLDDECISIONPOLICY']._serialized_options = b'\xca\xb4-\x1ecosmos.group.v1.DecisionPolicy\x8a\xe7\xb0*"cosmos-sdk/ThresholdDecisionPolicy'
    _globals['_PERCENTAGEDECISIONPOLICY']._options = None
    _globals['_PERCENTAGEDECISIONPOLICY']._serialized_options = b'\xca\xb4-\x1ecosmos.group.v1.DecisionPolicy\x8a\xe7\xb0*#cosmos-sdk/PercentageDecisionPolicy'
    _globals['_DECISIONPOLICYWINDOWS'].fields_by_name['voting_period']._options = None
    _globals['_DECISIONPOLICYWINDOWS'].fields_by_name['voting_period']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xa8\xe7\xb0*\x01'
    _globals['_DECISIONPOLICYWINDOWS'].fields_by_name['min_execution_period']._options = None
    _globals['_DECISIONPOLICYWINDOWS'].fields_by_name['min_execution_period']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01\xa8\xe7\xb0*\x01'
    _globals['_GROUPINFO'].fields_by_name['admin']._options = None
    _globals['_GROUPINFO'].fields_by_name['admin']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_GROUPINFO'].fields_by_name['created_at']._options = None
    _globals['_GROUPINFO'].fields_by_name['created_at']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01'
    _globals['_GROUPPOLICYINFO'].fields_by_name['address']._options = None
    _globals['_GROUPPOLICYINFO'].fields_by_name['address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_GROUPPOLICYINFO'].fields_by_name['admin']._options = None
    _globals['_GROUPPOLICYINFO'].fields_by_name['admin']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_GROUPPOLICYINFO'].fields_by_name['decision_policy']._options = None
    _globals['_GROUPPOLICYINFO'].fields_by_name['decision_policy']._serialized_options = b'\xca\xb4-\x1ecosmos.group.v1.DecisionPolicy'
    _globals['_GROUPPOLICYINFO'].fields_by_name['created_at']._options = None
    _globals['_GROUPPOLICYINFO'].fields_by_name['created_at']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01'
    _globals['_GROUPPOLICYINFO']._options = None
    _globals['_GROUPPOLICYINFO']._serialized_options = b'\x88\xa0\x1f\x00\xe8\xa0\x1f\x01'
    _globals['_PROPOSAL'].fields_by_name['group_policy_address']._options = None
    _globals['_PROPOSAL'].fields_by_name['group_policy_address']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_PROPOSAL'].fields_by_name['proposers']._options = None
    _globals['_PROPOSAL'].fields_by_name['proposers']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_PROPOSAL'].fields_by_name['submit_time']._options = None
    _globals['_PROPOSAL'].fields_by_name['submit_time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01'
    _globals['_PROPOSAL'].fields_by_name['final_tally_result']._options = None
    _globals['_PROPOSAL'].fields_by_name['final_tally_result']._serialized_options = b'\xc8\xde\x1f\x00\xa8\xe7\xb0*\x01'
    _globals['_PROPOSAL'].fields_by_name['voting_period_end']._options = None
    _globals['_PROPOSAL'].fields_by_name['voting_period_end']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01'
    _globals['_PROPOSAL']._options = None
    _globals['_PROPOSAL']._serialized_options = b'\x88\xa0\x1f\x00'
    _globals['_TALLYRESULT']._options = None
    _globals['_TALLYRESULT']._serialized_options = b'\x88\xa0\x1f\x00'
    _globals['_VOTE'].fields_by_name['voter']._options = None
    _globals['_VOTE'].fields_by_name['voter']._serialized_options = b'\xd2\xb4-\x14cosmos.AddressString'
    _globals['_VOTE'].fields_by_name['submit_time']._options = None
    _globals['_VOTE'].fields_by_name['submit_time']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01\xa8\xe7\xb0*\x01'
    _globals['_VOTEOPTION']._serialized_start = 2450
    _globals['_VOTEOPTION']._serialized_end = 2593
    _globals['_PROPOSALSTATUS']._serialized_start = 2596
    _globals['_PROPOSALSTATUS']._serialized_end = 2802
    _globals['_PROPOSALEXECUTORRESULT']._serialized_start = 2805
    _globals['_PROPOSALEXECUTORRESULT']._serialized_end = 2991
    _globals['_MEMBER']._serialized_start = 209
    _globals['_MEMBER']._serialized_end = 355
    _globals['_MEMBERREQUEST']._serialized_start = 357
    _globals['_MEMBERREQUEST']._serialized_end = 449
    _globals['_THRESHOLDDECISIONPOLICY']._serialized_start = 452
    _globals['_THRESHOLDDECISIONPOLICY']._serialized_end = 628
    _globals['_PERCENTAGEDECISIONPOLICY']._serialized_start = 631
    _globals['_PERCENTAGEDECISIONPOLICY']._serialized_end = 810
    _globals['_DECISIONPOLICYWINDOWS']._serialized_start = 813
    _globals['_DECISIONPOLICYWINDOWS']._serialized_end = 973
    _globals['_GROUPINFO']._serialized_start = 976
    _globals['_GROUPINFO']._serialized_end = 1160
    _globals['_GROUPMEMBER']._serialized_start = 1162
    _globals['_GROUPMEMBER']._serialized_end = 1234
    _globals['_GROUPPOLICYINFO']._serialized_start = 1237
    _globals['_GROUPPOLICYINFO']._serialized_end = 1547
    _globals['_PROPOSAL']._serialized_start = 1550
    _globals['_PROPOSAL']._serialized_end = 2140
    _globals['_TALLYRESULT']._serialized_start = 2142
    _globals['_TALLYRESULT']._serialized_end = 2249
    _globals['_VOTE']._serialized_start = 2252
    _globals['_VOTE']._serialized_end = 2447
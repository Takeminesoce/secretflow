# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: secretflow/ic/proto/handshake/entry.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from secretflow.ic.proto.common import header_pb2 as secretflow_dot_ic_dot_proto_dot_common_dot_header__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)secretflow/ic/proto/handshake/entry.proto\x12\x16org.interconnection.v2\x1a\x19google/protobuf/any.proto\x1a\'secretflow/ic/proto/common/header.proto\".\n\x1bHandshakeVersionCheckHelper\x12\x0f\n\x07version\x18\x01 \x01(\x05\"\xae\x02\n\x10HandshakeRequest\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12\x16\n\x0erequester_rank\x18\x02 \x01(\x05\x12\x17\n\x0fsupported_algos\x18\x03 \x03(\x05\x12)\n\x0b\x61lgo_params\x18\x04 \x03(\x0b\x32\x14.google.protobuf.Any\x12\x0b\n\x03ops\x18\x05 \x03(\x05\x12\'\n\top_params\x18\x06 \x03(\x0b\x32\x14.google.protobuf.Any\x12\x19\n\x11protocol_families\x18\x07 \x03(\x05\x12\x34\n\x16protocol_family_params\x18\x08 \x03(\x0b\x32\x14.google.protobuf.Any\x12&\n\x08io_param\x18\t \x01(\x0b\x32\x14.google.protobuf.Any\"\xaf\x02\n\x11HandshakeResponse\x12\x33\n\x06header\x18\x01 \x01(\x0b\x32#.org.interconnection.ResponseHeader\x12\x0c\n\x04\x61lgo\x18\x02 \x01(\x05\x12(\n\nalgo_param\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0b\n\x03ops\x18\x04 \x03(\x05\x12\'\n\top_params\x18\x05 \x03(\x0b\x32\x14.google.protobuf.Any\x12\x19\n\x11protocol_families\x18\x06 \x03(\x05\x12\x34\n\x16protocol_family_params\x18\x07 \x03(\x0b\x32\x14.google.protobuf.Any\x12&\n\x08io_param\x18\x08 \x01(\x0b\x32\x14.google.protobuf.Any*e\n\x08\x41lgoType\x12\x19\n\x15\x41LGO_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12\x41LGO_TYPE_ECDH_PSI\x10\x01\x12\x13\n\x0f\x41LGO_TYPE_SS_LR\x10\x02\x12\x11\n\rALGO_TYPE_SGB\x10\x03*6\n\x06OpType\x12\x17\n\x13OP_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fOP_TYPE_SIGMOID\x10\x01*{\n\x0eProtocolFamily\x12\x1f\n\x1bPROTOCOL_FAMILY_UNSPECIFIED\x10\x00\x12\x17\n\x13PROTOCOL_FAMILY_ECC\x10\x01\x12\x16\n\x12PROTOCOL_FAMILY_SS\x10\x02\x12\x17\n\x13PROTOCOL_FAMILY_PHE\x10\x03\x62\x06proto3')

_ALGOTYPE = DESCRIPTOR.enum_types_by_name['AlgoType']
AlgoType = enum_type_wrapper.EnumTypeWrapper(_ALGOTYPE)
_OPTYPE = DESCRIPTOR.enum_types_by_name['OpType']
OpType = enum_type_wrapper.EnumTypeWrapper(_OPTYPE)
_PROTOCOLFAMILY = DESCRIPTOR.enum_types_by_name['ProtocolFamily']
ProtocolFamily = enum_type_wrapper.EnumTypeWrapper(_PROTOCOLFAMILY)
ALGO_TYPE_UNSPECIFIED = 0
ALGO_TYPE_ECDH_PSI = 1
ALGO_TYPE_SS_LR = 2
ALGO_TYPE_SGB = 3
OP_TYPE_UNSPECIFIED = 0
OP_TYPE_SIGMOID = 1
PROTOCOL_FAMILY_UNSPECIFIED = 0
PROTOCOL_FAMILY_ECC = 1
PROTOCOL_FAMILY_SS = 2
PROTOCOL_FAMILY_PHE = 3


_HANDSHAKEVERSIONCHECKHELPER = DESCRIPTOR.message_types_by_name['HandshakeVersionCheckHelper']
_HANDSHAKEREQUEST = DESCRIPTOR.message_types_by_name['HandshakeRequest']
_HANDSHAKERESPONSE = DESCRIPTOR.message_types_by_name['HandshakeResponse']
HandshakeVersionCheckHelper = _reflection.GeneratedProtocolMessageType('HandshakeVersionCheckHelper', (_message.Message,), {
  'DESCRIPTOR' : _HANDSHAKEVERSIONCHECKHELPER,
  '__module__' : 'secretflow.ic.proto.handshake.entry_pb2'
  # @@protoc_insertion_point(class_scope:org.interconnection.v2.HandshakeVersionCheckHelper)
  })
_sym_db.RegisterMessage(HandshakeVersionCheckHelper)

HandshakeRequest = _reflection.GeneratedProtocolMessageType('HandshakeRequest', (_message.Message,), {
  'DESCRIPTOR' : _HANDSHAKEREQUEST,
  '__module__' : 'secretflow.ic.proto.handshake.entry_pb2'
  # @@protoc_insertion_point(class_scope:org.interconnection.v2.HandshakeRequest)
  })
_sym_db.RegisterMessage(HandshakeRequest)

HandshakeResponse = _reflection.GeneratedProtocolMessageType('HandshakeResponse', (_message.Message,), {
  'DESCRIPTOR' : _HANDSHAKERESPONSE,
  '__module__' : 'secretflow.ic.proto.handshake.entry_pb2'
  # @@protoc_insertion_point(class_scope:org.interconnection.v2.HandshakeResponse)
  })
_sym_db.RegisterMessage(HandshakeResponse)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ALGOTYPE._serialized_start=796
  _ALGOTYPE._serialized_end=897
  _OPTYPE._serialized_start=899
  _OPTYPE._serialized_end=953
  _PROTOCOLFAMILY._serialized_start=955
  _PROTOCOLFAMILY._serialized_end=1078
  _HANDSHAKEVERSIONCHECKHELPER._serialized_start=137
  _HANDSHAKEVERSIONCHECKHELPER._serialized_end=183
  _HANDSHAKEREQUEST._serialized_start=186
  _HANDSHAKEREQUEST._serialized_end=488
  _HANDSHAKERESPONSE._serialized_start=491
  _HANDSHAKERESPONSE._serialized_end=794
# @@protoc_insertion_point(module_scope)

"""
Stub representaton of the public objects exposed by the _psycopg3 module.

TODO: this should be generated by mypy's stubgen but it crashes with no
information. Will submit a bug.
"""

# Copyright (C) 2020 The Psycopg Team

import codecs
from typing import Any, Iterable, List, Optional, Sequence, Tuple

from .proto import AdaptContext, DumpFunc, DumpersMap, DumperType
from .proto import LoadFunc, LoadersMap, LoaderType, MaybeOid
from .connection import BaseConnection
from . import pq

Format = pq.Format

class Transformer:
    def __init__(self, context: AdaptContext = None): ...
    @property
    def connection(self) -> Optional[BaseConnection]: ...
    @property
    def codec(self) -> codecs.CodecInfo: ...
    @property
    def dumpers(self) -> DumpersMap: ...
    @property
    def loaders(self) -> LoadersMap: ...
    @property
    def pgresult(self) -> Optional["pq.proto.PGresult"]: ...
    @pgresult.setter
    def pgresult(self, result: Optional["pq.proto.PGresult"]) -> None: ...
    def set_row_types(self, types: Sequence[Tuple[int, Format]]) -> None: ...
    def dump_sequence(
        self, objs: Iterable[Any], formats: Iterable[Format]
    ) -> Tuple[List[Optional[bytes]], List[int]]: ...
    def dump(self, obj: None, format: Format = Format.TEXT) -> MaybeOid: ...
    def get_dump_function(self, src: type, format: Format) -> DumpFunc: ...
    def lookup_dumper(self, src: type, format: Format) -> DumperType: ...
    def load_row(self, row: int) -> Optional[Tuple[Any, ...]]: ...
    def load_sequence(
        self, record: Sequence[Optional[bytes]]
    ) -> Tuple[Any, ...]: ...
    def load(
        self, data: bytes, oid: int, format: Format = Format.TEXT
    ) -> Any: ...
    def get_load_function(self, oid: int, format: Format) -> LoadFunc: ...
    def lookup_loader(self, oid: int, format: Format) -> LoaderType: ...

def register_builtin_c_loaders() -> None: ...

# vim: set syntax=python:

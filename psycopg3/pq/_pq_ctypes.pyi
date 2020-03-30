"""
types stub for ctypes functions
"""

# Copyright (C) 2020 The Psycopg Team

from typing import Any, Optional, Sequence, NewType
from ctypes import Array, c_char, c_char_p, c_int, c_uint, pointer

Oid = c_uint

class PGconn_struct: ...
class PGresult_struct: ...

class PQconninfoOption_struct:
    keyword: bytes
    envvar: bytes
    compiled: bytes
    val: bytes
    label: bytes
    dispatcher: bytes
    dispsize: int

def PQhostaddr(arg1: Optional[PGconn_struct]) -> bytes: ...
def PQexecPrepared(
    arg1: Optional[PGconn_struct],
    arg2: bytes,
    arg3: int,
    arg4: Optional[Array[c_char_p]],
    arg5: Optional[Array[c_int]],
    arg6: Optional[Array[c_int]],
    arg7: int,
) -> PGresult_struct: ...
def PQprepare(
    arg1: Optional[PGconn_struct],
    arg2: bytes,
    arg3: bytes,
    arg4: int,
    arg5: Optional[Array[c_uint]],
) -> PGresult_struct: ...

# fmt: off
# autogenerated: start
def PQlibVersion() -> int: ...
def PQconnectdb(arg1: bytes) -> PGconn_struct: ...
def PQconnectStart(arg1: bytes) -> PGconn_struct: ...
def PQconnectPoll(arg1: Optional[PGconn_struct]) -> int: ...
def PQconndefaults() -> Sequence[PQconninfoOption_struct]: ...
def PQconninfoFree(arg1: Sequence[PQconninfoOption_struct]) -> None: ...
def PQconninfo(arg1: Optional[PGconn_struct]) -> Sequence[PQconninfoOption_struct]: ...
def PQconninfoParse(arg1: bytes, arg2: pointer[c_char_p]) -> Sequence[PQconninfoOption_struct]: ...
def PQfinish(arg1: Optional[PGconn_struct]) -> None: ...
def PQreset(arg1: Optional[PGconn_struct]) -> None: ...
def PQresetStart(arg1: Optional[PGconn_struct]) -> int: ...
def PQresetPoll(arg1: Optional[PGconn_struct]) -> int: ...
def PQping(arg1: bytes) -> int: ...
def PQdb(arg1: Optional[PGconn_struct]) -> bytes: ...
def PQuser(arg1: Optional[PGconn_struct]) -> bytes: ...
def PQpass(arg1: Optional[PGconn_struct]) -> bytes: ...
def PQhost(arg1: Optional[PGconn_struct]) -> bytes: ...
def _PQhostaddr(arg1: Optional[PGconn_struct]) -> bytes: ...
def PQport(arg1: Optional[PGconn_struct]) -> bytes: ...
def PQtty(arg1: Optional[PGconn_struct]) -> bytes: ...
def PQoptions(arg1: Optional[PGconn_struct]) -> bytes: ...
def PQstatus(arg1: Optional[PGconn_struct]) -> int: ...
def PQtransactionStatus(arg1: Optional[PGconn_struct]) -> int: ...
def PQparameterStatus(arg1: Optional[PGconn_struct], arg2: bytes) -> bytes: ...
def PQprotocolVersion(arg1: Optional[PGconn_struct]) -> int: ...
def PQserverVersion(arg1: Optional[PGconn_struct]) -> int: ...
def PQerrorMessage(arg1: Optional[PGconn_struct]) -> bytes: ...
def PQsocket(arg1: Optional[PGconn_struct]) -> int: ...
def PQbackendPID(arg1: Optional[PGconn_struct]) -> int: ...
def PQconnectionNeedsPassword(arg1: Optional[PGconn_struct]) -> int: ...
def PQconnectionUsedPassword(arg1: Optional[PGconn_struct]) -> int: ...
def PQsslInUse(arg1: Optional[PGconn_struct]) -> int: ...
def PQexec(arg1: Optional[PGconn_struct], arg2: bytes) -> PGresult_struct: ...
def PQexecParams(arg1: Optional[PGconn_struct], arg2: bytes, arg3: int, arg4: pointer[c_uint], arg5: pointer[c_char_p], arg6: pointer[c_int], arg7: pointer[c_int], arg8: int) -> PGresult_struct: ...
def PQdescribePrepared(arg1: Optional[PGconn_struct], arg2: bytes) -> PGresult_struct: ...
def PQdescribePortal(arg1: Optional[PGconn_struct], arg2: bytes) -> PGresult_struct: ...
def PQresultStatus(arg1: Optional[PGresult_struct]) -> int: ...
def PQresultErrorMessage(arg1: Optional[PGresult_struct]) -> bytes: ...
def PQresultErrorField(arg1: Optional[PGresult_struct], arg2: int) -> bytes: ...
def PQclear(arg1: Optional[PGresult_struct]) -> None: ...
def PQntuples(arg1: Optional[PGresult_struct]) -> int: ...
def PQnfields(arg1: Optional[PGresult_struct]) -> int: ...
def PQfname(arg1: Optional[PGresult_struct], arg2: int) -> bytes: ...
def PQftable(arg1: Optional[PGresult_struct], arg2: int) -> int: ...
def PQftablecol(arg1: Optional[PGresult_struct], arg2: int) -> int: ...
def PQfformat(arg1: Optional[PGresult_struct], arg2: int) -> int: ...
def PQftype(arg1: Optional[PGresult_struct], arg2: int) -> int: ...
def PQfmod(arg1: Optional[PGresult_struct], arg2: int) -> int: ...
def PQfsize(arg1: Optional[PGresult_struct], arg2: int) -> int: ...
def PQbinaryTuples(arg1: Optional[PGresult_struct]) -> int: ...
def PQgetvalue(arg1: Optional[PGresult_struct], arg2: int, arg3: int) -> pointer[c_char]: ...
def PQgetisnull(arg1: Optional[PGresult_struct], arg2: int, arg3: int) -> int: ...
def PQgetlength(arg1: Optional[PGresult_struct], arg2: int, arg3: int) -> int: ...
def PQnparams(arg1: Optional[PGresult_struct]) -> int: ...
def PQparamtype(arg1: Optional[PGresult_struct], arg2: int) -> int: ...
def PQcmdStatus(arg1: Optional[PGresult_struct]) -> bytes: ...
def PQcmdTuples(arg1: Optional[PGresult_struct]) -> bytes: ...
def PQoidValue(arg1: Optional[PGresult_struct]) -> int: ...
def PQsendQuery(arg1: Optional[PGconn_struct], arg2: bytes) -> int: ...
def PQsendQueryParams(arg1: Optional[PGconn_struct], arg2: bytes, arg3: int, arg4: pointer[c_uint], arg5: pointer[c_char_p], arg6: pointer[c_int], arg7: pointer[c_int], arg8: int) -> int: ...
def PQgetResult(arg1: Optional[PGconn_struct]) -> PGresult_struct: ...
def PQconsumeInput(arg1: Optional[PGconn_struct]) -> int: ...
def PQisBusy(arg1: Optional[PGconn_struct]) -> int: ...
def PQsetnonblocking(arg1: Optional[PGconn_struct], arg2: int) -> int: ...
def PQisnonblocking(arg1: Optional[PGconn_struct]) -> int: ...
def PQflush(arg1: Optional[PGconn_struct]) -> int: ...
def PQfreemem(arg1: Any) -> None: ...
def PQmakeEmptyPGresult(arg1: Optional[PGconn_struct], arg2: int) -> PGresult_struct: ...
# autogenerated: end
# fmt: on

# vim: set syntax=python:

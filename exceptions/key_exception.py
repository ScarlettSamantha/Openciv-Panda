from __future__ import annotations
from exceptions._base_exception import BaseException


class KeyException(BaseException):
    pass


class KeyNotFoundException(KeyException):
    pass

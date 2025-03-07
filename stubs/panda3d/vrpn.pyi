import panda3d.core
from typing import Any, ClassVar

Dtool_PyNativeInterface: int

class VrpnClient(panda3d.core.ClientBase):
    DtoolClassDict: ClassVar[dict] = ...
    def __init__(self, *args, **kwargs) -> None: ...
    @staticmethod
    def getClassType(*args, **kwargs): ...
    def getServerName(self, *args, **kwargs): ...
    @staticmethod
    def get_class_type() -> Any: ...
    def get_server_name(self, VrpnClientself) -> Any: ...
    def isConnected(self, *args, **kwargs): ...
    def isValid(self, *args, **kwargs): ...
    def is_connected(self, VrpnClientself) -> Any: ...
    def is_valid(self, VrpnClientself) -> Any: ...
    def write(self, VrpnClientself, ostreamout, intindent_level) -> Any: ...

def Dtool_BorrowThisReference(*args, **kwargs): ...

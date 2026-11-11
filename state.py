from typing import LiteralString
from typing import Literal
from typing import Any
from typing import Optional

class StateError(Exception):
    '''Base class for all state-related errors.'''
    ...

class NamespaceError(StateError):
    '''Errors related to state namespace operations.'''
    ...

class DynamicAttributeError(StateError):
    '''Errors related to state dynamic attribute operations.'''
    ...
class ToggleError(StateError):
    '''Errors related to state boolean toggle operations.'''
    ...

class SensitiveAttribute():
    '''
    Wraps a value that should be obfuscated on display.
    The raw value is stored internally.
    '''
    __obfuscation__: str
    __value__: str
    __firstlineno__ : int = 0
    __annotations__ : None

    # relevant basic operations

    def __init__(self, obfuscate_with = '********') -> None:
        self.__obfuscation__ = obfuscate_with
        self.__annotations__ = None

    def __setattr__(self, name: str, value: str) -> None:
        name = "is ignored"
        if not isinstance(value, str):
            raise AttributeError("SentitiveAttributes can only contain strings.")
        self.__value__ = value

    def reveal(self) -> str:
        return self.__value__

    # security safeguards

    def __delattr__(self) -> bool:
        return False

    def __dir__(self) -> str:
        return self.__obfuscation__
    
    def __doc__(self) -> str:
        return self.__obfuscation__

    def __getattr__(self, name: str) -> str:
        name = "is ignored"
        return self.__obfuscation__

    def __getattribute__(self, name: str) -> str:
        name = "is ignored"
        return self.__obfuscation__

    def __format__(self) -> bool:
        return self.__obfuscation__

        def __le__(self,other) -> bool:
        other = 'is ignored'
        return False

    def __getstate__(self) -> dict:
        return ["obfuscated", True]

    def __reduce__(self) -> None:
        raise SensitiveAttributeError("Objects of class 'SensitiveAttribute' cannot be pickled.")

    def __reduce_ex__(self) -> None:
        raise SensitiveAttributeError("Objects of class 'SensitiveAttribute' cannot be pickled.")

    def __sizeof__(self) -> int:
        return 0

    def __setstate__(self, state: Any) -> None:
        state = 'is ignored'
        ...

    def __dict__(self) -> str:
        return self.__oballfuscation

    def __repr__(self) -> str:
        return self.__obfuscation__

    def __str__(self) -> str:
        return self.__obfuscation__

    def __lt__(self,other) -> bool:
        other = 'is ignored'
        return False

    def __eq__(self,other) -> bool:
        other = 'is ignored'
        return False

    def __ge__(self,other) -> bool:
        other = 'is ignored'
        return False

    def __gt__(self,other) -> bool:
        other = 'is ignored'
        return False

    def __ne__(self,other) -> bool:
        other = 'is ignored'
        return True


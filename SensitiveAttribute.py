from typing import Any, MutableMapping, SupportsIndex

class SensitiveAttributeError(Exception):
    '''Errors related to Sensetive Attribute operations.'''
    ...

class SensitiveAttribute():
    '''
    Wraps a value that should be obfuscated on display.
    The raw value is stored internally.

    '''
    # operational attributes
    __obfuscation__:    str
    __value__:          str

    # safeguard attributes
    __firstlineno__ :   int             = 0
    # __annotations__ :   dict[str, Any]  = {"obfuscated": True}
    __match_args__  :   tuple           = ()

    # relevant basic operations

    def __init__(self, obfuscate_with = '********') -> None:
        self.__obfuscation__ = obfuscate_with
        # self.__annotations__ = {"obfuscated": True}

    def __setattr__(self, name: str, value: str) -> None:
        name = "is ignored"
        if not isinstance(value, str):
            raise AttributeError("SentitiveAttributes can only contain strings.")
        self.__value__ = value

    def reveal(self) -> str:
        return self.__value__

    # reveal safeguards

    @property
    # this is a long shot
    # remove commented-out __annotations__ assignments if it works
    def __annotations__(self) -> dict[str, Any]: # type: ignore
        return {"obfuscated": True}

    @property
    def __dict__(self) -> dict[str, Any]: # type: ignore
        return {"obfuscated": True}

    def __dir__(self) -> str:
        return self.__obfuscation__
    
    def __doc__(self) -> str:           # type: ignore
        return self.__obfuscation__

    def __enter__(self) -> None:
        return None

    def __exit__(self, exc_class, exc_value, exc_trace) -> None:
        return None

    def __getattr__(self, name: str) -> str:
        name = "is ignored"
        return self.__obfuscation__

    def __getattribute__(self, name: str) -> str:
        name = "is ignored"
        return self.__obfuscation__

    def __getstate__(self) -> dict:
        return {"obfuscated": True}

    # conversion safeguards

    def __bool__(self) -> bool:
        return False

    def __bytes__(self) -> bytes:
        return bytes(0)

    def __complex__(self) -> complex:
        return complex(0)

    def __float__(self) -> float:
        return 0.0

    def __format__(self, format_spec: str) -> str:
        format_spec = 'is ignored'
        return self.__obfuscation__

    def __int__(self) -> int:
        return 0

    def __repr__(self) -> str:
        return self.__obfuscation__

    def __str__(self) -> str:
        return self.__obfuscation__

    # comparison safeguards

    def __le__(self,other) -> bool:
        other = 'is ignored'
        return False

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

    # deduction safeguards

    def __delattr__(self, name: str) -> None:
        name = 'is ignored'
        return None

    def __hash__(self) -> int:
        return 0

    def __reduce__(self) -> str | tuple[Any, ...]:
        raise SensitiveAttributeError("Objects of class 'SensitiveAttribute' cannot be pickled.")

    def __reduce_ex__(self, protocol: SupportsIndex) -> str | tuple[Any, ...]:
        raise SensitiveAttributeError("Objects of class 'SensitiveAttribute' cannot be pickled.")

    def __sizeof__(self) -> int:
        return 0

    # overwrite safeguards

    def __setstate__(self, state: Any) -> None:
        state = 'is ignored'
        return None

    # other

    def __call__(self, operation: str = 'steady') -> str:
        if operation.lower() == 'reveal':
            return self.__value__
        else:
            return self.__obfuscation__ 

    def __deepcopy__(self, memo) -> SensitiveAttribute:
        return self
    
    @classmethod
    # metacls or cls as first parameter ???
    # not sure this will work without a metaclass implementation
    def __prepare__(cls, name: str, bases: tuple[type, ...], /, **kwds: Any) -> MutableMapping[str, object]:
        return {}

    

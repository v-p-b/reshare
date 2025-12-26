from . import *


class ReshHelperException(Exception):
    pass


class ResharePy(Reshare):
    def __init__(
        self,
        project_name: str,
        data_types: Optional[list[ReshDataType]] = None,
        project_version: Optional[str] = None,
        symbols: Optional[list[ReshSymbol]] = None,
        target_md5: Optional[str] = None,
        target_name: Optional[str] = None,
        target_sha256: Optional[str] = None,
        target_version: Optional[str] = None,
    ):
        if data_types is None:
            data_types = []
        if symbols is None:
            symbols = []

        super().__init__(
            project_name=project_name,
            data_types=data_types,
            project_version=project_version,
            symbols=symbols,
            target_md5=target_md5,
            target_name=target_name,
            target_sha256=target_sha256,
            target_version=target_version,
        )


class ReshDataTypePy(ReshDataType):
    def __init__(
        self,
        content: ReshDataTypeContent,
        name: str,
        size: int,
        modifiers: Optional[list[str]] = None,
    ):
        if modifiers is None:
            modifiers = []
        super().__init__(content=content, name=name, size=size, modifiers=modifiers)


class ReshDataTypeContentPrimitivePy(ReshDataTypeContentPrimitive):
    def __init__(self):
        super().__init__(type="PRIMITIVE")


class ReshDataTypeContentPointerPy(ReshDataTypeContentPointer):
    def __init__(self, target_type: ReshTypeSpec | str | ReshDataType):
        super().__init__(type="POINTER", target_type=_wrap_resh_type(target_type))

    def __setattr__(self, name, value):
        if name == "target_type":
            super().__setattr__(name, _wrap_resh_type(value))
        else:
            super().__setattr__(name, value)


class ReshDataTypeContentArrayPy(ReshDataTypeContentArray):
    def __init__(self, base_type: ReshTypeSpec | str | ReshDataType, length: int):
        super().__init__(
            type="ARRAY", base_type=_wrap_resh_type(base_type), length=length
        )

    def __setattr__(self, name, value):
        if name == "base_type":
            super().__setattr__(name, _wrap_resh_type(value))
        else:
            super().__setattr__(name, value)


class ReshDataTypeContentStructurePy(ReshDataTypeContentStructure):
    def __init__(self, members: list[ReshStructureMember]):
        super().__init__(type="STRUCTURE", members=members)


class ReshDataTypeContentUnionPy(ReshDataTypeContentUnion):
    def __init__(self, members: list[ReshStructureMember]):
        super().__init__(type="UNION", members=members)


class ReshDataTypeContentEnumPy(ReshDataTypeContentEnum):
    def __init__(
        self,
        base_type: ReshTypeSpec | str | ReshDataType,
        members: list[ReshEnumMember],
    ):
        super().__init__(
            type="ENUM", base_type=_wrap_resh_type(base_type), members=members
        )

    def __setattr__(self, name, value):
        if name == "base_type":
            super().__setattr__(name, _wrap_resh_type(value))
        else:
            super().__setattr__(name, value)


class ReshDataTypeContentFunctionPy(ReshDataTypeContentFunction):
    def __init__(
        self,
        arguments: Optional[list[ReshFunctionArgument]] = None,
        calling_convention: Optional[str] = None,
        return_type: Optional[ReshTypeSpec | str | ReshDataType] = None,
    ):
        if arguments is None:
            arguments = [] 
        super().__init__(
            type="FUNCTION",
            arguments=arguments,
            calling_convention=calling_convention,
            return_type=_wrap_resh_type(return_type),
        )

    def __setattr__(self, name, value):
        if name == "return_type":
            super().__setattr__(name, _wrap_resh_type(value))
        else:
            super().__setattr__(name, value)


class ReshFunctionArgumentPy(ReshFunctionArgument):
    def __init__(
        self,
        name: Optional[str] = None,
        type: Optional[ReshTypeSpec | str | ReshDataType] = None,
    ):
        super().__init__(name=name, type=_wrap_resh_type(type))

    def __setattr__(self, name, value):
        if name == "type":
            super().__setattr__(name, _wrap_resh_type(value))
        else:
            super().__setattr__(name, value)


class ReshStructureMemberPy(ReshStructureMember):
    def __init__(
        self,
        name: str,
        type: ReshTypeSpec | str | ReshDataType,
        offset: Optional[int] = None,
    ):
        super().__init__(name=name, type=_wrap_resh_type(type), offset=offset)

    def __setattr__(self, name, value):
        if name == "type":
            super().__setattr__(name, _wrap_resh_type(value))
        else:
            super().__setattr__(name, value)


class ReshSymbolPy(ReshSymbol):
    def __init__(
        self,
        address: ReshAddress,
        name: str,
        confidence: Optional[ReshSymbolConfidence] = None,
        labels: Optional[list[ReshLabel]] = None,
        type: Optional[ReshTypeSpec | str | ReshDataType] = None,
    ):
        if labels is None:
            labels = []
        super().__init__(
            address=address,
            name=name,
            confidence=confidence,
            labels=labels,
            type=_wrap_resh_type(type),
        )

    def __setattr__(self, name, value):
        if name == "type":
            super().__setattr__(name, _wrap_resh_type(value))
        else:
            super().__setattr__(name, value)


def _wrap_resh_type(val):
    if val is None:
        return val
    elif isinstance(val, str):
        return ReshTypeSpec(type_name=val, embedded_type=None)
    elif isinstance(val, ReshDataType):
        return ReshTypeSpec(type_name=val.name, embedded_type=val)
    elif isinstance(val, ReshTypeSpec):
        return val
    else:
        raise ReshHelperException("Invalid type!")

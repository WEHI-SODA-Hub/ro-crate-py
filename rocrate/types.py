from __future__ import annotations
from typing import Any, Literal, MutableMapping, Protocol, TypeAlias, TypeGuard, TypeVar, Union, TypedDict, TYPE_CHECKING, overload, runtime_checkable
from typing_extensions import TypeIs
from os import PathLike

if TYPE_CHECKING:
    from rocrate.model import Entity

StrPath: TypeAlias = Union[str, PathLike[str]]
JSON: TypeAlias = dict[str, "JSON"] | list["JSON"] | str | int | float | bool | None
Properties: TypeAlias = dict[str, Any] | None
T = TypeVar("T")
SourceT = TypeVar("SourceT", bound=Union[StrPath, EntityLike])
EntityType: TypeAlias = str | list[str]

def is_str_path(x: Any) -> TypeIs[StrPath]:
    return isinstance(x, (str, PathLike))


EntityLike: TypeAlias = MutableMapping[str, Any]
EntityMap: TypeAlias = dict[str, EntityLike]
# EntityLike: TypeAlias = Union[dict[str, Any], Entity]
# class EntityLike(dict[str, Any]):
#     @overload
#     def __getitem__(self, key: Literal["@id"], /) -> str:
#         ...
#     @overload
#     def __getitem__(self, key: Literal["@type"], /) -> str:
#         ...
#     @overload
#     def __getitem__(self, key: Literal["@graph"], /) -> list[EntityLike]:
#         ...
#     @overload
#     def __getitem__(self, key: Literal["@context"], /) -> Context:
#         ...
#     @overload
#     def __getitem__(self, key: str, /) -> Any:
#         ...
#     def __getitem__(self, key: str, /) -> Any:
#         ...


# @runtime_checkable
# class EntityLike(Protocol):
#     @overload
#     def __getitem__(self, key: Literal["@id"], /) -> str:
#         ...
#     @overload
#     def __getitem__(self, key: Literal["@type"], /) -> str:
#         ...
#     @overload
#     def __getitem__(self, key: Literal["@graph"], /) -> list[EntityLike]:
#         ...
#     @overload
#     def __getitem__(self, key: Literal["@context"], /) -> Context:
#         ...
#     @overload
#     def __getitem__(self, key: str, /) -> Any:
#         ...
#     def __getitem__(self, key: str, /) -> Any:
#         ...

# class JsonLdNode:
#     @overload
#     def __getitem__(self, key: Literal["@id"]) -> str:
#         ...
#     @overload
#     def __getitem__(self, key: Literal["@type"]) -> str:
#         ...
#     # @overload
#     # def __getitem__(self, key: str) -> JSON:
#         ...
#     @overload
#     def __getitem__(self, key: str) -> Any:
#         ...
#     def __getitem__(self, key: str) -> Any:
#         ...

Context: TypeAlias =  str | dict[str, str | EntityLike]

# class JsonLd:
#     @overload
#     def __getitem__(self, key: Literal["@graph"]) -> list[JsonLdNode]:
#         ...
#     @overload
#     def __getitem__(self, key: Literal["@context"]) -> Context:
#         ...
#     def __getitem__(self, key: str) -> Any:
#         ...
# # JsonLdNode = TypedDict("JsonLdNode", {
# #     "@id": str,
# #     "@type": str
# # }, total=False)

# # JsonLd = TypedDict("JsonLd", {
# #     "@graph": list[JsonLdNode],
# #     "@context": Context
# # }, total=False)
# def is_json_ld(obj: Any) -> TypeGuard[JsonLd]:
#     return isinstance(obj, dict) and "@graph" in obj and "@context" in obj

# def is_json_ld_node(obj: Any) -> TypeGuard[JsonLdNode]:
#     return isinstance(obj, dict) and "@id" in obj and "@type" in obj

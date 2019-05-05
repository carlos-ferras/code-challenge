from typing import Callable, Any, Tuple, Union, Dict

CacheKey = Any
CacheValue = Any
ValueLoadCallBack = Callable[[CacheKey], CacheValue]
Address = Union[Tuple[str, int], str]
NetworkPackage = Dict[str, Any]  # this should be converted to TypedDict

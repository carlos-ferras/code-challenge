from typing import Callable, Any

CacheKey = Any
CacheValue = Any
ValueLoadCallBack = Callable[[CacheKey], CacheValue]

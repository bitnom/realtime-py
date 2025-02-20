from typing import Callable, TypeVar

from typing_extensions import ParamSpec

T_ParamSpec = ParamSpec("T_ParamSpec")
T_Retval = TypeVar("T_Retval")

Callback = Callable[T_ParamSpec, T_Retval]

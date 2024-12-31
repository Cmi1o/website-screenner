from functools import wraps
from typing import Callable, ParamSpec, TypeVar

from app.page.loading import page_render_delay

_S = ParamSpec('_S')
_R = TypeVar('_R')


class delayed:
    def __init__(self, delay: int | float = 0.5) -> None:
        self.delay = delay

    def __call__(self, func: Callable[_S, _R]) -> Callable[_S, _R]:
        @wraps(func)
        def wrapper(*args: _S.args, **kwargs: _S.kwargs) -> _R:
            result = func(*args, **kwargs)
            page_render_delay(self.delay)
            return result

        return wrapper

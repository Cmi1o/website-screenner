from functools import wraps
from typing import Callable, ParamSpec, TypeVar

from app.page.loading import page_render_delay


_F_spec = ParamSpec('_F_spec')
_F_return = TypeVar('_F_return')
number = int | float


class create_delay:
    def __init__(self, delay: number=0.5) -> None:
        self.delay = delay
    
    def __call__(
        self, 
        func: Callable[_F_spec, _F_return]
    ) -> Callable[_F_spec, _F_return]:
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            page_render_delay(self.delay)
            return result
        
        return wrapper

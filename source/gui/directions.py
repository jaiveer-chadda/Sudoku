#—— External Imports —————————————————————————————————————————————————————————————————————————
from typing import Generator

#—————————————————————————————————————————————————————————————————————————————————————————————


# using a regular class instead of a dataclass,
#   cos pycharm doesn't like type-hinting dataclasses, and it's kinda important for this case
class Directions:
    def __init__(self, up: int = 0, down: int = 0, left: int = 0, right: int = 0) -> None:
        # using
        self.up = up
        self.down = down
        self.left = left
        self.right = right

    @property
    def top(self) -> int:
        return self.up
    
    @property
    def bottom(self) -> int:
        return self.down
    
    @property
    def n(self) -> int:
        return self.up
    
    @property
    def s(self) -> int:
        return self.down
    
    @property
    def w(self) -> int:
        return self.left
    
    @property
    def e(self) -> int:
        return self.right
    
    def __iter__(self) -> Generator[int, None, None]:
        # this method is here in case I want to treat the object
        #   as a list or iterator of some sort
        for value in (self.up, self.down, self.left, self.right):
            yield value

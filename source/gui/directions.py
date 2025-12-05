#—— External Imports —————————————————————————————————————————————————————————————————————————
from dataclasses import dataclass
from typing import Generator

#—————————————————————————————————————————————————————————————————————————————————————————————


@dataclass
class Directions:
    up: int
    down: int
    left: int
    right: int

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

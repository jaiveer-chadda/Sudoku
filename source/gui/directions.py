#—— External Imports —————————————————————————————————————————————————————————————————————————
from typing import Generator
#—————————————————————————————————————————————————————————————————————————————————————————————


#—— Directions ———————————————————————————————————————————————————————————————————————————————————————————————————————
# I'm using a regular class instead of a dataclass,
#   cos pycharm doesn't like type-hinting dataclasses, and it's kinda important for this case
class Directions:
    
    #—— Initialisation ———————————————————————————————————————————————————————————————————————
    def __init__(self, up: int = 0, down: int = 0, left: int = 0, right: int = 0) -> None:
        self.up:    int = up
        self.down:  int = down
        self.left:  int = left
        self.right: int = right
    
    #—— Properties ———————————————————————————————————————————————————————————————————————————
    #———— Top & Bottom ————————————————————————————
    @property
    def top(self)    -> int: return self.up
    @property
    def bottom(self) -> int: return self.down
    
    #———— NSE&W ———————————————————————————————————
    @property
    def n(self) -> int: return self.up
    @property
    def s(self) -> int: return self.down
    @property
    def w(self) -> int: return self.left
    @property
    def e(self) -> int: return self.right
    
    #———— North, South, East & West ———————————————
    @property
    def north(self) -> int: return self.up
    @property
    def south(self) -> int: return self.down
    @property
    def west(self)  -> int: return self.left
    @property
    def east(self)  -> int: return self.right
    
    #—— Dunder Methods ———————————————————————————————————————————————————————————————————————
    def __iter__(self) -> Generator[int, None, None]:
        # this method is here in case I want to treat the object
        #   as a list or iterator of some sort
        for value in (self.up, self.down, self.left, self.right):
            yield value

#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

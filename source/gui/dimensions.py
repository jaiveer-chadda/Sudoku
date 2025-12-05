#—— External Imports —————————————————————————————————————————————————————————————————————————
from dataclasses import dataclass
from typing import Optional, Generator
#—————————————————————————————————————————————————————————————————————————————————————————————


class NotSquareError(Exception):
    def __init__(self, obj: Dimensions) -> None:
        super().__init__(f"{obj.__repr__()} is not a square.")


#—— Dimension ————————————————————————————————————————————————————————————————————————————————————————————————————————
@dataclass
class Dimensions:
    width: int
    height: Optional[int] = None
    
    #—— Initialisation ———————————————————————————————————————————————————————————————————————
    def __post_init__(self) -> None:
        # if only one value is entered, or if the values are the same
        #   assume the dimensions are a square (nxn)
        self.is_square: bool = (self.width == self.height) or (self.height is None)
        
        if self.is_square:
            self.height = self.width
    
    #—— Properties ———————————————————————————————————————————————————————————————————————————
    #———— Alternatives to width and height ————————
    @property
    def x(self) -> int:
        return self.width
    
    @property
    def y(self) -> int:
        return self.height
    
    #?maybe rename this property
    #?  I don't think 'dimension' rly captures what it is
    @property
    def dimension(self) -> int:
        if not self.is_square:
            raise NotSquareError(self)
        return self.width
    
    #———— area/count ——————————————————————————————
    @property
    def area(self) -> int:
        return self.width * self.height
    
    @property
    def count(self) -> int:
        return self.area
    
    #———— smallest/largest ——————————————————————————————
    @property
    def smallest(self) -> int:
        return min(self.width, self.height)
    
    @property
    def largest(self) -> int:
        return max(self.width, self.height)
    
    #—— Dunder Methods ———————————————————————————————————————————————————————————————————————
    def __repr__(self) -> str:
        return f"Dimensions(width|x={self.width}, height|y={self.height})"
    
    def __iter__(self) -> Generator[int, None, None]:
        # this method is here in case I want to treat the object
        #   as a list or iterator of some sort
        for value in (self.width, self.height):
            yield value
            
#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

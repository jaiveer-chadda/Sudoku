from dataclasses import dataclass
from typing import Optional, Generator


class NotSquareError(Exception):
    def __init__(self, obj: Dimension) -> None:
        super().__init__(f"{obj.__repr__()} is not a square.")


@dataclass
class Dimension:
    width: int
    height: Optional[int] = None
    
    def __post_init__(self) -> None:
        # if only one value is entered, or if the values are the same
        #   assume the dimensions are a square (nxn)
        self.is_square: bool = (self.width == self.height) or (self.height is None)
        
        if self.is_square:
            self.height = self.width
    
    #?maybe rename this property
    #?  I don't think 'dimension' rly captures what it is
    @property
    def dimension(self) -> int:
        if not self.is_square:
            raise NotSquareError(self)
        return self.width
    
    @property
    def x(self) -> int:
        return self.width
    
    @property
    def y(self) -> int:
        return self.height
    
    @property
    def area(self) -> int:
        return self.width * self.height
    
    @property
    def count(self) -> int:
        return self.area
    
    @property
    def largest(self) -> int:
        return max(self.width, self.height)
    
    @property
    def smallest(self) -> int:
        return min(self.width, self.height)
    
    def __repr__(self) -> str:
        return f"Dimensions(width|x={self.width}, height|y={self.height})"
    
    def __iter__(self) -> Generator[int, None, None]:
        for value in (self.width, self.height):
            yield value

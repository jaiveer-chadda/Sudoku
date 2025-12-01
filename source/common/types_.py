#—— External Imports —————————————————————————————————————————————————————————————————————————
from typing import TypeVar, Literal, Iterable  #, Annotated
from enum import StrEnum, IntEnum, auto

#—————————————————————————————————————————————————————————————————————————————————————————————


T: TypeVar = TypeVar('T')

#_Cell_: TypeVar = TypeVar('Cell_')
#_Board_: TypeVar = TypeVar('Board')

type cell_colour = int
type coordinates = tuple[int, int]

# type Cell_ = object
type Board = 'Board'

type cell_insert_type = Literal["value", "corner", "centre", "colour"]


class CellInsertType(StrEnum):
    VALUE  = auto()
    CORNER = auto()
    CENTRE = auto()
    COLOUR = auto()
    

class ANSIColour(IntEnum):
    BLACK   = 0,
    RED     = 1,
    GREEN   = 2,
    YELLOW  = 3,
    BLUE    = 4,
    MAGENTA = 5,
    CYAN    = 6,
    WHITE   = 7


# type board_flat = list[Cell_]
# type board_matrix = list[list[Cell_]]

#_type board_flat = list[Annotated[object, 'Cell']]
#_type board_matrix = list[list[Annotated[object, 'Cell']]]

type board_flat_raw = Iterable[int]
type board_matrix_raw = Iterable[Iterable[int]]

#—— External Imports —————————————————————————————————————————————————————————————————————————
from typing import TypeVar, Literal, Iterable  #, Annotated

#—————————————————————————————————————————————————————————————————————————————————————————————


T: TypeVar = TypeVar('T')

#_Cell_: TypeVar = TypeVar('Cell_')
#_Board_: TypeVar = TypeVar('Board')

type colour = int
type coordinates = tuple[int, int]

# type Cell_ = object
type Board = 'Board'

type cell_insert_type = Literal["value", "corner", "centre", "colour"]

# type board_flat = list[Cell_]
# type board_matrix = list[list[Cell_]]

#_type board_flat = list[Annotated[object, 'Cell']]
#_type board_matrix = list[list[Annotated[object, 'Cell']]]

type board_flat_raw = Iterable[int]
type board_matrix_raw = Iterable[Iterable[int]]

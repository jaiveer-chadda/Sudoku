#—— External Imports —————————————————————————————————————————————————————————————————————————
from typing import TypeVar, Literal, Iterable  #, Annotated

#—————————————————————————————————————————————————————————————————————————————————————————————


T: TypeVar = TypeVar('T')

#_ Cell_: TypeVar = TypeVar('Cell_')
#_ Board_: TypeVar = TypeVar('Board_')

type colour = int
type coordinates = tuple[int, int]

type Cell_ = 'Cell'
type Board_ = 'Board'

type cell_insert_type = Literal["value", "corner", "centre", "colour"]

type board_flat = list[Cell_]
type board_matrix = list[list[Cell_]]

#_ type board_flat = list[Annotated[object, 'Cell']]
#_ type board_matrix = list[list[Annotated[object, 'Cell']]]

type board_flat_raw = Iterable[int]
type board_matrix_raw = Iterable[Iterable[int]]

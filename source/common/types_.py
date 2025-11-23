from typing import TypeVar, Literal, Iterable

T: TypeVar = TypeVar('T')

type colour = int
type coordinates = tuple[int, int]

type Cell_ = 'Cell'
type Board_ = 'Board'

type cell_insert_type = Literal["value", "corner", "centre", "colour"]

type board_flat = list[Cell_]
type board_matrix = list[list[Cell_]]

type board_flat_raw = Iterable[int]
type board_matrix_raw = Iterable[Iterable[int]]

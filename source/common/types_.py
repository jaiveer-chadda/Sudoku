from typing import TypeVar, Literal, Iterable

T: TypeVar = TypeVar('T')

type colour = int
type coordinates = tuple[int, int]

type cell_insert_type = Literal["value", "corner", "centre", "colour"]

type board_flat = list["Cell"]
type board_matrix = list[list["Cell"]]

type board_flat_raw = Iterable[int]
type board_matrix_raw = Iterable[Iterable[int]]

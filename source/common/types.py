
from typing import TypeVar, Literal, Iterable


T = TypeVar('T')

type colour = int

type coordinates = tuple[int, int]

type cell_insert_type = Literal["value", "corner", "centre", "colour"]

type board_flat = tuple["Cell", ...]
type board_matrix = tuple[tuple["Cell", ...], ...]

type board_flat_raw = Iterable[int]
type board_matrix_raw = Iterable[Iterable[int]]

# type board_flat_raw = tuple[
#     int, int, int, int, int, int, int, int, int,
#     int, int, int, int, int, int, int, int, int,
#     int, int, int, int, int, int, int, int, int,
#     int, int, int, int, int, int, int, int, int,
#     int, int, int, int, int, int, int, int, int,
#     int, int, int, int, int, int, int, int, int,
#     int, int, int, int, int, int, int, int, int,
#     int, int, int, int, int, int, int, int, int,
#     int, int, int, int, int, int, int, int, int
# ]
#
# type board_flat = tuple[
#     Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell,
#     Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell,
#     Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell,
#     Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell,
#     Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell,
#     Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell,
#     Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell,
#     Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell,
#     Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell, Cell
# ]
#
# type board_matrix_raw = tuple[
#     tuple[int, int, int, int, int, int, int, int, int],
#     tuple[int, int, int, int, int, int, int, int, int],
#     tuple[int, int, int, int, int, int, int, int, int],
#     tuple[int, int, int, int, int, int, int, int, int],
#     tuple[int, int, int, int, int, int, int, int, int],
#     tuple[int, int, int, int, int, int, int, int, int],
#     tuple[int, int, int, int, int, int, int, int, int],
#     tuple[int, int, int, int, int, int, int, int, int],
#     tuple[int, int, int, int, int, int, int, int, int]
# ]

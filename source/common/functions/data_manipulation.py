#—— External Imports ——————————————————————————————————————————————————————————————————————————
from itertools import chain
from typing import Iterable

#—— Project Imports ——————————————————————————————————————————————————————————————————————————
#————— Consts & Types ———————————————————————————
from source.common.types_ import T

#————— Objects ——————————————————————————————————
from source.objects.cell import Cell
#—————————————————————————————————————————————————————————————————————————————————————————————


def flatten_matrix_to_1d_tuple(list_to_flatten: Iterable[Iterable[T]]) -> tuple[T, ...]:
    # takes a matrix, flattens it, then casts it to a tuple
    #   mostly used to take a board given as a matrix, and convert it to an indexed format
    #   eg.  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    #        =>
    #        (1, 2, 3, 4, 5, 6, 7, 8, 9)
    return tuple(chain.from_iterable(list_to_flatten))


def get_set_of_values_from_cells(from_: Iterable[Cell]) -> set[int]:
    # takes an Iterable of Cells, finds each of their value, and returns those values as a set
    #   mostly used for finding the set of values that a cell can see
    return set(map(lambda cell: cell.value, from_))

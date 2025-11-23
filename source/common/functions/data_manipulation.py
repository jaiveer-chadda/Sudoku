from itertools import chain
from typing import Iterable

# noinspection PyUnresolvedReferences
from common.types_ import T, Cell_


def flatten_matrix_to_1d_tuple(list_to_flatten: Iterable[Iterable[T]]) -> tuple[T, ...]:
    return tuple(chain.from_iterable(list_to_flatten))


def get_all_values(from_: Iterable[Cell_]) -> set[int]:
    return set(map(lambda cell: cell.value, from_))

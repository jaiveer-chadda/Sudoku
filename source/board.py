from dataclasses import dataclass, field
from itertools import chain
from typing import Optional, Iterable, overload

from common.types import T, board_matrix_raw, board_flat_raw, board_flat, colour, coordinates, cell_insert_type


def flatten_matrix_to_1d_tuple(list_to_flatten: Iterable[Iterable[T]]) -> tuple[T, ...]:
    return tuple(chain.from_iterable(list_to_flatten))


def _convert_ints_to_cell_board(int_list: Iterable[int]) -> board_flat:
    return tuple(map(lambda value: Cell(value), int_list))


# def _get_coords_from_index(index: int) -> tuple[int, int]:
#     return index % 9, index // 9


def _get_index_from_coords(x: int, y: int) -> int:
    return (x % 9) + (y * 9)


def _get_parent_box_from_coords(x: int, y: int) -> int:
    return (x // 3) + (y // 3) * 3


@dataclass
class Cell:
    index: int
    
    value: Optional[int] = None
    corner_candidates: list[int] = field(default_factory=list)
    central_candidates: list[int] = field(default_factory=list)
    colours: list[colour] = field(default_factory=list)
    
    @property
    def x(self) -> int:
        return self.index % 9
    
    @property
    def y(self) -> int:
        return self.index // 9
    
    @property
    def coords(self) -> coordinates:
        return self.x, self.y
    
    @coords.setter
    def coords(self, xy: coordinates):
        self.index = _get_index_from_coords(*xy)
    
    @property
    def parent_box(self) -> int:
        return _get_parent_box_from_coords(*self.coords)


class Board:
    def __init__(self, board: board_matrix_raw) -> None:
        _flat_board: board_flat_raw  = flatten_matrix_to_1d_tuple(board)
        self.board: board_flat = _convert_ints_to_cell_board(_flat_board)
    
    @overload
    def fill_cell(self, input_: int, type_: cell_insert_type, index: int) -> None:
        pass

    @overload
    def fill_cell(self, input_: int, type_: cell_insert_type, coords: coordinates) -> None:
        pass
    
    def fill_cell(self,
                  input_: int | colour,
                  type_: cell_insert_type,
                  index: Optional[int]=None,
                  coords: Optional[coordinates]=None) -> None:
        
        if not ((index is None) ^ (coords is None)):
            raise ValueError(
                "'fill_cell' takes an input of at least one of 'index: int', "
                "or 'coords: tuple[int, int]', but not both."
            )
        
        index: int = _get_index_from_coords(*coords) if coords is not None else index
        
        if (input_ is colour) and type_ in ("value", "corner", "centre"):
            raise TypeError("'input_' must be of type 'int'")
        elif input_ is not colour and type_ == "colour":
            raise TypeError("'input_' must be of type 'colour'")
        
        match type_:
            case "value":
                self.board[index].value = input_
            case "corner":
                self.board[index].corner_candidates.append(input_)
            case "centre":
                self.board[index].central_candidates.append(input_)
            case "colour":
                self.board[index].colours.append(input_)
            case _:
                raise ValueError("Invalid cell type")



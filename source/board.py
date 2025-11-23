from dataclasses import dataclass, field
from itertools import chain
from typing import Optional, Iterable, overload

from common.types import T, board_matrix_raw, board_flat_raw, board_flat, colour, coordinates, cell_insert_type


ALL_OPTIONS: set[int] = set(range(1, 10))


def flatten_matrix_to_1d_tuple(list_to_flatten: Iterable[Iterable[T]]) -> tuple[T, ...]:
    return tuple(chain.from_iterable(list_to_flatten))
    

def _get_index_from_coords(x: int, y: int) -> int:
    return (x % 9) + (y * 9)


def _get_parent_box_from_coords(x: int, y: int) -> int:
    return (x // 3) + (y // 3) * 3


def get_all_values(from_: Iterable[Cell]) -> set[int]:
    return set(map(lambda cell: cell.value, from_))


def format_set(input_set: set[int]) -> str:
    return "{"+"".join([f"{i if i in input_set else " "}{", " if i!=9 else ""}" for i in range(1, 10)])+"} "


def format_set_2(input_set: set[int]) -> str:
    return "".join([f"{i if i in input_set else " "}{" " if i!=9 else ""}" for i in range(1, 10)])+" "


@dataclass(eq=False)
class Cell:
    index: int
    _parent: Board
    
    value: Optional[int] = None
    possible_options: set[int] = field(default_factory=lambda: ALL_OPTIONS.copy())
    
    corner_candidates: list[int] = field(default_factory=list)
    central_candidates: list[int] = field(default_factory=list)
    colours: list[colour] = field(default_factory=list)
    
    def __post_init__(self) -> None:
        self._parent.columns[self.x].add(self)
        self._parent.rows[self.y].add(self)
        self._parent.boxes[self.parent_box].add(self)
        
        # the board is stored such that the value of each cell is 0 if it's undefined -
        #  this just fixes that for easier logic
        if self.value == 0:
            self.value = None
            
        if self.value is not None:
            self.possible_options = {self.value}
        
    def remove_from_options(self, to_remove: int) -> None:
        self.possible_options.remove(to_remove)
        
        if len(self.possible_options) == 1:
            self.value = list(self.possible_options)[0]
            # print(f"changed {self.coords} to {self.value}")

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
    
    @property
    def sees(self) -> set[Cell]:
        return self._parent.columns[self.x] | self._parent.rows[self.y] | self._parent.boxes[self.parent_box]
    
    def __str__(self) -> str:
        return str(self.value) if self.value is not None else "-"
    
    def __repr__(self) -> str:
        return str(self.possible_options) if self.possible_options is not None else f".{self.value}."


class Board:
    def __init__(self, board: board_matrix_raw, *, do_auto_solve: bool=True) -> None:
        self.columns: list[set[Cell]] = [set() for _ in range(9)]
        self.rows: list[set[Cell]] = [set() for _ in range(9)]
        self.boxes: list[set[Cell]] = [set() for _ in range(9)]
        
        self.board: Optional[board_flat] = None  # just initialising the property
        
        _flat_board: board_flat_raw  = flatten_matrix_to_1d_tuple(board)
        self.board: board_flat = self._create_board_from_ints(_flat_board)
        if do_auto_solve:
            self._pre_backtracking_solve()
    
    def _create_board_from_ints(self, int_list: Iterable[int]) -> board_flat:
        return [Cell(index=i, _parent=self, value=val) for i, val in enumerate(int_list)]

    def _pre_backtracking_solve(self):
        something_changed: bool = True
        # repeat until you can make no further progress
        while something_changed:
            something_changed = False
            # iterate through every cell in the board
            for cell_to_check in self.board:
                # ignore the cells that don't have a value
                if cell_to_check.value is None:
                    continue
                # for all cells with a value, check which cells it can see,
                #  and remove its value from those seen cells
                for cell_to_change in cell_to_check.sees:
                    try:
                        cell_to_change.remove_from_options(cell_to_check.value)
                        something_changed = True
                    # if a KeyError is raised,
                    #  it means that that value wasn't in the cell we tried to remove it from
                    #   which doesn't matter, so it's ignored
                    except KeyError:
                        pass
                    
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
    
    def print_candidates(self) -> None:
        for i, cell in enumerate(self.board):
            print(f"{format_set(cell.possible_options)}", end=("\n" if i%9==8 else ""))
        
        # line: str = "│ {} {} {} │ {} {} {} │ {} {} {} │"
        # blank: str = " "*18
        # empty_line: str = f"│ {blank} {blank} {blank} │ {blank} {blank} {blank} │ {blank} {blank} {blank} │"
        # to_format: str = f"""
        # ┌{'—'*58}┬{'—'*58}┬{'—'*58}┐
        # {line}
        # {empty_line}
        # {line}
        # {empty_line}
        # {line}
        # ├{'—'*58}┼{'—'*58}┼{'—'*58}┤
        # {line}
        # {empty_line}
        # {line}
        # {empty_line}
        # {line}
        # ├{'—'*58}┼{'—'*58}┼{'—'*58}┤
        # {line}
        # {empty_line}
        # {line}
        # {empty_line}
        # {line}
        # └{'—'*58}┴{'—'*58}┴{'—'*58}┘
        # """
        #
        # print(to_format.format(
        #     *[format_set_2(i.possible_options) for i in self.board]
        # ))
    
    def __str__(self) -> str:
        return ("""
        ┌───────┬───────┬───────┐
        │ {} {} {} │ {} {} {} │ {} {} {} │
        │ {} {} {} │ {} {} {} │ {} {} {} │
        │ {} {} {} │ {} {} {} │ {} {} {} │
        ├───────┼───────┼───────┤
        │ {} {} {} │ {} {} {} │ {} {} {} │
        │ {} {} {} │ {} {} {} │ {} {} {} │
        │ {} {} {} │ {} {} {} │ {} {} {} │
        ├───────┼───────┼───────┤
        │ {} {} {} │ {} {} {} │ {} {} {} │
        │ {} {} {} │ {} {} {} │ {} {} {} │
        │ {} {} {} │ {} {} {} │ {} {} {} │
        └───────┴───────┴───────┘
        """.format(
            *[f"{i.value if i.value not in (0, None) else " "}" for i in self.board]
        ))

    def __repr__(self) -> str:
        return "".join(
            [f"{
                val if (val := self.board[i].value)!=0 else " "
            }{
                "\n" if i % 9 == 8 else " "
            }"
             for i in range(len(self.board))]
        )



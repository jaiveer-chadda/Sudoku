#—— External Imports —————————————————————————————————————————————————————————————————————————
from typing import Optional, Iterable, overload, Literal

#—— Project Imports ——————————————————————————————————————————————————————————————————————————
#————— Consts & Types ———————————————————————————
from source.common.constants import BOARD_SIZE
from source.common.types_ import board_matrix_raw, board_flat_raw, board_flat, colour, coordinates, cell_insert_type

#————— Objects ——————————————————————————————————
from source.objects.cell import Cell

#————— Functions ————————————————————————————————
from source.common.functions.calculations import get_index_from_coords
from source.common.functions.data_manipulation import flatten_matrix_to_1d_tuple
from source.common.functions.output_formatting import format_set, get_formatted_board
#—————————————————————————————————————————————————————————————————————————————————————————————


class Board:
    #—— Initialisation ———————————————————————————————————————————————————————————————————————
    def __init__(self, board: board_matrix_raw, *, do_auto_solve: bool=True) -> None:
        self.columns: list[set[Cell]] = [set() for _ in range(BOARD_SIZE)]
        self.rows: list[set[Cell]] = [set() for _ in range(BOARD_SIZE)]
        self.boxes: list[set[Cell]] = [set() for _ in range(BOARD_SIZE)]
        
        self.board: Optional[board_flat] = None  # just initialising the property
        
        _flat_board: board_flat_raw = flatten_matrix_to_1d_tuple(board)
        self.board: board_flat = self._create_board_from_ints(_flat_board)
        
        if do_auto_solve:
            self._changed_board_state: bool = True
            self.solve_board()
    
    #—— Private Methods ——————————————————————————————————————————————————————————————————————
    #———— _create_board_from_ints() ———————————————
    def _create_board_from_ints(self, int_list: Iterable[int]) -> board_flat:
        return [Cell(index=i, _parent=self, value=val, is_given_value=True) for i, val in enumerate(int_list)]
    
    #———— _remove_invalid_candidates() ————————————
    def _remove_invalid_candidates(self, cell_to_check: Cell) -> Literal[0, 1]:
        # ignore the cells that don't have a value
        if cell_to_check.has_no_value:
            return 1
        # for all cells with a value, check which cells it can see,
        #   and remove its value from those seen cells
        for cell_to_change in cell_to_check.sees:
            try:
                cell_to_change.remove_from_options(cell_to_check.value)
                self._changed_board_state = True
            # if a {{KeyError}} is raised
            #   it means that that value wasn't an option in the cell we tried to remove it from
            #   which doesn't matter, so it's ignored
            # it's also easier and quicker to handle it this way,
            #   rather than checking whether the value actually _is_ an option before removing it
            except KeyError:
                #{{Key Error Excepted}}
                pass
        return 0
    
    #———— solve_board() ———————————————————————————
    def solve_board(self) -> None:
        print(get_formatted_board(self.board, draw_box_borders=True))
        # repeat until you can make no further progress
        while self._changed_board_state:
            self._changed_board_state = False
            
            # iterate through every cell in the board
            for cell_to_check in self.board:
                self._remove_invalid_candidates(cell_to_check)
                    
    #—— General Methods ——————————————————————————————————————————————————————————————————————
    #———— fill_cell() —————————————————————————————
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
        
        index: int = get_index_from_coords(*coords) if coords is not None else index
        
        if (input_ is colour) and type_ in ("value", "corner", "centre"):
            raise TypeError("'input_' must be of type 'int'")
        elif input_ is not colour and type_ == "colour":
            raise TypeError("'input_' must be of type 'colour'")
        
        match type_:
            case "value":  self.board[index].value = input_
            case "corner": self.board[index].corner_candidates.append(input_)
            case "centre": self.board[index].central_candidates.append(input_)
            case "colour": self.board[index].colours.append(input_)
            case _:
                raise ValueError("Invalid cell type")
    
    #———— print_candidates() ——————————————————————
    def print_candidates(self) -> None:
        for i, cell in enumerate(self.board):
            print(f"{format_set(cell.possible_options)}", end=("\n" if i % BOARD_SIZE == BOARD_SIZE-1 else ""))
    
    #—— Dunder Methods ———————————————————————————————————————————————————————————————————————
    def __str__(self) -> str:
        return get_formatted_board(self.board, draw_box_borders=True)

    def __repr__(self) -> str:
        return get_formatted_board(self.board, draw_box_borders=False)

#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

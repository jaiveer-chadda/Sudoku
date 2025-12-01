#—— External Imports —————————————————————————————————————————————————————————————————————————
from typing import Optional, Iterable, overload

#—— Project Imports ——————————————————————————————————————————————————————————————————————————
#————— Consts & Types ———————————————————————————
from source.common.constants import BOARD_SIZE
from source.common.types_ import board_matrix_raw, board_flat_raw, cell_colour, coordinates, CellInsertType

#————— Objects ——————————————————————————————————
from source.objects.cell import Cell, validate_input_type, board_flat

#————— Solver ———————————————————————————————————
from source.objects.board.solver.main import get_solved_board

#————— Functions ————————————————————————————————
from source.common.functions.calculations import get_index_from_coords
from source.common.functions.data_manipulation import flatten_matrix_to_1d_tuple
from source.common.functions.output_formatting import format_set, get_formatted_board
#—————————————————————————————————————————————————————————————————————————————————————————————


def _validate_unique_input(index: int, coords: coordinates) -> None:
    if not ((index is None) ^ (coords is None)):
        raise TypeError(
            "'fill_cell' takes an input of at least one of 'index: int', "
            "or 'coords: tuple[int, int]', but not both."
        )


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
            # self._changed_board_state: bool = True
            self.solve_board()
    
    #—— General Methods ——————————————————————————————————————————————————————————————————————
    #———— solve_board() ———————————————————————————
    def solve_board(self) -> None:
        # print(str(self))
        self.board = get_solved_board(self.board)
        
    #———— _create_board_from_ints() ———————————————
    def _create_board_from_ints(self, int_list: Iterable[int]) -> board_flat:
        return [Cell(index=i, _parent=self, value=val, is_given_value=True) for i, val in enumerate(int_list)]
    
    #———— _debug_print_candidates() ————————————————
    def _debug_print_candidates(self) -> None:
        for i, cell in enumerate(self.board):
            print(f"{format_set(cell.possible_options)}", end=("\n" if i % BOARD_SIZE == BOARD_SIZE-1 else ""))
    
    #———— fill_cell() —————————————————————————————
    @overload
    def fill_cell(self, number_to_add: int | cell_colour, type_: CellInsertType, index: int) -> None:
        pass

    @overload
    def fill_cell(self, number_to_add: int | cell_colour, type_: CellInsertType, coords: coordinates) -> None:
        pass
    
    def fill_cell(self,
                  number_to_add: int | cell_colour,
                  type_: CellInsertType,
                  index: Optional[int]=None,
                  coords: Optional[coordinates]=None
                  ) -> None:
        _validate_unique_input(index, coords)
        validate_input_type(number_to_add, type_)
        
        index: int = get_index_from_coords(*coords) if (coords is not None) else index
        self.board[index].fill_or_add_number(number_to_add, type_)
    
    #—— Dunder Methods ———————————————————————————————————————————————————————————————————————
    def __str__(self) -> str:
        return get_formatted_board(self.board, draw_box_borders=True)

    def __repr__(self) -> str:
        return get_formatted_board(self.board, draw_box_borders=False)

#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

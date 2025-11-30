#—— External Imports —————————————————————————————————————————————————————————————————————————
from typing import Optional

#—— Project Imports ——————————————————————————————————————————————————————————————————————————s
#————— Consts & Types ———————————————————————————
from source.common.constants import ALL_OPTIONS

#————— Objects ——————————————————————————————————
from source.objects.cell import Cell, board_flat

#————— Functions ————————————————————————————————
from source.common.functions.output_formatting import print_pretty_board
#—————————————————————————————————————————————————————————————————————————————————————————————


def get_solved_board(board: board_flat) -> board_flat:
    for solving_function in (_basic_solve, _backtracking_solve):
        print_pretty_board(board)
        board = solving_function(board)
    return board


def _basic_solve(board: board_flat) -> board_flat:
    _changed_board_state: bool = True
    # repeat until you can make no further progress
    while _changed_board_state:
        _changed_board_state = False
        
        # iterate through every cell in the board
        for cell in board:
            _changed_board_state = _remove_invalid_candidates(cell, _changed_board_state)
            if _changed_board_state is None:
                continue
    return board


def _remove_invalid_candidates(cell_to_check: Cell, _has_changed: bool) -> Optional[bool]:
    # ignore the cells that don't have a value
    if not cell_to_check.has_some_value:
        return _has_changed
    # for all cells with a value, check which cells it can see,
    #   and remove its value from those seen cells
    for cell_to_change in cell_to_check.sees:
        try:
            cell_to_change.remove_from_options(cell_to_check.value)
            _has_changed = True
        # if a {{KeyError}} is raised
        #   it means that that value wasn't an option in the cell we tried to remove it from
        #   which doesn't matter, so it's ignored
        # it's also easier and quicker to handle it this way,
        #   rather than checking whether the value actually _is_ an option before removing it
        except KeyError:
            #{{Key Error Excepted}}
            pass
    return _has_changed


def _backtracking_solve(_board: board_flat) -> board_flat:
    def _is_valid_assignment(cell: Cell, val: int) -> bool:
        # cell.sees contains the cell itself (because cell was added to parent sets),
        #   so skip the same object check
        return not any(other is not cell and other.value == val for other in cell.sees)
    
    def solve_recursive(cell_index: int) -> bool:
        if cell_index >= len(_board):
            return True
        
        cell: Cell = _board[cell_index]
        
        if cell.has_some_value:
            return solve_recursive(cell_index+1)
            
        for val_to_try in ALL_OPTIONS:
            if val_to_try not in cell.possible_options:
                continue
            if not _is_valid_assignment(cell, val_to_try):
                continue
            
            cell.value = val_to_try
            if solve_recursive(cell_index+1):
                return True
            cell.value = None
            
        return False
        
    solve_recursive(0)
    return _board


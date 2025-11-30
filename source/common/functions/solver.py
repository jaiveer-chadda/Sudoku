#—— External Imports —————————————————————————————————————————————————————————————————————————
from typing import Optional, Literal

#————— Objects ——————————————————————————————————
from source.objects.cell import Cell, board_flat

#————— Functions ————————————————————————————————
from source.common.functions.output_formatting import print_pretty_board
#—————————————————————————————————————————————————————————————————————————————————————————————


SOLUTION_LIMIT: int = 1


def get_solved_board(board: board_flat) -> board_flat:
    print_pretty_board(board)
    board = _basic_solve(board)
    
    print_pretty_board(board)
    solve_result = _backtracking_solve(board)
    print(solve_result)
    
    if not isinstance(solve_result, str):
        return solve_result
    raise Exception(solve_result)


def _basic_solve(board: board_flat) -> board_flat:
    _changed_board_state: bool = True
    # repeat until you can make no further progress
    while _changed_board_state:
        _changed_board_state = False
        # iterate through every cell in the board
        for cell in board:
            _changed_board_state = _remove_invalid_candidates(cell, _changed_board_state)
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


def _is_valid_assignment(cell: Cell, val: int) -> bool:
    for other in cell.sees:
        if other is not cell and other.value == val:
            return False
    return True


def _backtracking_solve(_board: board_flat) -> board_flat | Literal["No solution found", "Multiple solutions found"]:
    solution_count: int = 0
    first_solution: Optional[board_flat] = None
    
    def solve_recursive(cell_index: int=0) -> bool:
        nonlocal solution_count, first_solution
        
        if cell_index >= len(_board):
            solution_count += 1
            
            # Store the first solution found
            if first_solution is None:
                first_solution = [c.copy() for c in _board]
            
            return solution_count > SOLUTION_LIMIT  # stop early if more than one solution is found
        
        cell: Cell = _board[cell_index]
        if cell.has_some_value:
            return solve_recursive(cell_index+1)
        
        for val_to_try in cell.possible_options:
            if not _is_valid_assignment(cell, val_to_try):
                continue
            
            cell.value = val_to_try
            
            if solve_recursive(cell_index + 1):
                return True
            cell.value = None  # backtrack
            
        return False  # keep searching
    
    solve_recursive()
    
    match solution_count:
        case 0:
            return "No solution found"
        case _ if solution_count > SOLUTION_LIMIT:
            return "Multiple solutions found"
        case _:
            return first_solution

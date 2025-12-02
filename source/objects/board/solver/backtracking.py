#—— External Imports —————————————————————————————————————————————————————————————————————————
from typing import Optional, Literal
from os import system

#—— Project Imports ——————————————————————————————————————————————————————————————————————————
#————— Objects ——————————————————————————————————
from source.objects.cell import Cell, board_flat

#————— Functions ————————————————————————————————
from source.common.functions.output_formatting import print_pretty_board
#—————————————————————————————————————————————————————————————————————————————————————————————


SOLUTION_LIMIT: int = 1


def _is_valid_assignment(cell: Cell, val: int) -> bool:
    for other in cell.sees:
        if other is not cell and other.value == val:
            return False
    return True


def backtracking_solve(_board: board_flat) -> board_flat | Literal["No solution found", "Multiple solutions found"]:
    iterations: int = 0
    
    solution_count: int = 0
    first_solution: Optional[board_flat] = None
    
    def solve_recursive(cell_index: int=0) -> bool:
        nonlocal solution_count, first_solution, iterations
        
        iterations += 1
        # print_pretty_board(_board)
        # system('clear')
        
        if cell_index >= len(_board):
            solution_count += 1
            
            # Store the first solution found
            if first_solution is None:
                first_solution = [c.copy() for c in _board]
            
            return solution_count > SOLUTION_LIMIT  # stop early if more than one solution is found
        
        cell: Cell = _board[cell_index]
        if cell.has_some_value:
            return solve_recursive(cell_index+1)
        
        for val_to_try in list(cell.possible_options)[::-1]:
            if not _is_valid_assignment(cell, val_to_try):
                continue
                
            cell.value = val_to_try
            
            if solve_recursive(cell_index + 1):
                return True
            cell.value = None  # backtrack
        
        return False  # keep searching
    
    try:
        solve_recursive()
    except KeyboardInterrupt:
        print(f"\n\n{iterations:,d}")
        quit()
    
    print(f"\n{iterations:,d}")
    match solution_count:
        case 0:
            return "No solution found"
        case _ if solution_count > SOLUTION_LIMIT:
            return "Multiple solutions found"
        case _:
            return first_solution

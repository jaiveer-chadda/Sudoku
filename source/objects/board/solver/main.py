#—— External Imports —————————————————————————————————————————————————————————————————————————
from typing import Literal

#—— Project Imports ——————————————————————————————————————————————————————————————————————————
#————— Objects ——————————————————————————————————
from source.objects.cell import board_flat

#————— Solver ———————————————————————————————————
from source.objects.board.solver.candidate_checker import basic_solve
from source.objects.board.solver.backtracking import backtracking_solve

#————— Functions ————————————————————————————————
from source.common.functions.output_formatting import print_pretty_board
#—————————————————————————————————————————————————————————————————————————————————————————————


class SolutionCountError(Exception):
    def __init__(self, message) -> None:
        self.message: Literal["No solution found", "Multiple solutions found"] = message
        super().__init__(self.message)


def get_solved_board(board: board_flat) -> board_flat:
    print_pretty_board(board)
    board = basic_solve(board)
    
    print_pretty_board(board)
    solve_result = backtracking_solve(board)
    
    if isinstance(solve_result, str):
        raise SolutionCountError(solve_result)
    
    return solve_result
    

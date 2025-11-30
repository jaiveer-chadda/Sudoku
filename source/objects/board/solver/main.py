#—— Project Imports ——————————————————————————————————————————————————————————————————————————
#————— Objects ——————————————————————————————————
from source.objects.cell import board_flat

#————— Solver ———————————————————————————————————
from source.objects.board.solver.candidate_checker import basic_solve
from source.objects.board.solver.backtracking import backtracking_solve

#————— Functions ————————————————————————————————
from source.common.functions.output_formatting import print_pretty_board
#—————————————————————————————————————————————————————————————————————————————————————————————


def get_solved_board(board: board_flat) -> board_flat:
    print_pretty_board(board)
    board = basic_solve(board)
    
    print_pretty_board(board)
    solve_result = backtracking_solve(board)
    print(solve_result)
    
    if not isinstance(solve_result, str):
        return solve_result
    raise Exception(solve_result)

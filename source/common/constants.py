#—— External Imports —————————————————————————————————————————————————————————————————————————
from math import sqrt

#—— Project Imports ——————————————————————————————————————————————————————————————————————————
#————— Consts & Types ———————————————————————————
from source.common.types_ import board_matrix_raw
#—————————————————————————————————————————————————————————————————————————————————————————————


def _int_sqrt(int_: int) -> int:
    # just a simple function that asserts that the inputted integer is a square number,
    #   and returns its square root
    if not isinstance(result := int(sqrt(int_)), int):
        raise ValueError(f"sqrt(int_) must be an integer\n{int_=}, {sqrt(int_)=}, {result=}")
    return int(result)


BOARD_SIZE: int = 9  # the board dimensions, eg =9 for a standard 9x9 sudoku board
BOX_SIZE: int = _int_sqrt(BOARD_SIZE)  # the sub-box dimensions (=3 for a standard sudoku board)

ALL_OPTIONS: tuple[int] = tuple(range(1, BOARD_SIZE + 1))  # a tuple containing the numbers 1 -> 9
ALL_OPTIONS_SET: set[int] = set(range(1, BOARD_SIZE + 1))  # a  set  containing the numbers 1 -> 9

#? temp
#    it's just here while I create the solver
BOARD_OPTIONS: dict[str, board_matrix_raw] = {
    "easy":
        [  # solved
            [0, 0, 2, 3, 7, 0, 1, 5, 4],
            [0, 5, 1, 0, 4, 0, 8, 0, 2],
            [8, 3, 4, 0, 1, 2, 0, 0, 0],
            [2, 0, 0, 6, 0, 0, 0, 9, 3],
            [6, 0, 8, 2, 0, 4, 0, 0, 0],
            [0, 0, 0, 1, 9, 0, 0, 0, 8],
            [5, 4, 9, 0, 0, 0, 0, 7, 0],
            [0, 8, 0, 0, 0, 9, 2, 4, 0],
            [1, 0, 0, 0, 0, 3, 5, 0, 0]
        ],
    "medium":
        [  # solvable with some more techniques like double-finding
            [0, 1, 2, 0, 7, 0, 0, 0, 3],
            [0, 7, 0, 1, 3, 4, 2, 0, 0],
            [3, 0, 6, 2, 8, 0, 0, 7, 0],
            [0, 0, 7, 4, 9, 3, 0, 0, 5],
            [1, 9, 4, 5, 2, 8, 0, 3, 0],
            [5, 8, 3, 0, 1, 0, 9, 0, 0],
            [7, 0, 0, 0, 0, 0, 0, 0, 8],
            [0, 0, 0, 8, 0, 2, 0, 0, 0],
            [0, 0, 8, 0, 0, 0, 4, 0, 0]
        ],
    "hard":
        [  # not solvable through basic techniques
            [9, 1, 7, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 6, 0, 0, 0, 0, 9],
            [0, 0, 0, 0, 0, 0, 0, 8, 0],
            [2, 5, 0, 0, 8, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 7, 0, 0, 0],
            [0, 0, 9, 0, 3, 5, 0, 4, 0],
            [0, 6, 0, 0, 0, 4, 0, 0, 5],
            [0, 0, 0, 8, 0, 0, 2, 0, 0],
            [0, 9, 4, 0, 0, 0, 0, 0, 0]
        ],
}

#? also temp
#    the program will eventually take the board in from somewhere else
#    (or it'll make its own), but this is just temporary,
#    to make it easier for me to handle
board_input: board_matrix_raw = BOARD_OPTIONS["easy"]

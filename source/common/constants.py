# — External Imports —————————————————————————————
from math import sqrt

# — Project Imports —————————————————————————————
# ———— Consts & Types ———————————————————————————
from common.types_ import board_matrix_raw


def _int_sqrt(int_: int) -> int:
    if not isinstance(result := int(sqrt(int_)), int):
        raise ValueError(f"sqrt(int_) must be an integer\n{int_=}, {sqrt(int_)=}, {result=}")
    return int(result)


BOARD_SIZE: int = 9
BOX_SIZE: int = _int_sqrt(BOARD_SIZE)

ALL_OPTIONS: tuple[int] = tuple(range(1, BOARD_SIZE + 1))
ALL_OPTIONS_SET: set[int] = set(range(1, BOARD_SIZE + 1))


# solved
raw_board: board_matrix_raw = [
    [0, 0, 2, 3, 7, 0, 1, 5, 4],
    [0, 5, 1, 0, 4, 0, 8, 0, 2],
    [8, 3, 4, 0, 1, 2, 0, 0, 0],
    [2, 0, 0, 6, 0, 0, 0, 9, 3],
    [6, 0, 8, 2, 0, 4, 0, 0, 0],
    [0, 0, 0, 1, 9, 0, 0, 0, 8],
    [5, 4, 9, 0, 0, 0, 0, 7, 0],
    [0, 8, 0, 0, 0, 9, 2, 4, 0],
    [1, 0, 0, 0, 0, 3, 5, 0, 0]
]

# # semi-unsolvable
# raw_board: board_matrix_raw = [
#     [0, 1, 2, 0, 7, 0, 0, 0, 3],
#     [0, 7, 0, 1, 3, 4, 2, 0, 0],
#     [3, 0, 6, 2, 8, 0, 0, 7, 0],
#     [0, 0, 7, 4, 9, 3, 0, 0, 5],
#     [1, 9, 4, 5, 2, 8, 0, 3, 0],
#     [5, 8, 3, 0, 1, 0, 9, 0, 0],
#     [7, 0, 0, 0, 0, 0, 0, 0, 8],
#     [0, 0, 0, 8, 0, 2, 0, 0, 0],
#     [0, 0, 8, 0, 0, 0, 4, 0, 0]
# ]

# # unsolvable at the moment
# raw_board: board_matrix_raw = [
#     [9, 1, 7, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 6, 0, 0, 0, 0, 9],
#     [0, 0, 0, 0, 0, 0, 0, 8, 0],
#     [2, 5, 0, 0, 8, 0, 0, 0, 1],
#     [0, 0, 0, 0, 1, 7, 0, 0, 0],
#     [0, 0, 9, 0, 3, 5, 0, 4, 0],
#     [0, 6, 0, 0, 0, 4, 0, 0, 5],
#     [0, 0, 0, 8, 0, 0, 2, 0, 0],
#     [0, 9, 4, 0, 0, 0, 0, 0, 0]
# ]

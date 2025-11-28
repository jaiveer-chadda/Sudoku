#—— Project Imports ——————————————————————————————————————————————————————————————————————————
#————— Consts & Types ———————————————————————————
from source.common.constants import BOARD_SIZE, BOX_SIZE
#—————————————————————————————————————————————————————————————————————————————————————————————


def get_index_from_coords(x: int, y: int) -> int:
    #v)in normal 9x9 sudoku, this formula is:
    #i)  (x % 9) + (y * 9)
    return (x % BOARD_SIZE) + (y * BOARD_SIZE)


def get_parent_box_from_coords(x: int, y: int) -> int:
    #v)in normal 9x9 sudoku, this formula is:
    #i)  (x/3 + y/3) * 3
    return (x // BOX_SIZE) + (y // BOX_SIZE) * BOX_SIZE

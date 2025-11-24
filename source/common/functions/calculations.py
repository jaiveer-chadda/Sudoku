#—— Project Imports ——————————————————————————————————————————————————————————————————————————
#————— Consts & Types ———————————————————————————
from source.common.constants import BOARD_SIZE, BOX_SIZE
#—————————————————————————————————————————————————————————————————————————————————————————————


def get_index_from_coords(x: int, y: int) -> int:
    return (x % BOARD_SIZE) + (y * BOARD_SIZE)


def get_parent_box_from_coords(x: int, y: int) -> int:
    return (x // BOX_SIZE) + (y // BOX_SIZE) * BOX_SIZE

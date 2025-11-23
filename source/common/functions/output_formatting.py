# — Project Imports —————————————————————————————
# ———— Consts & Types ———————————————————————————
# noinspection PyUnresolvedReferences
from common.constants import BOARD_SIZE, ALL_OPTIONS
# noinspection PyUnresolvedReferences
from common.types_ import board_flat


def format_set(input_set: set[int]) -> str:
    """
    Put the set in a constant-width format such that:
        {1, 5, 6, 8, 9} ⇒ {1,  ,  ,  , 5, 6,  , 8, 9}
    """
    return "{"+"".join([f"{i if i in input_set else " "}{", " if i!=BOARD_SIZE else ""}" for i in ALL_OPTIONS])+"} "


def get_board(input_board: board_flat, *, draw_box_borders: bool=False) -> str:
    if draw_box_borders:
        return """
            ┌───────┬───────┬───────┐
            │ {} {} {} │ {} {} {} │ {} {} {} │
            │ {} {} {} │ {} {} {} │ {} {} {} │
            │ {} {} {} │ {} {} {} │ {} {} {} │
            ├───────┼───────┼───────┤
            │ {} {} {} │ {} {} {} │ {} {} {} │
            │ {} {} {} │ {} {} {} │ {} {} {} │
            │ {} {} {} │ {} {} {} │ {} {} {} │
            ├───────┼───────┼───────┤
            │ {} {} {} │ {} {} {} │ {} {} {} │
            │ {} {} {} │ {} {} {} │ {} {} {} │
            │ {} {} {} │ {} {} {} │ {} {} {} │
            └───────┴───────┴───────┘
            """.format(
            *[
                f"{
                    i.value if i.value not in (0, None) else " "
                }"
                for i in input_board
            ]
        )
    else:
        return "".join(
            [f"{
                val if (val := cell.value)!=0 else " "
            }{
                "\n" if i % BOARD_SIZE == BOARD_SIZE-1 else " "
            }"
             for i, cell in enumerate(input_board)]
        )

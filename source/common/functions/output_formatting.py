# — External Imports —————————————————————————————
from typing import Literal

# — Project Imports —————————————————————————————
# ———— Consts & Types ———————————————————————————
from common.constants import BOARD_SIZE, ALL_OPTIONS
from common.types_ import board_flat


def format_set(input_set: set[int]) -> str:
    """
    Put the set in a constant-width format such that:
        {1, 5, 6, 8, 9} ⇒ {1,  ,  ,  , 5, 6,  , 8, 9}
    """
    return "{"+"".join([f"{i if i in input_set else " "}{", " if i!=BOARD_SIZE else ""}" for i in ALL_OPTIONS])+"} "


def get_board(input_board: board_flat, *, draw_box_borders: bool=False) -> str:
    if draw_box_borders:
        return _get_board_with_borders(input_board)
    return _get_board_no_borders(input_board)


def _get_board_no_borders(input_board: board_flat) -> str:
    return "".join(
        [
            f"{
                val if (val := cell.value)!=0 else " "
            }{
                "\n" if i % BOARD_SIZE == BOARD_SIZE-1 else " "
            }"
            for i, cell in enumerate(input_board)
        ]
    )


def _get_board_with_borders(input_board: board_flat) -> str:
    """
        ┌───────┬───────┬───────┐
        │ 9 6 2 │ 3 7 8 │ 1 5 4 │
        │ 7 5 1 │ 9 4 6 │ 8 3 2 │
        │ 8 3 4 │ 5 1 2 │ 9 6 7 │
        ├───────┼───────┼───────┤
        │ 2 1 5 │ 6 8 7 │ 4 9 3 │
        │ 6 9 8 │ 2 3 4 │ 7 1 5 │
        │ 4 7 3 │ 1 9 5 │ 6 2 8 │
        ├───────┼───────┼───────┤
        │ 5 4 9 │ 8 2 1 │ 3 7 6 │
        │ 3 8 6 │ 7 5 9 │ 2 4 1 │
        │ 1 2 7 │ 4 6 3 │ 5 8 9 │
        └───────┴───────┴───────┘
    """
    
    _indent:               str = "\n"+" "*8
    _line_segment:         str = "─"*7
    
    _content_segment:      str = f"│ "+"{} "*3
    _content_line:         str = f"{_indent}{_content_segment*3}│"
    
    _line_seg_3:      list[str] = [_line_segment]*3
    _content_lines_3: list[str] = [_content_line*3]*3
    
    def _get_line(line_type: Literal["up", "mid", "down"]) -> str:
        s1, s2, s3 =                 ('┼', '┼', '┼')
        match line_type:
            case "up":   s1, s2, s3 = '┌', '┬', '┐'
            case "mid":  s1, s2, s3 = '├', '┼', '┤'
            case "down": s1, s2, s3 = '└', '┴', '┘'
        
        return f"{_indent}{s1}{s2.join(_line_seg_3)}{s3}"
    
    return f"{_get_line("up")}{_get_line("mid").join(_content_lines_3)}{_get_line("down")}\n".format(
        *[
            f"{
                val if (val := cell.value)!=0 else " "
            }"
            for i, cell in enumerate(input_board)
        ]
    )

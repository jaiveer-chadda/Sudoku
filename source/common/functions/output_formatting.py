#—— External Imports ——————————————————————————————————————————————————————————————————————————
from typing import Literal, Optional

#—— Project Imports ——————————————————————————————————————————————————————————————————————————
#————— Consts & Types ———————————————————————————
from source.common.constants import BOARD_SIZE, ALL_OPTIONS
from source.common.types_ import board_flat
#—————————————————————————————————————————————————————————————————————————————————————————————

_COLOUR_MAPPING: dict[str, int] = {
    "black":    0,
    "red":      1,
    "green":    2,
    "yellow":   3,
    "blue":     4,
    "magenta":  5,
    "cyan":     6,
    "white":    7
}


def colour_text(
        text: str,
        font_colour: Optional[Literal[
            "black",
            "red",
            "green",
            "yellow",
            "blue",
            "magenta",
            "cyan",
            "white"
        ] | tuple[int, int, int] | int] = None,
        font_is_bright: bool = False,
        background_colour: Optional[Literal[
            "black",
            "red",
            "green",
            "yellow",
            "blue",
            "magenta",
            "cyan",
            "white"
        ] | tuple[int, int, int] | int] = None,
        background_is_bright: bool = False
) -> str:
    if font_colour is None and background_colour is None:
        raise ValueError("You must specify either a font colour or a background colour")
    
    #TODO:
    # - figure out why the cases are unreachable
    # - figure out the actual implementation
    # - figure out if this is the best way to do it
    #   - may have to just use if/else statements

    # match type(font_colour):
    #     case str:
    #         pass
    #     case int:
    #         pass
    #     case tuple:
    #         pass
    #     case _:
    #         pass
    
    return f"\x1b[0;31m{text}"


def format_set(input_set: set[int]) -> str:
    # Puts the set in a constant-width format such that:
    #   {1, 5, 6, 8, 9} ⇒ {1,  ,  ,  , 5, 6,  , 8, 9}
    return "{"+"".join([f"{i if i in input_set else " "}{", " if i!=BOARD_SIZE else ""}" for i in ALL_OPTIONS])+"} "


def get_formatted_board(input_board: board_flat, *, draw_box_borders: bool=False) -> str:
    # A handler function that calls one of the two functions below
    #   it was just cleaner to do it this way
    if draw_box_borders:
        return _get_board_with_borders(input_board)
    return _get_board_no_borders(input_board)


def _get_board_no_borders(input_board: board_flat) -> str:
    # Returns the 9x9 grid, shown without borders
    return "".join(
        [
            f"{                                                     # return the value of the cell,
                " " if (val := cell.value) in (0, None) else val    #   unless its 0 or None, then return a space
            }{
                "\n" if i % BOARD_SIZE == BOARD_SIZE-1 else " "     # every (by default) 8 chars, return a newline
            }"
            for i, cell in enumerate(input_board)
        ]
    )


def _get_board_with_borders(input_board: board_flat) -> str:
    
    # a new line and 8 spaces wirth of indent
    _newline:              str  = "\n"+" "*8                          # => '\n        '
    # the lines between the boxes
    _line_segment:         str  = "─"*7                               # => '───────'
    
    # one of the segments where the .format function will eventually put the values
    _content_segment:      str  = "│ "+"{} "*3                        # => '│ {} {} {} '
    # a newline, 3 of the content segments, and a box char, all concatenated together
    _content_line:         str  = f"{_newline}{_content_segment*3}│"  # => '│ {} {} {} │ {} {} {} │ {} {} {} │'
    
    # a tuple of three line segments - will be used to collate the final table
    _line_seg_3:     tuple[str, ...] = tuple([_line_segment]*3)       # => ['───────', '───────', '───────']
    
    # a tuple of 3 content lines, which themselves have been multiplied by 3
    _cont_3_lines_3: tuple[str, ...] = tuple([_content_line*3]*3)     # => ['│ {} {} {} │ {} {} {} │ {} {} {} │',
    #                                                                       '│ {} {} {} │ {} {} {} │ {} {} {} │',
    #                                                                       '│ {} {} {} │ {} {} {} │ {} {} {} │']
    
    def _separator_line(line_type: Literal["up", "mid", "down"]) -> str:
        _left, _mid, _right = {  # look up the inputted line_type, and get their relevant box drawing chars
            "up":   ('┌', '┬', '┐'),
            "mid":  ('├', '┼', '┤'),
            "down": ('└', '┴', '┘'),
        }.setdefault(line_type, ('┼', '┼', '┼'))  # just some default values, in case something fails
        
        #_mid.join(_line_seg_3) joins 3 line segments ('───────') by separating them with the middle box char (eg.'┬'),
        #   creating '───────┬───────┬───────',
        # which is then concatenated with:
        #   a newline and the left box drawing character (eg.'┌') on one side,
        #   and the right box char ('┐') on the other
        return f"{_newline}{_left}{_mid.join(_line_seg_3)}{_right}"  # => '┌───────┬───────┬───────┐' (line_type="up")
    
    return ((                                               # finally, concatenate the three separator lines together
        _separator_line("up") +                             # for the content sections, do the same thing as the sep
        _separator_line("mid").join(_cont_3_lines_3) +      #   lines, instead joining 3 middle sections
        _separator_line("down") +
        "\n"  #  => """
        #         ┌───────┬───────┬───────┐
        #         │ {} {} {} │ {} {} {} │ {} {} {} │
        #         │ {} {} {} │ {} {} {} │ {} {} {} │
        #         │ {} {} {} │ {} {} {} │ {} {} {} │
        #         ├───────┼───────┼───────┤
        #         │ {} {} {} │ {} {} {} │ {} {} {} │
        #         │ {} {} {} │ {} {} {} │ {} {} {} │
        #         │ {} {} {} │ {} {} {} │ {} {} {} │
        #         ├───────┼───────┼───────┤
        #         │ {} {} {} │ {} {} {} │ {} {} {} │
        #         │ {} {} {} │ {} {} {} │ {} {} {} │
        #         │ {} {} {} │ {} {} {} │ {} {} {} │
        #         └───────┴───────┴───────┘
        # """
    ).format(  # now, since we have a string with {}s in it, we can use .format() to assign values to those {}s
        *[       # make sure to unpack the result of the list comprehension,
            f"{    # so that all the values can be individually assigned
                " " if (val := cell.value) in (0, None) else val  # don't display a cell if its value is 0 or None
            }" for i, cell in enumerate(input_board)
        ]
    ))  # => """
    #         ┌───────┬───────┬───────┐
    #         │ 9 6 2 │ 3 7 8 │ 1 5 4 │
    #         │ 7 5 1 │ 9 4 6 │ 8 3 2 │
    #         │ 8 3 4 │ 5 1 2 │ 9 6 7 │
    #         ├───────┼───────┼───────┤
    #         │ 2 1 5 │ 6 8 7 │ 4 9 3 │
    #         │ 6 9 8 │ 2 3 4 │ 7 1 5 │
    #         │ 4 7 3 │ 1 9 5 │ 6 2 8 │
    #         ├───────┼───────┼───────┤
    #         │ 5 4 9 │ 8 2 1 │ 3 7 6 │
    #         │ 3 8 6 │ 7 5 9 │ 2 4 1 │
    #         │ 1 2 7 │ 4 6 3 │ 5 8 9 │
    #         └───────┴───────┴───────┘
    # """ (using example data ofc)

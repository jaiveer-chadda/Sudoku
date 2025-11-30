#—— External Imports —————————————————————————————————————————————————————————————————————————
from typing import Optional
#—————————————————————————————————————————————————————————————————————————————————————————————


def basic_solve(board: board_flat) -> board_flat:
    _changed_board_state: bool = True
    # repeat until you can make no further progress
    while _changed_board_state:
        _changed_board_state = False
        # iterate through every cell in the board
        for cell in board:
            _changed_board_state = _remove_invalid_candidates(cell, _changed_board_state)
    return board


def _remove_invalid_candidates(cell_to_check: Cell, _has_changed: bool) -> Optional[bool]:
    # ignore the cells that don't have a value
    if not cell_to_check.has_some_value:
        return _has_changed
    # for all cells with a value, check which cells it can see,
    #   and remove its value from those seen cells
    for cell_to_change in cell_to_check.sees:
        try:
            cell_to_change.remove_from_options(cell_to_check.value)
            _has_changed = True
        # if a {{KeyError}} is raised
        #   it means that that value wasn't an option in the cell we tried to remove it from
        #   which doesn't matter, so it's ignored
        # it's also easier and quicker to handle it this way,
        #   rather than checking whether the value actually _is_ an option before removing it
        except KeyError:
            #{{Key Error Excepted}}
            pass
    return _has_changed

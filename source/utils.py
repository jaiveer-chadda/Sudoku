



# from typing import Literal
#
#
# def is_solved(bv: dict[tuple[int, int], list[int | tuple[int, int] | bool | set[int]]]) -> bool:
#     return all(map(lambda x: x[2], bv.values()))
#
#
# def get_candidates(
#         bv:  dict[tuple[int, int], list[int | tuple[int, int] | bool | set[int]]],
#         key: tuple[int, int]
# ) -> set[int]:
#     visible = bv[key][3]
#     return set(range(1, 10)) - visible
#
#
# def add_seeable_vals(
#         board_values: dict[tuple[int, int], list[int | tuple[int, int] | bool | set[int]]],
#         loc: tuple[int, int],
#         to_add: Literal['candidates', 'value'] = 'value'
# ):
#     pass
#
#
# def print_board(raw_board: list[list[int]]) -> None:
#     print()
#     for row in range(len(raw_board)):
#         for col in range(len(raw_board[row])):
#             print(raw_board[row][col] if raw_board[row][col] != 0 else " ", end=" ")
#         print()
#     print()
#
#
# def print_line() -> None:
#     print("-"*18)

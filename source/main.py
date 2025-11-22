from get_board import raw_board
from board import Board


board: Board = Board(raw_board)


# print("\n"*10)

for i in board.board:
    pass
    # print(repr(i))

print(board)

board.print_candidates()

# from utils import *
#
# # unsolvable at the moment
# # raw_board: list[list[int]] = [[9, 1, 7, 0, 0, 0, 0, 0, 0],
# #                               [0, 0, 0, 6, 0, 0, 0, 0, 9],
# #                               [0, 0, 0, 0, 0, 0, 0, 8, 0],
# #                               [2, 5, 0, 0, 8, 0, 0, 0, 1],
# #                               [0, 0, 0, 0, 1, 7, 0, 0, 0],
# #                               [0, 0, 9, 0, 3, 5, 0, 4, 0],
# #                               [0, 6, 0, 0, 0, 4, 0, 0, 5],
# #                               [0, 0, 0, 8, 0, 0, 2, 0, 0],
# #                               [0, 9, 4, 0, 0, 0, 0, 0, 0]]
#
# raw_board: list[list[int]] = [[0, 1, 2, 0, 7, 0, 0, 0, 3],
#                               [0, 7, 0, 1, 3, 4, 2, 0, 0],
#                               [3, 0, 6, 2, 8, 0, 0, 7, 0],
#                               [0, 0, 7, 4, 9, 3, 0, 0, 5],
#                               [1, 9, 4, 5, 2, 8, 0, 3, 0],
#                               [5, 8, 3, 0, 1, 0, 9, 0, 0],
#                               [7, 0, 0, 0, 0, 0, 0, 0, 8],
#                               [0, 0, 0, 8, 0, 2, 0, 0, 0],
#                               [0, 0, 8, 0, 0, 0, 4, 0, 0]]
#
# # raw_board: list[list[int]] = [[0, 1, 2, 0, 7, 0, 0, 0, 3],
# #                               [0, 7, 0, 1, 3, 4, 2, 0, 0],
# #                               [3, 0, 6, 2, 8, 0, 0, 7, 0],
# #                               [0, 0, 7, 4, 9, 3, 0, 0, 5],
# #                               [1, 9, 4, 5, 2, 8, 0, 3, 0],
# #                               [5, 8, 3, 0, 1, 0, 9, 0, 0],
# #                               [7, 0, 0, 0, 0, 0, 0, 0, 8],
# #                               [0, 0, 0, 8, 0, 2, 0, 0, 0],
# #                               [0, 0, 8, 0, 0, 0, 4, 0, 0]]
#
# # solved
# # raw_board: list[list[int]] = [[0, 0, 2, 3, 7, 0, 1, 5, 4],
# #                               [0, 5, 1, 0, 4, 0, 8, 0, 2],
# #                               [8, 3, 4, 0, 1, 2, 0, 0, 0],
# #                               [2, 0, 0, 6, 0, 0, 0, 9, 3],
# #                               [6, 0, 8, 2, 0, 4, 0, 0, 0],
# #                               [0, 0, 0, 1, 9, 0, 0, 0, 8],
# #                               [5, 4, 9, 0, 0, 0, 0, 7, 0],
# #                               [0, 8, 0, 0, 0, 9, 2, 4, 0],
# #                               [1, 0, 0, 0, 0, 3, 5, 0, 0]]
#
# board_values: dict[tuple[int, int], list[int | tuple[int, int] | bool | set[int]]] = {}
#
# for row in range(len(raw_board)):
#     for col in range(len(raw_board[row])):
#         board_values[(row, col)] = [
#             raw_board[row][col],  # value
#             (col // 3, row // 3),  # section coordinates
#             raw_board[row][col] != 0,  # solved or not
#             set()  # the set of seeable numbers
#         ]
#
# print_board(raw_board)
#
# i: int = 0
# while not is_solved(board_values):
#
#     # ------- basic checking ------- #
#     for box_being_checked_key in board_values.keys():
#         if board_values[box_being_checked_key][2]:  # box is solved
#
#             for box_to_change_key in board_values.keys():
#
#                 # if the box isn't already solved and ...
#                 if (not board_values[box_to_change_key][2] and
#                         # ... the box is in the same row or ...
#                         (box_to_change_key[0] == box_being_checked_key[0] or
#                          # ... the box is in the same col or ...
#                          box_to_change_key[1] == box_being_checked_key[1] or
#                          # ... the box is in the same section
#                          board_values[box_to_change_key][1] == board_values[box_being_checked_key][1])):
#                     board_values[box_to_change_key][3].add(board_values[box_being_checked_key][0])
#
#                     something_was_checked = True
#
#                 candidates: set[int] = get_candidates(board_values, box_to_change_key)
#                 if len(candidates) == 1:
#                     board_values[box_to_change_key][0] = (new_value := candidates.pop())
#                     raw_board[box_to_change_key[0]][box_to_change_key[1]] = new_value
#                     board_values[box_to_change_key][2] = True
#
#     # ------- checking for doubles ------- #
#     for row in range(len(raw_board)):
#         #                 key            , candidate doubles
#         pairs: list[tuple[tuple[int, int], set[int]]] = []
#
#         for box in range(len(raw_board[row])):
#             key: tuple[int, int] = (row, box)
#             candidates: set[int] = get_candidates(board_values, key)
#
#             # if row == 4: print(candidates)
#
#             # if it could be a pair ...
#             if len(candidates) == 2:
#                 # ... add it to the pairs candidate list
#                 pairs.append((key, candidates))
#             else:
#                 # and if not solved
#                 if not board_values[key][2]:
#                     # otherwise check if it interferes with any pairs
#                     to_remove: list[tuple[tuple[int, int], set[int]]] = []
#                     for pair in pairs:
#                         if len(candidates.intersection(pair[1])) >= 1:
#                             to_remove.append(pair)
#
#                     # remove a pair if there is another box in the row
#                     #   with a candidate that is included in the pair
#                     for pair in to_remove:
#                         pairs.remove(pair)
#
#             # if row == 4: print()
#
#         # if row == 4: print(pairs, board_values[pairs[0][0]][3], board_values[pairs[1][0]][3])
#
#         if len(pairs) == 2 and (board_values[pairs[0][0]][3] == board_values[pairs[1][0]][3]):
#             # print("yeah?")
#             # if pairs are in the same box
#             add_seeable_vals(board_values, (row, box), 'candidates')
#
#             for box in range(len(raw_board[row])):
#                 # if row == 4:
#                 #     print((row, box))
#                 #     print([pair[0] for pair in pairs])
#                 #     print((row, box) not in [pair[0] for pair in pairs])
#                 if (row, box) not in [pair[0] for pair in pairs]:
#                     # if row == 4: print("yes")
#                     board_values[(row, box)][3].update(pairs[0][1])
#
#     # print("\n\n\n")
#
#     i += 1
#     if i > 3:
#         break
#
# print_line()
# print_board(raw_board)

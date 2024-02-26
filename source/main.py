def is_solved(bv: dict[tuple[int, int], list[int | tuple[int, int] | bool | set[int]]]) -> bool:
    return all(map(lambda x: x[2], bv.values()))


# unsolvable at the moment
raw_board: list[list[int]] = [[9, 1, 7, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 6, 0, 0, 0, 0, 9],
                              [0, 0, 0, 0, 0, 0, 0, 8, 0],
                              [2, 5, 0, 0, 8, 0, 0, 0, 1],
                              [0, 0, 0, 0, 1, 7, 0, 0, 0],
                              [0, 0, 9, 0, 3, 5, 0, 4, 0],
                              [0, 6, 0, 0, 0, 4, 0, 0, 5],
                              [0, 0, 0, 8, 0, 0, 2, 0, 0],
                              [0, 9, 4, 0, 0, 0, 0, 0, 0]]

# solved
# raw_board: list[list[int]] = [[0, 0, 2, 3, 7, 0, 1, 5, 4],
#                               [0, 5, 1, 0, 4, 0, 8, 0, 2],
#                               [8, 3, 4, 0, 1, 2, 0, 0, 0],
#                               [2, 0, 0, 6, 0, 0, 0, 9, 3],
#                               [6, 0, 8, 2, 0, 4, 0, 0, 0],
#                               [0, 0, 0, 1, 9, 0, 0, 0, 8],
#                               [5, 4, 9, 0, 0, 0, 0, 7, 0],
#                               [0, 8, 0, 0, 0, 9, 2, 4, 0],
#                               [1, 0, 0, 0, 0, 3, 5, 0, 0]]

board_values: dict[tuple[int, int], list[int | tuple[int, int] | bool | set[int]]] = {}

for row in range(len(raw_board)):
    for col in range(len(raw_board[row])):
        board_values[(row, col)] = [
            raw_board[row][col],  # value
            (col // 3, row // 3),  # section coordinates
            raw_board[row][col] != 0,  # solved or not
            set()  # the set of seeable numbers
        ]

for row in range(len(raw_board)):
    for col in range(len(raw_board[row])):
        print(raw_board[row][col] if raw_board[row][col] != 0 else " ", end=" ")
    print()


while not is_solved(board_values):

    for box_being_checked_key in board_values.keys():
        if board_values[box_being_checked_key][2]:  # box is solved

            for box_to_change_key in board_values.keys():

                # the box isn't already solved and ...
                if (not board_values[box_to_change_key][2] and
                    # ... the box is in the same row or ...
                    (box_to_change_key[0] == box_being_checked_key[0] or
                     # ... the box is in the same col or ...
                     box_to_change_key[1] == box_being_checked_key[1] or
                     # ... the box is in the same section
                     board_values[box_to_change_key][1] == board_values[box_being_checked_key][1])):

                    board_values[box_to_change_key][3].add(board_values[box_being_checked_key][0])

                if len(board_values[box_to_change_key][3]) == 8:
                    new_value: int = (set(range(1, 10)) - board_values[box_to_change_key][3]).pop()
                    board_values[box_to_change_key][0] = new_value
                    raw_board[box_to_change_key[0]][box_to_change_key[1]] = new_value
                    board_values[box_to_change_key][2] = True

print()

for row in range(len(raw_board)):
    for col in range(len(raw_board[row])):
        print(raw_board[row][col], end=" ")
    print()

from board import flatten_matrix_to_1d_tuple

SUDOKU_BOARD_SIZE: int = 9

raw_board: list[list[int]] = [
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

# raw_board: list[list[int]] = [
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


def create_board_json(board: tuple[int, ...]) -> None:
    output_buffer: list[str] = ['{\n  "board_positions": {']
    
    for i in range(SUDOKU_BOARD_SIZE**2):
        output_buffer.append(f"""
        "{i}": {{
          "main": {board[i]},
          "corner_candidates": [],
          "central_candidates": [],
          "colours": []
        }}""" + ("," if i != SUDOKU_BOARD_SIZE**2 - 1 else "\n  }\n}"))
    
    output: str = "".join(output_buffer)
    
    with open('board.json', 'w') as f:
        f.write(output)


def from_matrix(board: list[list[int]]) -> None:
    create_board_json(flatten_matrix_to_1d_tuple(board))


def main() -> None:
    from_matrix(raw_board)


if __name__ == "__main__":
    main()

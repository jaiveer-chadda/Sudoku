from common.constants import SUDOKU_BOARD_SIZE, raw_board
from board import flatten_matrix_to_1d_tuple


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

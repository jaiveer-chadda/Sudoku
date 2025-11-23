# noinspection PyUnresolvedReferences
from objects.board import flatten_matrix_to_1d_tuple
from common.constants import BOARD_SIZE, raw_board


def create_board_json(board: tuple[int, ...]) -> None:
    output_buffer: list[str] = ['{\n  "board_positions": {']
    
    for i in range(BOARD_SIZE ** 2):
        output_buffer.append(f"""
        "{i}": {{
          "main": {board[i]},
          "corner_candidates": [],
          "central_candidates": [],
          "colours": []
        }}""" + ("," if i != (BOARD_SIZE**2)-1 else "\n  }\n}"))
    
    output: str = "".join(output_buffer)
    
    with open('resources/boards/board.json', 'w') as f:
        f.write(output)


def from_matrix(board: list[list[int]]) -> None:
    create_board_json(flatten_matrix_to_1d_tuple(board))


def main() -> None:
    from_matrix(raw_board)


if __name__ == "__main__":
    main()

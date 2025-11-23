# — Project Imports —————————————————————————————
# ———— Consts & Types ———————————————————————————
from common.constants import BOARD_SIZE, raw_board
# ———— Objects ——————————————————————————————————
# noinspection PyUnresolvedReferences
from objects.board import flatten_matrix_to_1d_tuple
# ———— Functions ————————————————————————————————
from common.functions.base_64_ import encode_b64


def create_board_json(board_list: tuple[int, ...]) -> None:
    output_buffer: list[str] = ['{\n  "board_positions": {']
    
    # iterate through the given list,
    #   and create a text file with that info in a json format
    for i in range(BOARD_SIZE ** 2):
        output_buffer.append(f"""
        "{i}": {{
          "main": {board_list[i]},
          "corner_candidates": [],
          "central_candidates": [],
          "colours": []
        }}""" + ("," if i != (BOARD_SIZE**2)-1 else "\n  }\n}"))
    
    output: str = "".join(output_buffer)
    
    # add a board code to the end of a file,
    #   which just makes it so that every board I use/test has a unique identifier,
    #   without making them sequential
    board_code: str = encode_b64("".join(map(str, board_list)))
    with open(f"resources/boards/board_{board_code}.json", 'w') as f:
        f.write(output)


def from_matrix(board: list[list[int]]) -> None:
    create_board_json(flatten_matrix_to_1d_tuple(board))


def main() -> None:
    from_matrix(raw_board)


if __name__ == "__main__":
    main()

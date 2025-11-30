#—— Project Imports ——————————————————————————————————————————————————————————————————————————
#————— Consts & Types ———————————————————————————
from source.common.constants import BOARD_SIZE, board_input
from source.common.types_ import board_matrix_raw
#————— Objects ——————————————————————————————————
from source.objects.board.board import flatten_matrix_to_1d_tuple
#————— Utils ————————————————————————————————
#_from source.common.utils.base_64_ import encode_b64
from source.common.utils.hashing import hash_to_8_chars
#—————————————————————————————————————————————————————————————————————————————————————————————


def create_board_json(board_list: tuple[int, ...]) -> None:
    output_buffer: list[str] = ['{\n  "board_positions": {']
    
    # iterate through the given list,
    #   and create a text file with that info (in a json format)
    for i in range(BOARD_SIZE ** 2):
        output_buffer.append(f"""
        "{i}": {
          "main": {board_list[i]},
          "corner_candidates": [],
          "central_candidates": [],
          "colours": []
        }""" + ("," if i != (BOARD_SIZE**2)-1 else "\n  }\n}"))
    
    output: str = "".join(output_buffer)
    
    # add a board code/hash to the end of a file,
    #   which just makes it so that every board I use/test has a unique identifier,
    #   without making them sequential
    board_hash: str = hash_to_8_chars(  #_encode_b64(
        int(
            "".join(                    # make sure all the board characters are strings
                map(str, board_list)    #   then concatenate them, and pass them into the hashing function
            )
        )
    )
    with open(f"resources/boards/board_{board_hash}.json", 'w') as f:
        f.write(output)


def from_matrix(board: board_matrix_raw) -> None:
    create_board_json(flatten_matrix_to_1d_tuple(board))


#—————————————————————————————————————————————————————————————————————————————————————————————

def main() -> None:
    from_matrix(board_input)


if __name__ == "__main__":
    main()

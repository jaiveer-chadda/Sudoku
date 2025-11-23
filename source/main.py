# — Project Imports ——————————————————————————————————————————————————————————————————————————
# ———— Consts & Types ———————————————————————————
from source.common.constants import board_input
# ———— Objects ——————————————————————————————————
from source.objects.board import Board
# ————————————————————————————————————————————————————————————————————————————————————————————


board: Board = Board(board_input)
print(board)

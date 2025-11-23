# — Project Imports —————————————————————————————
# ———— Consts & Types ———————————————————————————
from .common.constants import board_input
# ———— Objects ——————————————————————————————————
from .objects.board import Board


board: Board = Board(board_input)
print(board)

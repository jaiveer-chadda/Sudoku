# — Project Imports —————————————————————————————
# ———— Consts & Types ———————————————————————————
from common.constants import raw_board
# ———— Objects ——————————————————————————————————
from objects.board import Board


board: Board = Board(raw_board)
print(board)

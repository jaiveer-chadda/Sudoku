import tkinter as tk
from tkinter import Tk, Label, Canvas, Frame, Button


WINDOW_WIDTH: int = 600
WINDOW_HEIGHT: int = 800

APP_TITLE: str = "Sudoku App"


class AppGUI:
    def __init__(self, title: str = APP_TITLE) -> None:
        self.title: str = title
        self._window_init()
        # self._canvas_init()

    def _window_init(self, width: int = WINDOW_WIDTH, height: int = WINDOW_HEIGHT) -> None:
        self.window_width: int = width
        self.window_height: int = height
        
        self.window: Tk = Tk()
        self._set_window_dimensions_and_pos()
        self.window.resizable(False, False)
        self.window.title("Sudoku App")

    def _set_window_dimensions_and_pos(self) -> None:
        x: int = (self.window.winfo_screenwidth() - self.window_width) // 2
        y: int = (self.window.winfo_screenheight() - self.window_height) // 2
        self.window.geometry(f"{self.window_width}x{self.window_height}+{x}+{y-50}")
        
    # def _canvas_init(self) -> None:
    #     self.canvas: Canvas = Canvas(self.window, width=self.window_width, height=self.window_height)
    #     self.canvas.pack()


app: AppGUI = AppGUI()

board_dims: int = 500


outer = Frame(app.window)
outer.pack(expand=True, fill='both')

test_frame = Frame(outer, background="red")
test_frame.place(relx=0.5, y=50, anchor="n", width=board_dims, height=board_dims)

rows: int = 9
cols: int = 9

# set grid weights for equal spacing
for i in range(rows):
    test_frame.rowconfigure(i, weight=1)
for j in range(cols):
    test_frame.columnconfigure(j, weight=1)

for i in range(rows):
    for j in range(cols):
        frame = Frame(
            master=test_frame,
            borderwidth=1,
            background='green'
        )
        frame.grid(row=i, column=j, sticky='nsew')  # sticky = expand to fill the cell
        frame.grid_propagate(False)
        
        lab = Label(frame, text=f"({j+1},{i+1})")
        lab.pack(expand=True, fill='both')


app.window.mainloop()

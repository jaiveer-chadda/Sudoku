import tkinter as tk

APP_TITLE: str = "Sudoku App"

WINDOW_SIZE_PX: tuple[int, int] = (600, 800)
BOARD_DIMS_PX: int = 500

BOARD_XY_SIZE: int = 9


_WINDOW_WIDTH_PX: int = WINDOW_SIZE_PX[0]
_WINDOW_HEIGHT_PX: int = WINDOW_SIZE_PX[1]


class AppGUI:
    def __init__(self, title: str = APP_TITLE) -> None:
        self.title: str = title
        self._window_init()

    def _window_init(self, width: int = _WINDOW_WIDTH_PX, height: int = _WINDOW_HEIGHT_PX) -> None:
        self.window_width: int = width
        self.window_height: int = height
        
        self.window: tk.Tk = tk.Tk()
        self._set_window_dimensions_and_pos()
        self.window.resizable(False, False)
        self.window.title("Sudoku App")

    def _set_window_dimensions_and_pos(self) -> None:
        x: int = (self.window.winfo_screenwidth() - self.window_width) // 2
        y: int = (self.window.winfo_screenheight() - self.window_height) // 2
        self.window.geometry(f"{self.window_width}x{self.window_height}+{x}+{y-50}")


app: AppGUI = AppGUI()

board_container: tk.Frame = tk.Frame(app.window)
board_container.pack(expand=True, fill='both')

board_frame: tk.Frame = tk.Frame(board_container, background="red")
board_frame.place(relx=0.5, y=50, anchor="n", width=BOARD_DIMS_PX, height=BOARD_DIMS_PX)

# set grid weights for equal spacing
for row_col in range(BOARD_XY_SIZE):
    board_frame.rowconfigure(row_col, weight=1)
    board_frame.columnconfigure(row_col, weight=1)

for row in range(BOARD_XY_SIZE):
    for col in range(BOARD_XY_SIZE):
        cell_frame: tk.Frame = tk.Frame(
            master=board_frame,
            borderwidth=1,
            background='green'
        )
        cell_frame.grid(row=row, column=col, sticky=tk.NSEW)  # sticky makes it expand to fill the frame
        cell_frame.grid_propagate(False)
        
        debug_lab: tk.Label = tk.Label(cell_frame, text=f"({col + 1},{row + 1})")
        debug_lab.pack(expand=True, fill='both')

app.window.mainloop()

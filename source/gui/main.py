import tkinter as tk

from source.gui.dimensions import Dimension

APP_TITLE: str = "Sudoku App"

WINDOW_SIZE:      Dimension = Dimension(600, 800)
WINDOW_OFFSET:    Dimension = Dimension(0, -50)

BOARD_SIZE_PX:    Dimension = Dimension(500)
BOARD_SIZE_CELLS: Dimension = Dimension(9)


class AppGUI:
    def __init__(self,
                 title: str = APP_TITLE,
                 width: int = WINDOW_SIZE.width,
                 height: int = WINDOW_SIZE.height,
                 offset_x: int = WINDOW_OFFSET.x,
                 offset_y: int = WINDOW_OFFSET.y
                 ) -> None:
        self.title: str = title
        
        self.size_px: Dimension = Dimension(width, height)
        self._offset: Dimension = Dimension(offset_x, offset_y)
        
        self._window_init()

    def _window_init(self) -> None:
        self.root_window: tk.Tk = tk.Tk()
        
        self._set_window_dimensions_and_pos()
        self.root_window.resizable(False, False)
        self.root_window.title(self.title)

    def _set_window_dimensions_and_pos(self) -> None:
        _screen_width: int = self.root_window.winfo_screenwidth()
        _screen_height: int = self.root_window.winfo_screenheight()
        
        _window_centre_pos_x: int = (_screen_width - self.size_px.width) // 2
        _window_centre_pos_y: int = (_screen_height - self.size_px.height) // 2
        
        self.root_window.geometry(
            f"{self.size_px.width}x{self.size_px.height}" +
            f"+{_window_centre_pos_x+self._offset.x}+{_window_centre_pos_y++self._offset.y}"
        )


app: AppGUI = AppGUI()

board_container: tk.Frame = tk.Frame(app.root_window)
board_container.pack(expand=True, fill='both')

board_frame: tk.Frame = tk.Frame(board_container, background="red")

# relx=0.5 places the box in the centre horizontally, and y=50 places it 50 px away from the top (as padding)
board_frame.place(relx=0.5, y=50, anchor="n", width=BOARD_SIZE_PX.width, height=BOARD_SIZE_PX.height)

# set grid weights for equal column and row spacing
for row_col in range(BOARD_SIZE_CELLS.dimension):
    board_frame.rowconfigure(row_col, weight=1)
    board_frame.columnconfigure(row_col, weight=1)

for cell_index in range(BOARD_SIZE_CELLS.dimension**2):
    row, col = cell_index//BOARD_SIZE_CELLS.dimension, cell_index%BOARD_SIZE_CELLS.dimension

    cell_frame_i: tk.Frame = tk.Frame(master=board_frame, borderwidth=1, background='green')
    cell_frame_i.grid(row=row, column=col, sticky=tk.NSEW)  # sticky=tk.NSEW makes each cell expand to fill the frame
    cell_frame_i.grid_propagate(False)
    
    debug_lab: tk.Label = tk.Label(cell_frame_i, text=f"({col + 1},{row + 1})")
    debug_lab.pack(expand=True, fill='both')

app.root_window.mainloop()

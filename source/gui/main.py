import tkinter as tk

from source.gui.dimensions import Dimension


APP_TITLE: str = "Sudoku App"

WINDOW_SIZE:      Dimension = Dimension(600, 800)
WINDOW_OFFSET:    Dimension = Dimension(0, -30)

BOARD_SIZE_PX:    Dimension = Dimension(500)
BOARD_SIZE_CELLS: Dimension = Dimension(9)

BOARD_PADDING_TOP: int = 50


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
            f"+{_window_centre_pos_x+self._offset.x}+{_window_centre_pos_y+self._offset.y}"
        )
        
        
class BoardGUI:
    def __init__(self, master: AppGUI, padding_top: int = BOARD_PADDING_TOP, background: str = "") -> None:
        self.master: AppGUI = master
        
        self._padding_top: int = padding_top
        self._background: str = background  #?bg=red for debugging
        
        self._cells: list[CellGUI] = [].copy()
        
        self._container_init()
        self._board_init()
        self._init_all_cells()
    
    def _container_init(self) -> None:
        self.container: tk.Frame = tk.Frame(self.master.root_window)
        self.container.pack(expand=True, fill='both')
        
    def _board_init(self) -> None:
        def _configure_board_grid_spacing() -> None:
            # set grid weights for equal column and row spacing
            for _row_col in range(BOARD_SIZE_CELLS.dimension):
                self.frame.rowconfigure(_row_col, weight=1)
                self.frame.columnconfigure(_row_col, weight=1)
        
        self.frame: tk.Frame = tk.Frame(self.container, background=self._background)
        # anchor='n' means that when setting the frame's pos, I'm focusing on the top middle part of it to place
        # relx=0.5 places the anchor in the centre horizontally, and y=50 places it 50px away from the top (as padding)
        self.frame.place(
            relx=0.5, y=self._padding_top,
            anchor="n",
            width=BOARD_SIZE_PX.width, height=BOARD_SIZE_PX.height
        )
        _configure_board_grid_spacing()
            
    def _init_all_cells(self) -> None:
        for cell_index in range(BOARD_SIZE_CELLS.dimension**2):
            new_cell: CellGUI = CellGUI(self, cell_index)
            self._cells.append(new_cell)


class CellGUI:
    def __init__(self, master: BoardGUI, index: int) -> None:
        self.master: BoardGUI = master
        self.index: int = index
        
        self.row: int = index // BOARD_SIZE_CELLS.dimension
        self.col: int = index % BOARD_SIZE_CELLS.dimension
        
        self._cell_init()
        self._add_debug_label()
        
    def _cell_init(self) -> None:
        self.frame: tk.Frame = tk.Frame(master=self.master.frame, borderwidth=1, background='green')
        
        # sticky=tk.NSEW makes each cell expand to fill the frame
        self.frame.grid(row=self.row, column=self.col, sticky=tk.NSEW)
        self.frame.grid_propagate(False)

    def _add_debug_label(self) -> None:
        debug_lab: tk.Label = tk.Label(self.frame, text=f"({self.col + 1},{self.row + 1})")
        debug_lab.pack(expand=True, fill='both')


app: AppGUI = AppGUI()
board: BoardGUI = BoardGUI(app)

app.root_window.mainloop()

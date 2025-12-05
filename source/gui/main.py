#—— External Imports —————————————————————————————————————————————————————————————————————————
import tkinter as tk

#—— Project Imports ——————————————————————————————————————————————————————————————————————————
#————— GUI ——————————————————————————————————————
from source.gui.dimensions import Dimensions
from source.gui.directions import Directions as Dir
from source.gui.bordered_frame import BorderedFrame  #, BorderedFrame
#—————————————————————————————————————————————————————————————————————————————————————————————

# TODO:
#   - move all of the GUI classes into their own files
#   - rework the hardcoded window sizes to be based on the screen size instead
#       - maybe on this one
#       - test it first


APP_TITLE: str = "Sudoku App"

WINDOW_SIZE:      Dimensions = Dimensions(600, 800)
WINDOW_OFFSET:    Dimensions = Dimensions(0, -30)

BOARD_SIZE_PX:    Dimensions = Dimensions(500)
BOARD_SIZE_CELLS: Dimensions = Dimensions(9)

BOARD_PADDING_TOP: int = 50

#?colours are just for debugging (for now)
BOARD_BACKGROUND: str = "red"
CELL_BACKGROUND: str = "green"


#—— Main App —————————————————————————————————————————————————————————————————————————————————————————————————————————
class AppGUI:
    def __init__(
            self,
            title: str = APP_TITLE,
            width: int = WINDOW_SIZE.width,
            height: int = WINDOW_SIZE.height,
            offset_x: int = WINDOW_OFFSET.x,
            offset_y: int = WINDOW_OFFSET.y
    ) -> None:
        self.title: str = title
        
        self._win_size: Dimensions = Dimensions(width, height)
        self._offset: Dimensions = Dimensions(offset_x, offset_y)
        
        self._window_init()

    def _window_init(self) -> None:
        self.root_window: tk.Tk = tk.Tk()
        self.root_window.title(self.title)
        
        self._set_window_dimensions_and_pos()
        self.root_window.resizable(False, False)

    def _set_window_dimensions_and_pos(self) -> None:
        _screen_size: Dimensions = Dimensions(
            self.root_window.winfo_screenwidth(),
            self.root_window.winfo_screenheight()
        )
        _window_centre: Dimensions = Dimensions(
            (_screen_size.width - self._win_size.width) // 2,
            (_screen_size.height - self._win_size.height) // 2
        )
        self.root_window.geometry(
            # Set the app window's size
            f"{self._win_size.width}x{self._win_size.height}" +
            # Just move the window slightly for ease of visualisation
            #   (on a Mac, the screen size doesn't take into account the dock,
            #    so if you put the window in the middle of the screen, it looks off-centre)
            f"+{_window_centre.x + self._offset.x}+{_window_centre.y + self._offset.y}"
        )


#—— Board ————————————————————————————————————————————————————————————————————————————————————————————————————————————
class BoardGUI:
    def __init__(
            self,
            master: AppGUI,
            padding_top: int = BOARD_PADDING_TOP,
            background: str = BOARD_BACKGROUND
    ) -> None:
        self.master: AppGUI = master
        
        self._padding_top: int = padding_top
        self._background: str = background
        
        self._container_init()
        self._board_init()
        self._init_all_cells()
    
    def _container_init(self) -> None:
        self.container: tk.Frame = tk.Frame(self.master.root_window)
        self.container.pack(expand=True, fill='both')
        
    def _board_init(self) -> None:
        self.frame: tk.Frame = tk.Frame(self.container, background=self._background)
        
        self.frame.place(
            # when setting the frame's pos, set the top middle part (the 'north' point)
            anchor='n',
            # place the anchor in the centre of the window horizontally,
            #   and 50px away from the top (as a kinda padding)
            relx=0.5, y=self._padding_top,
            width=BOARD_SIZE_PX.width, height=BOARD_SIZE_PX.height
        )
        self.__configure_board_grid_spacing()
    
    def __configure_board_grid_spacing(self) -> None:
        # set grid weights for equal column and row spacing
        #?this whole function will have to be reworked since,
        #?  again, .dimension only works if the board's a square
        for _row_col in range(BOARD_SIZE_CELLS.dimension):
            self.frame.rowconfigure(_row_col, weight=1)
            self.frame.columnconfigure(_row_col, weight=1)
            
    def _init_all_cells(self) -> None:
        # iterate through the cells, and initialise them one by one
        #?the use of 'dimension' here will have to be changed,
        #?  cos it only works if the board's a square
        for cell_index in range(BOARD_SIZE_CELLS.dimension**2):
            CellGUI(self, cell_index)  #, background="")


#—— An Individual Cell ———————————————————————————————————————————————————————————————————————————————————————————————
class CellGUI:
    def __init__(
            self,
            master: BoardGUI,
            index: int,
            background: str = CELL_BACKGROUND
    ) -> None:
        self.master: BoardGUI = master
        self.index: int = index
        self._background: str = background
        
        #?when fixing the implementation to work with non-square boards,
        #?  I'm rly gonna have to figure out the row and col calculations,
        #?  cos it rly messed with my head the last time I tried it
        self.row: int = index // BOARD_SIZE_CELLS.dimension
        self.col: int = index % BOARD_SIZE_CELLS.dimension
        
        self._cell_init()
        self._add_debug_label()
        
    def _cell_init(self) -> None:
        self.frame: tk.Frame = tk.Frame(
            master=self.master.frame,
            borderwidth=2,
            relief='solid',
            background=self._background
        )
        
        # sticky=tk.NSEW makes the cell's corners expand to fill the grid position
        self.frame.grid(row=self.row, column=self.col, sticky=tk.NSEW)  #, padx=1, pady=1)
        self.frame.grid_propagate(False)

    def _add_debug_label(self) -> None:
        # put some text in each cell with its row and column number - just so I can see what's happening
        debug_lab: tk.Label = tk.Label(self.frame, text=f"({self.col + 1},{self.row + 1})")
        debug_lab.pack(expand=True, fill='both')

#—————————————————————————————————————————————————————————————————————————————————————————————————————————————————————


# def main() -> None:
#     # app: AppGUI = AppGUI()
#     # _: BoardGUI = BoardGUI(app)
#     #
#     # app.root_window.mainloop()
#
#     try:
#         from Tkinter import Tk, Label
#     except ImportError:
#         from tkinter import Tk, Label
#
#     root = Tk()
#     root.geometry("300x400")
#     root.configure(background="white")
#
#     f = BorderedFrame(
#         root, text="This is some text", background="white", border_colour="blue", padx=3,
#         border_weights=Dir(2, 0, 0, 0), interior_widget=Label
#     )
#     f.pack(pady=10)
#
#     f = BorderedFrame(
#         root, background="white", border_colour="green",
#         border_weights=Dir(2, 0, 0, 0)
#     )
#     f.pack(pady=10)
#
#     Label(f.interior, text="This is another example", background="white").pack(padx=4, pady=2)
#
#     root.mainloop()


# if __name__ == "__main__":
#     main()


if __name__ == "__main__":
    try:
        from Tkinter import Tk, Label
    except ImportError:
        from tkinter import Tk, Label
    
    root = Tk()
    root.geometry("300x400")
    root.configure(background="white")
    
    f = BorderedFrame(root, text="This is a text", background="white", border_colour="blue", padx=3, border_left=7, interior_widget=Label)
    f.pack(pady=10)
    
    f = BorderedFrame(root, background="white", border_colour="green", border_left=7, border_top=2, border_right=2, border_bottom=2)
    f.pack(pady=10)
    
    Label(f.interior, text="This is another example", background="white").pack(padx=4, pady=2)
    
    root.mainloop()

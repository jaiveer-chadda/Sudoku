#—— External Imports —————————————————————————————————————————————————————————————————————————
import tkinter as tk
# from typing import Optional

#—— Project Imports ——————————————————————————————————————————————————————————————————————————
#————— GUI ——————————————————————————————————————
from source.gui.directions import Directions
#—————————————————————————————————————————————————————————————————————————————————————————————


class BorderedFrame(tk.Frame):
    """
    Adapted from code by Miguel Martinez Lopez
        https://code.activestate.com/recipes/580798-tkinter-frame-with-different-border-sizes/
    """
    def __init__(
            self,
            master: tk.Misc,
            border_weights: Directions = Directions(),
            border_colour: str = "",
            *,
            interior_widget: type[tk.Widget] = tk.Frame,
            **kwargs
    ) -> None:
        super().__init__(master, background=border_colour, bd=0, highlightthickness=0)
        
        self.interior: tk.Widget = interior_widget.__new__(interior_widget)
        self.interior.__init__(self, **kwargs)
        
        self.interior.pack(
            padx=(border_weights.left, border_weights.right),
            pady=(border_weights.top, border_weights.bottom)
        )

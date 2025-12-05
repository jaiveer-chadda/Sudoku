#—— External Imports —————————————————————————————————————————————————————————————————————————
import tkinter as tk
from typing import Literal

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
        self.border_weights: Directions = border_weights
        self.border_colour: str = border_colour
        
        super().__init__(master, background=self.border_colour, bd=0, highlightthickness=0)
        
        # Create an instance of whichever object was passed into interior_widget
        self.interior: tk.Widget = interior_widget.__new__(interior_widget)
        # Initialise that object
        self.interior.__init__(self, **kwargs)
        
        self.interior.pack(
            padx=(self.border_weights.left, self.border_weights.right),
            pady=(self.border_weights.top, self.border_weights.bottom)
        )
        
    def change_border_colour(self, colour: str) -> None:
        self.border_colour = colour
        
    def change_border_weights(self, weights: Directions, mode: Literal['add', 'absolute'] = 'absolute') -> None:
        match mode:
            case 'add':
                self.border_weights: Directions = self.border_weights + weights
            case 'absolute' | _:
                self.border_weights: Directions = weights
            
    

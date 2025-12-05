#—— External Imports —————————————————————————————————————————————————————————————————————————
import tkinter as tk
# from typing import Optional
#
# #—— Project Imports ——————————————————————————————————————————————————————————————————————————
# #————— GUI ——————————————————————————————————————
# from source.gui.directions import Directions
# #—————————————————————————————————————————————————————————————————————————————————————————————


class BorderedFrame(tk.Frame):
    def __init__(
            self,
            master: tk.Misc,
            border_colour: str = "",
            border_left: int = 0,
            border_top: int = 0,
            border_right: int = 0,
            border_bottom: int = 0,
            interior_widget=tk.Frame,
            **kwargs
    ) -> None:
        tk.Frame.__init__(self, master, background=border_colour, bd=0, highlightthickness=0)
        
        self.interior: tk.Frame = interior_widget(self, **kwargs)
        self.interior.pack(padx=(border_left, border_right), pady=(border_top, border_bottom))


# class BorderedFrame(tk.Frame):
#     def __init__(self, master, border_colour=None, border_weights: Directions=Directions(0, 0, 0, 0), interior_widget=tk.Frame, **kwargs):
#         tk.Frame.__init__(self, master, background=border_colour, bd=0, highlightthickness=0)
#
#         self.interior = interior_widget(self, **kwargs)
#         self.interior.pack(padx=(border_weights.left, border_weights.right), pady=(border_weights.top, border_weights.bottom))


# class BorderedFrame(tk.Frame):
#     """
#     Adapted from code by Miguel Martinez Lopez
#         https://code.activestate.com/recipes/580798-tkinter-frame-with-different-border-sizes/
#     """
#     def __init__(
#             self,
#             master: tk.Misc,
#             border_weights: Directions,
#             border_colour: str = "",
#             interior_widget=tk.Frame,
#             # border_left: int = 0,
#             # border_top: int = 0,
#             # border_right: int = 0,
#             # border_bottom: int = 0,
#             **kwargs
#     ) -> None:
#         tk.Frame.__init__(self, master, background=border_colour, bd=0, highlightthickness=0)
#
#         self.interior: tk.Frame = interior_widget(master=self, **kwargs)
#         self.interior.pack(
#             padx=(border_weights.left, border_weights.right),
#             pady=(border_weights.top, border_weights.bottom)
#         )

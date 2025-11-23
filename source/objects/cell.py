# — External Imports ————————————————————————————
from dataclasses import dataclass, field
from typing import Optional

# — Project Imports —————————————————————————————
# ———— Consts & Types ———————————————————————————
from common.constants import BOARD_SIZE, ALL_OPTIONS_SET
from common.types_ import colour, coordinates, Board_

# ———— Functions ————————————————————————————————
from common.functions.calculations import get_index_from_coords, get_parent_box_from_coords


# eq=False just fixes some functionality when Cells are used in sets
@dataclass(eq=False)
class Cell:
    # Mandatory properties
    index: int
    _parent: Board_
    
    # Optional properties
    #   (which honestly, except for value,
    #   will probably never be given on init -
    #   they're just being initialised themselves over here)
    value: Optional[int] = None
    possible_options: set[int] = field(default_factory=lambda: ALL_OPTIONS_SET.copy())
    
    corner_candidates: list[int] = field(default_factory=list)
    central_candidates: list[int] = field(default_factory=list)
    colours: list[colour] = field(default_factory=list)
    
    # — Initialisation ———————————————————————————————————————————————————————————————————————
    def __post_init__(self) -> None:
        self._parent.columns[self.x].add(self)
        self._parent.rows[self.y].add(self)
        self._parent.boxes[self.parent_box].add(self)
        
        # the board is stored such that the value of each cell is 0 if it's undefined -
        #   this just fixes that for easier logic
        if self.value == 0:
            self.value = None
        
        if self.value is not None:
            self.possible_options = {self.value}
    
    # — General Methods ——————————————————————————————————————————————————————————————————————
    # ——— remove_from_options ———————————————————
    def remove_from_options(self, to_remove: int) -> None:
        self.possible_options.remove(to_remove)
        # if there's only one possible value the cell can be,
        #   then set the cell to that value
        if len(self.possible_options) == 1:
            self.value = list(self.possible_options)[0]
    
    # — Property Methods —————————————————————————————————————————————————————————————————————
    # ——— x —————————————————————————————————————
    @property
    def x(self) -> int:
        return self.index % BOARD_SIZE
    
    # ——— y —————————————————————————————————————
    @property
    def y(self) -> int:
        return self.index // BOARD_SIZE
    
    # ——— coords ————————————————————————————————
    @property
    def coords(self) -> coordinates:
        return self.x, self.y
    
    @coords.setter
    def coords(self, xy: coordinates):
        self.index = get_index_from_coords(*xy)
    
    # ——— parent_box ————————————————————————————
    @property
    def parent_box(self) -> int:
        return get_parent_box_from_coords(*self.coords)
    
    # ——— sees ——————————————————————————————————
    @property
    def sees(self) -> set[Cell]:
        return self._parent.columns[self.x] | self._parent.rows[self.y] | self._parent.boxes[self.parent_box]
    
    # — Dunder Methods ———————————————————————————————————————————————————————————————————————
    def __str__(self) -> str:
        return str(self.value) if self.value is not None else "-"
    
    def __repr__(self) -> str:
        return str(self.possible_options) if self.possible_options is not None else f".{self.value}."
    # ————————————————————————————————————————————————————————————————————————————————————————

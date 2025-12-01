#—— External Imports —————————————————————————————————————————————————————————————————————————
from dataclasses import dataclass, field
from typing import Optional

#—— Project Imports ——————————————————————————————————————————————————————————————————————————
#————— Consts & Types ———————————————————————————
from source.common.constants import BOARD_SIZE, ALL_OPTIONS_SET
from source.common.types_ import cell_colour, coordinates, Board, CellInsertType

#————— Functions ————————————————————————————————
from source.common.functions.calculations import get_index_from_coords, get_parent_box_from_coords
#—————————————————————————————————————————————————————————————————————————————————————————————


type board_flat = list[Cell]
type board_matrix = list[list[Cell]]


def validate_input_type(number_to_check: int, type_: CellInsertType) -> None:
    if (number_to_check is cell_colour) and (type_ in (
            CellInsertType.VALUE, CellInsertType.CORNER, CellInsertType.CENTRE
    )):
        raise TypeError("'number_to_add' must be of type 'int'")
    elif (number_to_check is not cell_colour) and (type_ == "colour"):
        raise TypeError("'number_to_add' must be of type 'colour'")


@dataclass(eq=False)
# eq=False just fixes some functionality when Cells are used in sets
class Cell:
    #I)Mandatory properties
    index: int
    _parent: Board
    
    #I)Optional properties
    #    (which honestly, except for value, will probably never be given on init -
    #    they're just being initialised themselves over here)
    value: Optional[int] = None
    possible_options: set[int] = field(default_factory=lambda: ALL_OPTIONS_SET.copy())
    
    corner_candidates: list[int] = field(default_factory=list)
    central_candidates: list[int] = field(default_factory=list)
    colours: list[cell_colour] = field(default_factory=list)
    
    is_given_value: Optional[bool] = None
    
    #—— Initialisation ———————————————————————————————————————————————————————————————————————
    def __post_init__(self) -> None:
        # add the cell being created to the column, row, and box tracker of its parent
        #   this just makes it a lit easier to figure out which cells see which other cells
        self._parent.columns[self.x].add(self)
        self._parent.rows[self.y].add(self)
        self._parent.boxes[self.parent_box].add(self)
        
        # the board is stored such that the value of each cell is 0 if it's undefined -
        #   this just fixes that, for easier logic
        if self.value == 0:
            self.value = None
        
        # if the cell's value is given at initialisation,
        #   then there's only one option that can ever go in possible_options
        if self.value is not None:
            self.possible_options = {self.value}
            
        self.is_given_value = self.value is not None
    
    #—— General Methods ——————————————————————————————————————————————————————————————————————
    #———— remove_from_options() ———————————————————
    def remove_from_options(self, to_remove: int) -> None:
        # remove the given digit from this cell's possibility set
        #   [this will raise a KeyError if the value being removed isn't in the set]
        #     but that functionality is intended, as it's useful to see if something was actually removed,
        #     and the error is handled in {{Key Error Excepted}}
        self.possible_options.remove(to_remove)
        
        # if there's only one possible value left that the cell can be,
        #   then set the cell to that value
        if len(self.possible_options) == 1:
            self.value = list(self.possible_options)[0]
    
    def fill_or_add_number(self, number_to_add: int, input_type: CellInsertType) -> None:
        match input_type:
            case "value":  self.value = number_to_add
            case "corner": self.corner_candidates.append(number_to_add)
            case "centre": self.central_candidates.append(number_to_add)
            case "colour": self.colours.append(number_to_add)
            case _:
                raise ValueError("Invalid cell type")
    
    def remove_or_delete_number(self, number_to_remove: int, input_type: CellInsertType) -> None:
        match input_type:
            case "value":  self.value = None
            case "corner": self.corner_candidates.remove(number_to_remove)
            case "centre": self.central_candidates.remove(number_to_remove)
            case "colour": self.colours.remove(number_to_remove)
            case _:
                raise ValueError("Invalid cell type")
        
    def copy(self) -> Cell:
        new: Cell = object.__new__(Cell)
        
        state: dict[str, Any] = self.__dict__.copy()
        state["_parent"] = self._parent
        
        new.__dict__ = state
        return new
    
    #—— Property Methods —————————————————————————————————————————————————————————————————————
    #———— x —————————————————————————————————————
    @property
    def has_some_value(self) -> int:
        return self.value not in (0, None)
    
    #———— x —————————————————————————————————————
    @property
    def x(self) -> int:
        return self.index % BOARD_SIZE
    
    #———— y —————————————————————————————————————
    @property
    def y(self) -> int:
        return self.index // BOARD_SIZE
    
    #———— coords ————————————————————————————————
    @property
    def coords(self) -> coordinates:
        return self.x, self.y
    
    @coords.setter
    def coords(self, xy: coordinates) -> None:
        self.index = get_index_from_coords(*xy)
    
    #———— parent_box ————————————————————————————
    @property
    def parent_box(self) -> int:
        return get_parent_box_from_coords(*self.coords)
    
    #———— sees ——————————————————————————————————
    @property
    def sees(self) -> set[Cell]:
        # Get the union of the 3 sets containing the values that this cell can see
        return self._parent.columns[self.x] | self._parent.rows[self.y] | self._parent.boxes[self.parent_box]
    
    #—— Dunder Methods ———————————————————————————————————————————————————————————————————————
    def __str__(self) -> str:
        return str(self.value) if self.value is not None else "-"
    
    def __repr__(self) -> str:
        return str(self.possible_options) if self.possible_options is not None else f".{self.value}."

#———————————————————————————————————————————————————————————————————————————————————————————————————————————————————————

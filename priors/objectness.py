from typing import Tuple, List, Set

import copy
import numpy as np
from arc import ArcColors

from arc.types import ArcGrid

from priors.space import adjacent

Cell = Tuple[int, int]


class ArcObject:
    def __init__(self, cells: Set[Cell], color: int):
        x, y = (min(c[0] for c in cells), min(c[1] for c in cells))
        self.upper_left = x, y
        self._cells: Set[Cell] = {(xc - x, yc - y) for xc, yc in cells}
        self.color: int = color

    @property
    def area(self):
        return len(self._cells)

    @property
    def width(self):
        ys = [c[1] for c in self.mask]
        return 1 + max(ys) - min(ys)

    @property
    def heigth(self):
        xs = [c[0] for c in self.mask]
        return 1 + max(xs) - min(xs)

    @property
    def mask(self) -> Set[Cell]:
        x, y = self.upper_left
        return {(xc + x, yc + y) for xc, yc in self._cells}

    @property
    def bottom_right(self):
        x, y = self.upper_left
        return x + self.heigth - 1, y + self.width - 1

    @property
    def box(self):
        return self.upper_left, self.bottom_right

    def copy(self):
        return copy.deepcopy(self)

    def as_grid(self) -> ArcGrid:
        result = np.zeros([self.heigth, self.width], dtype=np.uint8)
        new = self.copy()
        new.upper_left = (0, 0)
        new.draw(result)
        return result

    def overlap(self, other: "ArcObject") -> Set[Cell]:
        return self.mask.intersection(other.mask)

    def fits(self, grid: ArcGrid) -> bool:
        (xmin, ymin), (xmax, ymax) = self.box
        return xmin > 0 and ymin > 0 and xmax < grid.shape[0] and ymax < grid.shape[1]

    def draw(self, grid: ArcGrid, at: Cell = None) -> None:
        """Draws the object onto the grid. """
        obj = self
        if at is not None:
            obj = obj.copy()
            obj.upper_left = at

        for cell in obj.mask:
            assert grid[cell] == ArcColors.BLACK, "don't want to overwrite other objects."

        for cell in obj.mask:
            grid[cell] = obj.color

    def remove_from(self, grid: ArcGrid) -> None:
        """Paints the cells where object was in black. """
        for cell in self.mask:
            assert grid[cell] == self.color, "Object appears not to be there.."

        for cell in self.mask:
            grid[cell] = ArcColors.BLACK


def merge(grid: ArcGrid, start: Cell, diag: bool, multicolor:bool) -> ArcObject:
    visited = {start}
    color = grid[start]
    stack = list(adjacent(grid, start, diag))
    while stack:
        nxt = stack.pop()
        if grid[nxt] == color or (multicolor and grid[nxt] != ArcColors.BLACK):
            visited.add(nxt)
            stack += list(adjacent(grid, nxt, diag) - visited)

    return ArcObject(visited, color)


def find_objects(grid: ArcGrid, allow_diag: bool=False, multicolor: bool = False) -> List[ArcObject]:
    results = []
    grid = np.copy(grid)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j] == 0:
                continue
            new_obj = merge(grid, (i, j), allow_diag, multicolor)
            results.append(new_obj)
            for cell in new_obj.mask:
                grid[cell] = 0

    return results

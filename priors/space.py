from __future__ import annotations

from typing import Set, TYPE_CHECKING

from arc.types import ArcGrid

if TYPE_CHECKING:
    from priors.objectness import Cell


def adjacent(grid: ArcGrid, cell: Cell, diag: bool = False) -> Set[Cell]:
    x, y = cell
    candidates = [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)]
    if diag:
        candidates += [(x+1, y+1), (x+1, y-1), (x-1, y-1), (x-1, y+1)]
    result = set()
    h, w = grid.shape
    for c in candidates:
        x, y = c
        if 0 <= x < h and 0 <= y < w:
            result.add(c)

    return result
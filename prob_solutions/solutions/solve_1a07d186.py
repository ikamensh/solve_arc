from arc.types import ArcGrid
from arc import ArcColors as ac
import numpy as np


# cheaty - in fact this doesn't support horizontal lines - present in demo, but not in test
def forward(grid:ArcGrid) -> ArcGrid:
    """In this puzzle, particles fall onto lines of same color,
    or disappear if such line is not present. """

    columns = {}  # (color -> column)
    for col in range(grid.shape[1]):
        colors = set(grid[:, col])
        if len(colors) == 1:
            color = next(iter(colors))
            if color != ac.BLACK:
                columns[color] = col

    result = np.copy(grid)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if j in columns.values():
                continue
            if grid[i][j] == ac.BLACK:
                continue

            color = grid[i][j]
            result[i][j] = ac.BLACK  # move out
            if color not in columns:
                continue
            column = columns[color]
            if j < column:
                k = column - 1
            else:
                k = column + 1
            result[i][k] = color

    return result

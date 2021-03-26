from arc.types import ArcGrid
from arc import ArcColors

from priors.space import adjacent


def forward(grid:ArcGrid) -> ArcGrid:
    """In this puzzle, only bigger rectangles are preserved, small particles disappear. """
    grid = grid.copy()
    x, y = grid.shape

    for i in range(x):
        for j in range(y):
            if grid[i,j] != ArcColors.BLACK:
                count_nb_neighbours = 0
                for n in adjacent(grid, (i,j), diag=False):
                    if grid[n] != ArcColors.BLACK:
                        count_nb_neighbours+= 1

                if count_nb_neighbours < 2:
                    grid[i,j] = ArcColors.BLACK

    return grid
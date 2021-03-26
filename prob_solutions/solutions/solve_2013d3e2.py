from arc.types import ArcGrid

from priors.objectness import find_objects

def forward(grid:ArcGrid) -> ArcGrid:
    """In this puzzle, drops fall from bombers on the floor. """

    obj = find_objects(grid, multicolor=True, allow_diag=True)[0]
    x, y = obj.upper_left
    quarter = grid[x:x+obj.heigth//2, y:y+obj.width//2]

    return quarter

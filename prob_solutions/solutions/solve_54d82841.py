from arc.types import ArcGrid
from arc import ArcColors as ac
import numpy as np

from priors import physics
from priors.objectness import ArcObject, find_objects

def forward(grid:ArcGrid) -> ArcGrid:
    """In this puzzle, drops fall from bombers on the floor. """

    result = np.copy(grid)

    bombers = find_objects(grid)

    # in this puzzle, drop appears at (1, 1) w.r.t. each bomber.
    for b in bombers:
        x, y = b.upper_left
        d = ArcObject({(x+1, y+1)}, color=ac.YELLOW)
        d.draw(result)
        physics.drop(result, d)

    return result

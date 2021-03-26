from arc.types import ArcGrid

from priors.objectness import find_objects

def forward(grid:ArcGrid) -> ArcGrid:
    """In this puzzle, we need to find biggest object by the area. """

    objs = find_objects(grid)
    biggest = max(objs, key=lambda o: o.area)

    return biggest.as_grid()

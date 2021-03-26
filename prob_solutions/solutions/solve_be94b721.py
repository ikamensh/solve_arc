from arc.types import ArcGrid

from priors.objectness import find_objects

def forward(grid:ArcGrid) -> ArcGrid:
    """In this puzzle, particles fall onto lines of same color,
    or disappear if such line is not present. """

    objs = find_objects(grid)
    biggest = max(objs, key=lambda o: o.area)

    return biggest.as_grid()

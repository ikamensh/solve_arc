from arc.types import ArcGrid

from priors.objectness import ArcObject


def drop(grid: ArcGrid, obj: ArcObject, direction=(1, 0)):
    obj.remove_from(grid)

    dx, dy = direction
    x, y = obj.upper_left
    new_obj = obj.copy()
    new_obj.upper_left = (x + dx, y + dy)

    while new_obj.fits(grid):
        obj = new_obj
        x, y = obj.upper_left
        new_obj = obj.copy()
        new_obj.upper_left = (x + dx, y + dy)

    obj.draw(grid)

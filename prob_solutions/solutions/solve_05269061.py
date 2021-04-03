from arc.types import ArcGrid
from arc import ArcColors

from priors.objectness import find_objects
from actions.draw import draw_ray

def go_down_right(grid):
    h, w = grid.shape
    x, y = 0, 0
    def check() : return 0 <= x < h and 0 <= y < w
    while check():
        yield x, y
        x += 1
        if not check(): break
        yield x, y
        y += 1


def forward(grid:ArcGrid) -> ArcGrid:
    """In this puzzle, we need to find biggest object by the area. """

    grid = grid.copy()
    colors = set()
    for row in grid:
        for cell in row:
            colors.add(cell)
    colors -= {ArcColors.BLACK}

    period = len(colors)

    assert grid.shape[0] == grid.shape[1]
    keypoints = list(go_down_right(grid))
    for x, y in keypoints:
        if grid[x][y] in colors:
            color = grid[x][y]
            cur = keypoints.index((x,y)) % period
            while cur < len(keypoints):
                draw_ray(grid, keypoints[cur], 1, -1, color)
                cur += period

    return grid




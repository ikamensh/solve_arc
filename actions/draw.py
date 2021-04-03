from typing import Tuple

from arc.types import ArcGrid


def draw_line(
    grid: ArcGrid, start: Tuple[int, int], end: Tuple[int, int], color: int
) -> None:
    xa, ya = start
    xb, yb = end
    dx, dy = xb - xa, yb - ya
    straight = dx == 0 or dy == 0
    diagonal = abs(dx) == abs(dy)
    if not straight and not diagonal:
        raise Exception("only horizontal, vertical and diagonal lines are supported.")

    grid[xa, ya] = color
    while xa != xb or ya != yb:
        xa += dx
        ya += dy
        grid[xa, ya] = color


def draw_ray(grid: ArcGrid, start: Tuple[int, int], dx, dy, color):
    h, w = grid.shape
    x, y = start
    while 0 <= x < h and 0 <= y < w:
        grid[x, y] = color
        x, y = x + dx, y + dy

    x, y = start
    while 0 <= x < h and 0 <= y < w:
        grid[x, y] = color
        x, y = x - dx, y - dy

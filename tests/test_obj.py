from priors.objectness import find_objects, ArcObject
from priors.space import adjacent
from arc import get_train_problem_by_uid, ArcColors

import numpy as np


def test_obj_simple():
    cells = [(0, 0), (1, 0), (0, 1), (0, 2), (1, 2)]
    bomber = ArcObject(set(cells), color=ArcColors.RED)

    assert bomber.width == 3
    assert bomber.heigth == 2
    assert bomber.upper_left == (0, 0)
    assert bomber.bottom_right == (1, 2)
    assert bomber.mask == set(cells)



def test_obj_moved():
    cells = [(0, 1), (1, 1), (0, 2), (0, 3), (1, 3)]
    bomber = ArcObject(set(cells), color=ArcColors.RED)

    assert bomber.width == 3
    assert bomber.heigth == 2
    assert bomber.upper_left == (0, 1)
    assert bomber.bottom_right == (1, 3)
    assert bomber.mask == set(cells)


def test_find_objects():

    drop_prob = get_train_problem_by_uid("54d82841")
    first_demo = drop_prob.train_pairs[0]

    assert len(find_objects(first_demo.x)) == 2
    obj1, obj2 = find_objects(first_demo.x)
    assert obj1.area == 5
    assert obj1.width == 3
    assert obj1.heigth == 2
    assert obj1.color == ArcColors.FUCHSIA

    assert len(find_objects(first_demo.y)) == 4
    assert len(set(o.area for o in find_objects(first_demo.y))) == 2
    assert len(set(o.color for o in find_objects(first_demo.y))) == 2


def test_adjacent():
    grid = np.zeros([3, 3])

    assert len(adjacent(grid, (0, 0))) == 2
    assert len(adjacent(grid, (0, 1))) == 3
    assert len(adjacent(grid, (1, 0))) == 3
    assert len(adjacent(grid, (1, 1))) == 4
    assert len(adjacent(grid, (2, 0))) == 2
    assert len(adjacent(grid, (2, 2))) == 2

    assert (0, 1) in adjacent(grid, (0, 0))
    assert (1, 0) in adjacent(grid, (0, 0))


def test_fits():
    grid = np.zeros([3, 3])

    good = ArcObject({(1, 1)}, color=ArcColors.GREEN)
    assert good.fits(grid)

    bad1 = ArcObject({(-4, 1)}, color=ArcColors.RED)
    assert not bad1.fits(grid)

    bad2 = ArcObject({(5, 1)}, color=ArcColors.GREY)
    assert not bad2.fits(grid)

    bad3 = ArcObject({(5, 1111)}, color=ArcColors.FUCHSIA)
    assert not bad3.fits(grid)

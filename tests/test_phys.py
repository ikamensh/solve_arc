import numpy as np
from arc import ArcColors

from priors.physics import drop
from priors.objectness import ArcObject


def test_drop():

    grid = np.zeros([3,3])

    blob = ArcObject({(1, 1)}, color=ArcColors.RED)
    blob.draw(grid)
    drop(grid, blob)

    expected = np.zeros([3,3])
    expected[2,1] = ArcColors.RED

    assert np.all( grid == expected )

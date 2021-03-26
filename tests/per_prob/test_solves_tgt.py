import pytest

from arc import get_train_problem_by_uid
from arc.types import verify_is_arc_grid

import numpy as np

from prob_solutions.agent import solutions_dir, import_module

solved = [
    "1a07d186",
    "54d82841",
    "be94b721",
    "2013d3e2",
    "7f4411dc"
]
@pytest.fixture(params=solved)
def problem(request):
    yield request.param


def test_solves(problem):
    prob = get_train_problem_by_uid(problem)

    path = f"{solutions_dir}/solve_{problem}.py"
    mod = import_module(path)

    for tg, target in zip(prob.test_inputs, prob.test_outputs):
        prediction = mod.forward(tg)
        verify_is_arc_grid(prediction)
        assert np.all(prediction == target)

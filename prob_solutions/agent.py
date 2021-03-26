import collections
from typing import List

from arc import ArcIOPair
from arc.agents import RandomAgent
from arc.types import ArcGrid, ArcPrediction


import os
import importlib.util
import sys

import numpy as np

here = os.path.dirname(__file__)
solutions_dir = os.path.join(here, "solutions")

def import_module(file_path):
    module_name = file_path.split("/")[-1].replace(".py", "")

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
    except FileNotFoundError as e:
        raise ImportError from e
    else:
        return module


class HardcodedAgent(RandomAgent):
    def __init__(self):
        self.solutions = []
        for file in os.listdir(solutions_dir):
            if not ".py" in file:
                continue
            mod = import_module(os.path.join(solutions_dir, file))
            self.solutions.append(mod.forward)

    def predict(
        self, demo_pairs: List[ArcIOPair], test_grids: List[ArcGrid]
    ) -> List[ArcPrediction]:
        demo_results = collections.defaultdict(list)
        for pair in demo_pairs:
            for sol in self.solutions:
                try:
                    out = sol(pair.x)
                except:
                    score = -1
                else:
                    score = np.mean(out == pair.y)
                    if out.shape == pair.y.shape:
                        score += 1

                demo_results[sol].append(score)

        demo_results = {sol: sum(scores) for sol, scores in demo_results.items()}
        best = sorted(self.solutions, key=demo_results.__getitem__, reverse=True)[:3]

        result = []
        for tg in test_grids:
            maybe_answers = []
            for sol in best:
                try:
                    maybe_answers.append(sol(tg))
                except:
                    pass

            result.append(maybe_answers)

        return result

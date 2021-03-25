from typing import List, Tuple

import numpy as np

from arc import ArcIOPair
from arc.agents import ArcAgent
from arc.types import ArcGrid, ArcPrediction


class ShapeAgent(ArcAgent):
    def predict_shape(
        self, demo_pairs: List[ArcIOPair], test_grids: List[ArcGrid]
    ) -> List[Tuple[int, int]]:
        out_same_as_in = all(p.x.shape == p.y.shape for p in demo_pairs)
        if out_same_as_in:
            return [g.shape for g in test_grids]  # noqa

        out_shapes = set(pair.y.shape for pair in demo_pairs)
        all_same = len(out_shapes)
        if all_same:
            return next(iter(out_shapes))  # noqa

        # ran out of hardcoded rules to determine the shape...
        return [(1, 1) for g in test_grids]

    def predict(
        self, demo_pairs: List[ArcIOPair], test_grids: List[ArcGrid]
    ) -> List[ArcPrediction]:
        shapes = self.predict_shape(demo_pairs, test_grids)
        return [
            [np.zeros(shape=shape, dtype=np.uint8)]
            for shape, g in zip(shapes, test_grids)
        ]


if __name__ == '__main__':
    from arc.evaluation import evaluate_agent

    agent = ShapeAgent()
    result = evaluate_agent(agent)
    print(result)

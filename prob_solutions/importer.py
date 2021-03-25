import os
import importlib.util
import sys

here = os.path.dirname(__file__)


def import_module(prob_name):
    module_name = f"solve_{prob_name}"
    file_path = f"{here}/solutions/{module_name}.py"

    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
    except FileNotFoundError as e:
        raise ImportError from e
    else:
        return module


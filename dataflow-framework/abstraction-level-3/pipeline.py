import yaml
import importlib
from processor_types import ProcessorFn


def load_pipeline(config_path: str) -> list[ProcessorFn]:
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    steps = config.get("pipeline", [])
    processors = []

    for step in steps:
        path = step["type"]
        module_path, func_name = path.rsplit(".", 1)
        try:
            module = importlib.import_module(module_path)
            func = getattr(module, func_name)
            processors.append(func)
        except (ModuleNotFoundError, AttributeError) as e:
            raise ImportError(f"Could not load processor {path}: {e}")

    return processors

from typing import Optional
from .config_loader import load_config

def say_hello(name: Optional[str] = None) -> str:
    target = name or "World"
    config = load_config()
    num_times = config.get("num_times", 1)

    message = f"Hello, {target}!"
    full_message = "\n".join([message] * num_times)
    return full_message

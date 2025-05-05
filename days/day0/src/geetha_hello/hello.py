from rich import print
from typing import Optional

def say_hello(name: Optional[str] = None) -> None:
    """
    Prints a rich-formatted hello message.

    Args:
        name (Optional[str]): Name to greet. Defaults to 'World'.
    """
    target = name or "World"
    print(f"[bold green]Hello, {target}![/bold green]")

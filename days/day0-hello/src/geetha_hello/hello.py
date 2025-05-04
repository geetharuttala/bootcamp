from rich import print
from typing import Optional
import sys

def say_hello(name: Optional[str] = None) -> None:
    """
    Prints a rich-formatted hello message.

    Args:
        name (Optional[str]): Name to greet. Defaults to 'World'.
    """
    target = name or "World"
    print(f"[bold green]Hello, {target}![/bold green]")

if __name__ == "__main__":
    # Get name from command-line arguments if provided
    name_arg = sys.argv[1] if len(sys.argv) > 1 else None
    say_hello(name_arg)

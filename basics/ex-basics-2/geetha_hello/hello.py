from rich.console import Console
import sys

# Force terminal if the output is NOT a terminal (e.g., PyCharm run button)
force = not sys.stdout.isatty()

console = Console(force_terminal=force)

def say_hello(name: str = "World") -> None:
    console.print(f"[bold green]Hello, {name}![/bold green]")

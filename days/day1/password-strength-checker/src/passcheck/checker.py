# src/passcheck/checker.py

import typer
from rich import print
from rich.console import Console

app = typer.Typer()
console = Console()

def evaluate_strength(password: str) -> str:
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if length >= 12 and score == 4:
        return "Strong"
    elif length >= 8 and score >= 3:
        return "Moderate"
    else:
        return "Weak"

@app.command()
def check(password: str = typer.Argument(..., help="The password to evaluate")):
    """Check the strength of a password."""
    result = evaluate_strength(password)
    console.print(f"[bold cyan]Password Strength:[/bold cyan] {result}")

if __name__ == "__main__":
    app()

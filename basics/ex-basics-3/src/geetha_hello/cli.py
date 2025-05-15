import typer
from rich import print
from .hello import say_hello

app = typer.Typer()

@app.command()
def main(name: str = "World"):
    """CLI to say hello"""
    print(say_hello(name))

if __name__ == "__main__":
    app()

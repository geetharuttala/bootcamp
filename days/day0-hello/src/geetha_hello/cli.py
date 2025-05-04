import typer
from .hello import say_hello

app = typer.Typer()

@app.command()
def greet(name: str = "world"):
    """
    Greets the user with their name.
    """
    typer.echo(say_hello(name))

if __name__ == "__main__":
    app()

import typer
from geetha_hello.hello import say_hello

app = typer.Typer()

@app.command("many-hellos")
def many_hellos(names: list[str]):
    for name in names:
        print(say_hello(name))  # <- this is the only print now

if __name__ == "__main__":
    app()

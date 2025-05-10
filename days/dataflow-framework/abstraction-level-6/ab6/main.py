# ab6/main.py
import typer
from pathlib import Path
from ab6.router_engine import load_config, run_router

app = typer.Typer()

@app.command()
def main(
    input: Path = typer.Option(..., help="Path to input file"),
    config: Path = typer.Option(..., help="Path to config YAML"),
    visualize: bool = typer.Option(False, help="Visualize the routing graph and save it as a PNG")
):
    with input.open() as infile:
        lines = (line.strip() for line in infile)
        config_data = load_config(config)
        run_router(config_data, lines, visualize=visualize)

if __name__ == "__main__":
    app()

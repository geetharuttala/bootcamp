import typer
from pathlib import Path
from dag_engine import load_dag, run_dag

app = typer.Typer()

@app.command()
def process(
        input: Path = typer.Option(..., help="Input file path"),
        config: Path = typer.Option(..., help="Path to pipeline YAML config")):
    with input.open() as f:
        lines = (line.rstrip("\n") for line in f)
        root = load_dag(str(config))
        run_dag(root, lines)

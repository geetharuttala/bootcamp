import typer
from pathlib import Path

app = typer.Typer()

@app.command()
def process(
    input: Path = typer.Option(..., "--input", help="Input file"),
    output: Path = typer.Option(None, "--output", help="Output file"),
    config: Path = typer.Option(..., "--config", help="Path to pipeline.yaml")
):
    from core import apply_pipeline
    from pipeline import load_pipeline

    processors = load_pipeline(str(config))

    with open(input, "r") as f:
        lines = (line for line in f)

        transformed = apply_pipeline(lines, processors)

        if output:
            with open(output, "w") as out:
                for line in transformed:
                    out.write(line + "\n")
        else:
            for line in transformed:
                print(line)

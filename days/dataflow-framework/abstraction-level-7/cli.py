import typer

app = typer.Typer()

@app.command()
def run(
    input: str = typer.Option(..., help="Path to the input file"),
    config: str = typer.Option(..., help="Path to the pipeline configuration YAML"),
    trace: bool = typer.Option(False, help="Enable execution tracing"),
):
    from main import main
    main(input, config, trace)

if __name__ == "__main__":
    app()

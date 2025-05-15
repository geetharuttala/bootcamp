# cli.py

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

@app.command()
def watch(
    config: str = typer.Option(..., help="Path to the pipeline configuration YAML"),
):
    """Start the folder watcher and dashboard (Level 8)."""
    from file_watcher import start_watcher
    from dashboard.server import start_dashboard
    from utils.metrics import metrics_store
    from utils.tracing import trace_store
    import threading

    print("[CLI] Starting file watcher and dashboard...")

    # Start the watcher
    start_watcher(config)

    # Start the dashboard with required dependencies
    start_dashboard(metrics_store, trace_store)


if __name__ == "__main__":
    app()

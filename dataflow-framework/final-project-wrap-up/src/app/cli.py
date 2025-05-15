# Updated cli.py with state-based routing support

import typer
import signal
import sys
from app.main import run_once, run_watch
import os

app = typer.Typer()

# Default config file path
DEFAULT_CONFIG_PATH = "src/config/pipeline.yaml"


@app.command()
def run(
        input: str = typer.Option(None, help="Path to the input file"),
        config: str = typer.Option(None, help="Path to the pipeline configuration YAML"),
        trace: bool = typer.Option(False, help="Enable execution tracing"),
        watch: bool = typer.Option(False, help="Enable folder watch mode"),
        host: str = typer.Option("0.0.0.0", help="Host for the dashboard server"),
        port: int = typer.Option(8000, help="Port for the dashboard server"),
):
    # Find config file if not specified
    if config is None:
        config_paths = [
            DEFAULT_CONFIG_PATH,
            "src/app/config/pipeline.yaml",
            "config/pipeline.yaml",
        ]
        for path in config_paths:
            if os.path.exists(path):
                config = path
                break

        if config is None:
            typer.echo(f"Error: Could not find configuration file. Please specify with --config")
            raise typer.Exit(code=1)

    if watch:
        print(f"[MAIN] Running in folder watch mode.")
        print(f"[MAIN] Visit your dashboard at: http://{host}:{port}/health")
        run_watch(config)
    elif input:
        run_once(input, config, trace)
    else:
        typer.echo("Please specify either --input <file> or --watch")
        raise typer.Exit(code=1)


def handle_shutdown_signal(sig, frame):
    print("Shutting down gracefully...")
    sys.exit(0)


signal.signal(signal.SIGINT, handle_shutdown_signal)

if __name__ == "__main__":
    app()
# src/app/cli.py

import typer
import signal
import sys
from app.main import run_once, run_watch

app = typer.Typer()

@app.command()
def run(
    input: str = typer.Option(None, help="Path to the input file"),
    config: str = typer.Option(..., help="Path to the pipeline configuration YAML"),
    trace: bool = typer.Option(False, help="Enable execution tracing"),
    watch: bool = typer.Option(False, help="Enable folder watch mode"),
):
    if watch:
        print("[MAIN] Running in folder watch mode.")
        print("[MAIN] Visit your dashboard at: http://geethar.mooo.com:8000/health")
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

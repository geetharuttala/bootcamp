import typer
from typing import Optional, Iterator
from dotenv import load_dotenv
import os
import sys

app = typer.Typer()
load_dotenv()

def read_lines(path: str) -> Iterator[(str)]:
    with open(path, 'r') as f:
        for line in f:
            yield line.strip()

def transform_line(line: str, mode: str) -> str:
    if mode == 'uppercase':
        return line.upper()
    elif mode == 'snakecase':
        return line.replace(' ','_').lower()
    else:
        raise ValueError(f"Unsupported mode: {mode}")

def write_output(lines: Iterator[str], output_path: Optional[[str]]) -> None:
    if output_path:
        with open(output_path, 'w') as f:
            for line in lines:
                f.write(line + '\n')
    else:
        for line in lines:
            print(line)


@app.command()
def main(
    input: str = typer.Option(..., help="Input file path"),
    output: Optional[str] = typer.Option(None, help="Optional output file path"),
    mode: Optional[str] = typer.Option(None, help="Processing mode")
):
    mode = mode or os.getenv("MODE", "uppercase")
    lines = read_lines(input)
    processed = (transform_line(line, mode) for line in lines)
    write_output(processed, output)

if __name__ == "__main__":
    app()
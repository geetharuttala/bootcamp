from dotenv import load_dotenv
import os
from typing import Optional

from pipeline import get_pipeline
from core import apply_processors

load_dotenv()

def read_lines(path: str):
    with open(path) as f:
        for line in f:
            yield line

def write_output(lines, output_path: Optional[str]):
    if output_path:
        with open(output_path, 'w') as f:
            for line in lines:
                f.write(line + '\n')
    else:
        for line in lines:
            print(line)

def run(input_path: str, output_path: Optional[str], mode: Optional[str]):
    mode = mode or os.getenv("MODE", "uppercase")
    processors = get_pipeline(mode)
    lines = (apply_processors(line, processors) for line in read_lines(input_path))
    write_output(lines, output_path)

if __name__ == "__main__":
    import cli
    cli.app()

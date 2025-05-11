from setuptools import setup, find_packages

setup(
    name="file-processing-sys",
    version="0.1.0",
    description="A real-time file processing system with FastAPI and CLI.",
    author="Your Name",
    author_email="you@example.com",
    packages=find_packages(where="src"),  # Tell setuptools to look in the 'src' folder
    package_dir={"": "src"},  # Direct setuptools to use 'src' as the root for packages
    include_package_data=True,  # Include non-Python files via MANIFEST.in
    install_requires=[
        "fastapi",
        "uvicorn",
        "typer",
        "pydantic",
        "rich",
        "networkx",
        "watchdog",
        "pyyaml",
    ],
    entry_points={
        'console_scripts': [
            'fpsys = file_processing_sys.cli:app',  # This allows running 'fpsys' from the CLI
        ]
    },
)

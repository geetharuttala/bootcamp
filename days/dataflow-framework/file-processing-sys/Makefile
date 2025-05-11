# Makefile for file-processing-sys

.PHONY: run run-file docker-build docker-run clean publish build-pkg publish-pkg

# Run in watch mode
run:
	python main.py --watch

# Run in single-file mode: make run-file FILE=input.txt
run-file:
	python main.py --input $(FILE)

# Build Docker image
docker-build:
	docker build -t file-processing-sys .

# Run Docker container with volume mount
docker-run:
	docker run -it --rm -p 8000:8000 -v $(PWD)/watch_dir:/app/watch_dir file-processing-sys

# Build Python package
build-pkg:
	python -m build

# Publish Python package
publish-pkg:
	twine upload dist/*

# Clean generated files
clean:
	find . -name '*.pyc' -delete
	rm -rf __pycache__/ build/ dist/ *.egg-info

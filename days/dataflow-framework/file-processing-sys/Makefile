# Makefile for file-processing-sys

.PHONY: run run-file docker-build docker-run clean publish build-pkg publish-pkg docker-compose-up docker-compose-down

# Run in watch mode
# Run the application directly with PYTHONPATH set to src
run:
	PYTHONPATH=src python -m app.cli --watch --config src/app/config/pipeline.yaml

# Run in single-file mode: make run-file FILE=input.txt
run-file:
	PYTHONPATH=src python -m cli run --input $(FILE) --config src/config/pipeline.yaml

# Build Docker image
docker-build:
	docker build -t file-processing-sys .

# Run Docker container with volume mount and pass the config option
docker-run:
	-docker rm -f file-processing-sys || true
	docker run -it -p 8000:8000 \
		-v $(pwd)/watch_dir:/app/watch_dir \
		-v $(pwd)/src/config:/app/src/config \
		--name file-processing-sys \
		file-processing-sys \
		python /app/src/app/cli.py --watch --config /app/src/config/pipeline.yaml

# Run the application with Docker Compose
docker-compose-up:
	docker-compose up  # Runs the containers in detached mode

# Stop and remove containers with Docker Compose
docker-compose-down:
	docker-compose down  # Stops and removes the containers

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

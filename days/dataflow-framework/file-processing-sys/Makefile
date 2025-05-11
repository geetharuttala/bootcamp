.PHONY: run run-file docker-build docker-run clean publish build-pkg publish-pkg

# Run in watch mode
run:
	PYTHONPATH=src python -m app.cli --watch --config src/app/config/pipeline.yaml

# Run in single-file mode: make run-file input=test.txt
run-file:
	PYTHONPATH=src python -m app.cli --input $(input) --config src/app/config/pipeline.yaml

# Build Docker image
docker-build:
	docker build -t file-processing-sys .

# Run Docker container with volume mount and pass the config option
docker-run:
	docker run -it --rm -p 8000:8000 \
		-v $(PWD)/watch_dir:/app/watch_dir \
		-v $(PWD)/src/config:/app/src/config \
		file-processing-sys python /app/src/app/cli.py --watch --config /app/src/config/pipeline.yaml

# Build Python package
build-pkg:
	python -m build

# Publish Python package
publish-pkg:
	twine upload dist/*

# Clean generated files
clean:
	# Delete all .pyc files
	find . -name '*.pyc' -delete
	# Remove __pycache__, build, dist, and .egg-info directories
	rm -rf __pycache__/ build/ dist/ *.egg-info src/file_processing_sys.egg-info

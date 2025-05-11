# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Set PYTHONPATH to include src
ENV PYTHONPATH=/app/src

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install the package in editable mode
RUN pip install -e .

# Expose the dashboard port
EXPOSE 8000

# Set default command to start in watch mode with the new port and config path
CMD ["python", "src/app/cli.py", "watch", "--config", "src/config/pipeline.yaml", "--host", "0.0.0.0", "--port", "8001"]

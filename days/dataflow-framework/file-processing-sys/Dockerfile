# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the dashboard port
EXPOSE 8000

# Set default command to start in watch mode
CMD ["python", "main.py", "--watch"]

# Use official Python image as base
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /app/

# Expose port for Uvicorn
EXPOSE 5000

# Set PYTHONPATH to ensure absolute imports work
ENV PYTHONPATH=/app

# Debug: Print working directory and files before running Uvicorn
CMD ["sh", "-c", "pwd && ls -l && uvicorn main:app --host 0.0.0.0 --port 5000"]

# Base image (modern Python version)
FROM python:3.12-slim

# Prevents Python from writing pyc files & enables cleaner logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside container
WORKDIR /app

# Install system dependencies (important for psycopg2, etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project into container
COPY . .

# Default command (you can override with docker-compose later)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
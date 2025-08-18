# Use a slim Python base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Avoid writing .pyc files and force stdout logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    build-essential \
    && apt-get clean

# Set pip version (stable and compatible)
RUN pip install --upgrade pip==23.2.1

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy entire Django project into container
COPY . .

# Expose Django default port
EXPOSE 8000

# Default command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

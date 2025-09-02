# Use a full Python image to avoid mysqlclient build issues
FROM python:3.11

WORKDIR /code

# Prevent Python from writing pyc files and enable unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    libssl-dev \
    && apt-get clean

# Upgrade pip
RUN pip install --upgrade pip setuptools wheel

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project files
COPY . .

EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

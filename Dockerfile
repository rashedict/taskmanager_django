<<<<<<< HEAD
# Use official Python 3.13 image
FROM python:3.13.1-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1


# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libssl-dev \
    libffi-dev \
    libmariadb-dev \
    && apt-get clean

# Copy requirements first
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Django project code
COPY . /app/

# Expose Django port
EXPOSE 8000

# Run the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
=======
# Use official Python 3.13 image
FROM python:3.13.1-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1


# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    build-essential \
    libssl-dev \
    libffi-dev \
    libmariadb-dev \
    && apt-get clean

# Copy requirements first
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Django project code
COPY . /app/

# Expose Django port
EXPOSE 8000

# Run the development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
>>>>>>> be6276b (Initial commit for taskmanager microservice)

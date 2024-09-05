# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app

# Expose port
EXPOSE 5000

# Set environment variables for Flask
ENV FLASK_APP=core/server.py
ENV FLASK_ENV=production

# Use Gunicorn as the WSGI server for production, point to core
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "core.server:app"]

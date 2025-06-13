# Use a lightweight official Python image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Install OS dependencies
RUN apt-get update && apt-get install -y build-essential libpq-dev

# Copy dependency list and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Collect static files (if any)
RUN python manage.py collectstatic --noinput
# Run the application using Gunicorn
CMD ["gunicorn", "product-service.wsgi:application", "--bind", "0.0.0.0:8000"]

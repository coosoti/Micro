# Use Python base image
FROM python:3.10-slim

# Set work directory inside the container
WORKDIR /app

# Copy dependencies list and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . .

# Run the application using Gunicorn
CMD ["gunicorn", "order-service.wsgi:application", "--bind", "0.0.0.0:8000"]

# Micro - Django MicroServices Implementation


🧑‍💻 user_service - Django Microservice for User Management

📌 Overview

user_service is a Django RESTful microservice that handles user registration, login, and profile management. It includes token-based authentication using Django REST Framework’s Token Authentication.

⸻

🚀 Features
	•	User Registration with secure password hashing
	•	User Login with token authentication
	•	Authenticated Profile Retrieval
	•	Dockerized for containerized deployment
	•	PostgreSQL as the primary database

⸻

📂 Project Structure

user_service/
│
├── Dockerfile
├── requirements.txt
├── manage.py
├── user_service/
│   └── settings.py, urls.py, wsgi.py, etc.
└── users/
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    └── ...


⸻

⚙️ Setup Instructions

1. Clone the Repository

git clone <your-repo-url>
cd user_service

2. Configure Environment (Optional)

Edit the database config in user_service/settings.py if not using Docker Compose:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'user_service_db',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


⸻

🐳 Docker Setup

3. Build and Run the Container

docker build -t user_service_container .
docker run -p 8000:8000 user_service_container

4. With Docker Compose
```
# docker-compose.yml (example snippet)
version: '3.8'
services:
  user_service:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DEBUG=1
    depends_on:
      - db
  db:
    image: postgres:13
    environment:
      POSTGRES_DB: user_service_db
      POSTGRES_USER: db_user
      POSTGRES_PASSWORD: db_password
```
```
docker-compose up --build
```

⸻

📫 API Endpoints

Method	Endpoint	Description	Auth Required
POST	/api/users/register/	Register a new user	❌
POST	/api/users/login/	Login, receive token	❌
GET	/api/users/profile/	View user profile	✅

Use Authorization: Token <your_token> in headers for protected routes.

⸻

📦 product_service - Django Microservice for Product Management

📌 Overview

product_service is a standalone Django REST microservice for creating, listing, updating, and deleting product entries.

⸻

🚀 Features
	•	CRUD operations on Product Model
	•	DRF Generic Views for performance
	•	RESTful endpoints
	•	Docker-ready
	•	PostgreSQL supported

⸻

📂 Project Structure

product_service/
│
├── Dockerfile
├── requirements.txt
├── manage.py
├── product_service/
│   └── settings.py, urls.py, wsgi.py, etc.
└── products/
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    └── ...


⸻

⚙️ Setup Instructions

1. Clone the Repository

git clone <your-repo-url>
cd product_service

2. Edit Database Settings (Optional)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'product_service_db',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


⸻

🐳 Docker Setup

3. Build and Run

docker build -t product_service_container .
docker run -p 8001:8000 product_service_container


⸻

📫 API Endpoints

Method	Endpoint	Description
GET	/api/products/	List all products
POST	/api/products/	Create a new product
GET	/api/products/<id>/	Retrieve a product
PUT	/api/products/<id>/	Update a product
DELETE	/api/products/<id>/	Delete a product

Example POST Request (via Postman or cURL):

POST /api/products/
{
  "name": "Laptop",
  "description": "A powerful device",
  "price": 999.99,
  "stock": 10
}

# Inventory Service (Microservice)

This is the Inventory microservice in a Django-based microservices architecture. It manages product stock levels, availability, and updates.

## 🚀 Features

- Add and manage inventory for products
- RESTful API using Django REST Framework
- Containerized with Docker
- Ready for integration with Product and Order services

## 🧱 Tech Stack

- Python 3.10
- Django 4.x
- Django REST Framework
- PostgreSQL (or SQLite for development)
- Docker + Gunicorn

## 📦 Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/inventory_service.git
cd inventory_service
```

🔧 Step 1: Dockerfile

Create a Dockerfile in the root of your inventory_service project:

# Use Python base image
FROM python:3.10-slim

# Set work directory inside the container
WORKDIR /app

# Copy dependencies list and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . .

# Collect static files (if needed)
RUN python manage.py collectstatic --noinput || true

# Expose port
EXPOSE 8002

# Run the application using Gunicorn
CMD ["gunicorn", "inventory_service.wsgi:application", "--bind", "0.0.0.0:8002"]


⸻

📦 Step 2: requirements.txt

Generate your dependencies if not already created:

pip freeze > requirements.txt

Make sure the following are included:

Django>=4.2
djangorestframework
gunicorn


⸻

🧪 Step 3: Build & Run

# Build the image
docker build -t inventory_service_container .

# Run the container
docker run -p 8002:8002 inventory_service_container

Make sure you’re using a different port from the other services (e.g., 8000 for user, 8001 for product).

⸻

📝 README.md for inventory_service

Here’s a starter README you can modify as needed:

⸻


# Inventory Service (Microservice)

This is the Inventory microservice in a Django-based microservices architecture. It manages product stock levels, availability, and updates.

## 🚀 Features

- Add and manage inventory for products
- RESTful API using Django REST Framework
- Containerized with Docker
- Ready for integration with Product and Order services

## 🧱 Tech Stack

- Python 3.10
- Django 4.x
- Django REST Framework
- PostgreSQL (or SQLite for development)
- Docker + Gunicorn

## 📦 Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/inventory_service.git
cd inventory_service

2. Create virtual environment

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Apply migrations

python manage.py migrate

5. Run locally

python manage.py runserver 8002


⸻

🐳 Docker Instructions

Build the Docker image

docker build -t inventory_service_container .

Run the Docker container

docker run -p 8002:8002 inventory_service_container


⸻

📬 API Endpoints

Method	Endpoint	Description
GET	/api/inventory/	List inventory items
POST	/api/inventory/	Add new stock entry
GET	/api/inventory/<id>/	Retrieve stock by ID
PUT	/api/inventory/<id>/	Update stock
DELETE	/api/inventory/<id>/	Remove stock item


⸻

🧪 Testing With Postman

POST /api/inventory/
Content-Type: application/json

{
  "product_id": 1,
  "quantity": 100
}


⸻

🔗 Related Services
	•	User Service (port 8000)
	•	Product Service (port 8001)

⸻

📄 License

MIT © 2025 Charles

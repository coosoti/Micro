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

🧾 Order Service

The Order Service is a microservice built using Django and Django REST Framework (DRF) that handles the creation and management of customer orders. It communicates with the Product Service to validate product IDs before processing any order.

⸻

📦 Features
	•	Create, retrieve, update, and delete orders
	•	Validates that a product exists before accepting an order
	•	Quantity validation to prevent invalid data
	•	RESTful API endpoints with Swagger documentation

⸻

📁 Project Structure

order_service/
├── orders/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py         # Order model
│   ├── serializers.py    # Validation logic
│   ├── views.py          # API views
│   ├── urls.py           # Route definitions
├── order_service/
│   ├── settings.py
│   ├── urls.py           # Main URL router
├── manage.py
├── Dockerfile
├── requirements.txt


⸻

🚀 Getting Started

1. Clone the Repository

git clone https://github.com/your-username/order_service.git
cd order_service

2. Create a Virtual Environment (Optional)

python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

3. Install Dependencies

pip install -r requirements.txt

4. Run Migrations

python manage.py migrate

5. Start the Development Server

python manage.py runserver 8003


⸻

🐳 Docker Usage

Build and Run

docker build -t order_service_container .
docker run -p 8003:8000 order_service_container

Ensure the Product Service is running and accessible at http://product_service:8000.

⸻

🛠 API Endpoints

✅ Create an Order

POST /api/orders/

Body:

{
  "customer_name": "Alice",
  "product_id": 1,
  "quantity": 3
}

📦 List All Orders

GET /api/orders/

🔍 Retrieve Single Order

GET /api/orders/{id}/

♻️ Update Order

PUT /api/orders/{id}/

❌ Delete Order

DELETE /api/orders/{id}/


⸻

📚 Swagger/OpenAPI Docs

Access API documentation at:

http://localhost:8003/swagger/


⸻

🧪 Testing With Postman
	•	Use POST to create new orders.
	•	Try invalid product_id or quantity to test validations.
	•	Ensure product_service is running in Docker or accessible to your Order Service container.

⸻

🔒 Validations
	•	quantity must be greater than 0
	•	product_id must exist in Product Service

⸻

🔗 Related Services
	•	Product Service: Validates the existence of products
	•	Inventory Service (optional): Can be integrated to validate stock levels

⸻
📄 License MIT © 2025 Charles

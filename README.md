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

docker-compose up --build


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


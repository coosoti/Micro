
🧩 Microservices Overview

This project follows a microservices architecture using Django REST Framework. The following services are implemented:

Service	Description	URL Prefix	Port
User	Manages user registration & authentication	/api/users/	8000
Product	Handles product creation & listing	/api/products/	8001
Inventory	Tracks product stock levels	/api/inventory/	8002
Order	Processes orders	/api/orders/	8003


⸻

⚙️ Architecture Diagram

                            +-------------+
                            |  Frontend   |
                            +------+------+ 
                                   |
             +---------------------|----------------------+
             |                    API Gateway             |
             +-----------+---------+---------+-----------+
                         |                   |
         +---------------+                   +----------------+
         |                                      |
+--------v--------+        +----------------+   +----------------+
|  User Service   |<------>|  Order Service |-->| Inventory Svc  |
|    (8000)       |        |     (8003)     |   |    (8002)      |
+-----------------+        +----------------+   +----------------+
                              ^
                              |
                          +---+----+
                          | Product |
                          | Service |
                          | (8001)  |
                          +--------+


⸻

🚀 How to Run with Docker Compose
	1.	Create .env files (optional for environment configs)
	2.	Start all services:

docker-compose up --build

	3.	Access Each Service:

	•	User: http://localhost:8000/api/users/
	•	Product: http://localhost:8001/api/products/
	•	Inventory: http://localhost:8002/api/inventory/
	•	Order: http://localhost:8003/api/orders/

⸻

📦 Postman Collection

You can import this Postman Collection JSON (replace # with actual link if hosted or share as file).

⸻

📘 Swagger/OpenAPI Documentation

Each service includes Swagger/OpenAPI documentation at:
	•	User: http://localhost:8000/swagger/
	•	Product: http://localhost:8001/swagger/
	•	Inventory: http://localhost:8002/swagger/
	•	Order: http://localhost:8003/swagger/

Use drf-yasg or drf-spectacular in your services:

pip install drf-yasg

Add to each service’s urls.py:

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
   openapi.Info(title="Service API", default_version='v1'),
   public=True,
   permission_classes=(AllowAny,),
)

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]


⸻

✅ Sample Test Flow

To test service-to-service flow:
	1.	Create Product
POST http://localhost:8001/api/products/
	2.	Add Inventory
POST http://localhost:8002/api/inventory/
	3.	Place Order
POST http://localhost:8003/api/orders/

Backend will:
	•	Call Product to verify product exists.
	•	Call Inventory to reduce stock.
	•	Save Order.

⸻

🧪 Integration Behavior
	1.	Verify:
	•	Order created successfully
	•	Inventory reduced
	•	Product reference is valid
	2.	Error Scenarios:
	•	Ordering non-existent product returns error.
	•	Insufficient stock returns error.

⸻

📁 Directory Structure

root/
├── user_service/
├── product_service/
├── inventory_service/
├── order_service/
├── docker-compose.yml
└── README.md


⸻

✍️ Contributors
	•	You (Project Lead 👨‍💻)

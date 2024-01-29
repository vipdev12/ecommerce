TechSpace E-commerce Project
Project Name: TechSpace(ecommerce)
Project Description:
TechSpace is an e-commerce platform built on Django, designed to provide users with a seamless and efficient experience in purchasing electronics. Whether you are looking for the latest gadgets, high-end smartphones, or cutting-edge electronics, TechSpace has you covered. The platform aims to create a user-friendly environment for both buyers and sellers, offering a diverse range of products and features.

Features:
1. User Authentication:

Secure user authentication and authorization mechanisms for a personalized experience.
2. Product Catalog:

A comprehensive catalog of electronics, including detailed product descriptions, specifications, and images.
3. Search and Filter:

Powerful search and filtering options to help users find the products they are looking for quickly.
4. Shopping Cart:

Intuitive shopping cart functionality for users to easily manage their selected items before proceeding to checkout.
5. Checkout Process:

Streamlined and secure checkout process with multiple payment options for a hassle-free purchasing experience.
6. Order Tracking:

Order tracking system to keep users informed about the status of their purchases.
7. User Reviews and Ratings:

Allow users to leave reviews and ratings for products to help others make informed decisions.
8. Responsive Design:

A responsive and mobile-friendly design to ensure a seamless experience across various devices.
Technologies Used:
Backend Framework: Django
Database: PostgreSQL
Frontend: HTML, CSS, JavaScript, BootStrap
Payment: Deliver, By cash
Authentication: Django Authentication System

Getting Started:

1. Clone the Repository:

git clone https://github.com/vipdev1988/ecommerce.git
cd ECommerceSite

2. Create Virtual Environment:

python -m venv venv

3. Activate Virtual Environment:

Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

4. Install Dependencies:

pip install -r requirements.txt

5. Run Migrations:

python manage.py migrate

6. Create Superuser:

python manage.py createsuperuser

7. Run the development server:

python manage.py runserver


Docker Setup:

1. Build Docker Image:

docker build  .
2. Run Docker Compose:

docker-compose up

License:
This project is licensed under the MIT License.

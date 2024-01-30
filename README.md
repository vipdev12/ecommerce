### TechSpace E-commerce Project


**Project Name:** TechSpace(ecommerce)


**Project Description:**
TechSpace is an e-commerce platform built on Django, designed to provide users with a seamless and efficient experience in purchasing electronics. Whether you are looking for the latest gadgets, high-end smartphones, or cutting-edge electronics, TechSpace has you covered. The platform aims to create a user-friendly environment for both buyers and sellers, offering a diverse range of products and features.

### Features:

## 1. User Authentication:

Ensure a secure and personalized experience through robust user authentication and authorization mechanisms.
## 2. Product Catalog:

Explore a diverse range of electronics with a comprehensive catalog. Detailed product descriptions, specifications, and high-quality images provide users with valuable information.
## 3. Search and Filter:

Easily find desired products with powerful search and filtering options. Streamline the shopping experience by quickly narrowing down choices.
## 4. Shopping Cart:

Manage selected items effortlessly with an intuitive shopping cart. Users can review, add, or remove items before proceeding to a seamless checkout process.
## 5. Checkout Process:

Experience a streamlined and secure checkout process. Multiple payment options ensure a hassle-free purchasing experience, catering to diverse user preferences.
## 6. Order Tracking:

Stay informed about the status of your purchases through an efficient order tracking system. Track shipments and delivery updates for a transparent and reliable experience.
User Reviews and Ratings:

## 7. Contribute to the community by leaving reviews and ratings for products. This feature helps fellow users make informed decisions based on real experiences.
Responsive Design:

Enjoy a seamless and consistent user experience across various devices. The responsive design ensures accessibility and usability, providing a user-friendly interface.

## Screenshots:

Home page(categories):
![home page](https://i.ibb.co/qMFgQjJ/191.png)
Subcategories:
![sub categories](https://i.ibb.co/THJzszP/192.png)
Product detail:
![product detail](https://i.ibb.co/THJzszP/192.png)
Cart:
![Cart](https://i.ibb.co/4pF9qV3/199.png)
Billing Address Page:
![BillingAddress](https://i.ibb.co/0KZNQC7/200.png)


## Technologies Used:
Backend Framework: Django
Database: PostgreSQL
Frontend: HTML, CSS, JavaScript, BootStrap
Payment: Deliver, By cash
Authentication: Django Authentication System

##Getting Started:

## 1. Clone the Repository:

```
git clone https://github.com/vipdev1988/ecommerce.git
cd ECommerceSite
```
## 2. Create Virtual Environment:
```
python -m venv venv
```
## 3. Activate Virtual Environment:

Windows:
```
venv\Scripts\activate
```
Linux/Mac:
```
source venv/bin/activate
```
## 4. Install Dependencies:
```
pip install -r requirements.txt
```
## 5. Run Postgresql server

Linux/mac:
```
sudo service postgresql start
```
Windows:
Run postgresql on Windows

## 6. Run Migrations:
```
python manage.py migrate
```
## 7. Create Superuser:
```
python manage.py createsuperuser
```

## 8. Run redis server

```
redis-server
```

## 8. Run the development server:
```
python manage.py runserver
```

### Docker Setup:

## 1. Build Docker Image:
```
docker build  .
```
## 2. Run Docker Compose:
```
docker-compose up
```
License:
This project is licensed under the MIT License.

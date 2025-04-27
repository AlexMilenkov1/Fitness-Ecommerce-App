# Fitness Ecommerce App

Welcome to the **Fitness Ecommerce App**! This is a fully-featured Django-based e-commerce platform where users can shop for fitness products. The application includes an admin interface, user authentication, shopping cart functionality, and more. It has been deployed using Render.

[Visit the Fitness Ecommerce App](https://fitness-app-tcv5.onrender.com/)

## Features

- **User Authentication**: Users can create accounts, log in, and log out
- **Product Management**: Staff and admins can add, update, and delete products
- **Shopping Cart**: Regular users can add products to their shopping cart
- **Support Ticket System**: Users can submit support tickets and staff can resolve them
- **Admin Panel**: Full-featured admin panel with the ability to manage users, products, and orders

## Project Setup

### 1. Clone the repository

```bash
git clone https://github.com/AlexMilenkov1/Fitness-Ecommerce-App.git
```

### 2. Navigate to project directory

```bash
cd fitnessEcommerceApp
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Change DB settings in settings.py
In settings.py, update the database configuration to connect to your PostgreSQL database:

```bash
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "your_db_name",
        "USER": "your_username",
        "PASSWORD": "your_pass",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
```


### 5. Run migrations
 ```bash
python manage.py migrate
```


### 6. Run development server
```bash
python manage.py runserver
```

### 7. Create superuser (for admin access)
```bash
python manage.py createsuperuser
```

# # # User Roles
There are three types of users:

-Regular Users: Can browse products and manage their shopping cart

-Staff: Can resolve support tickets and manage certain aspects of the site

-Admins: Have full access to manage products, orders, users, and support tickets

### Admin Panel
Access the admin panel at http://127.0.0.1:8000/admin/ after creating a superuser.

### Deployment
The app is deployed on Render using GitHub Actions for CI/CD. Every push to the main branch triggers:

Dependency installation

Static files collection

Automatic deployment to Render

### Technologies Used
- Django 5.1

- PostgreSQL

- Bootstrap 5

- Cloudinary (for media storage)

- Whitenoise (for static files)

- Render (for deployment)


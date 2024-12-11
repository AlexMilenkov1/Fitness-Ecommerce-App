from django.core.management.base import BaseCommand
from fitnessEcommerceApp.products.models import Category, Product


class Command(BaseCommand):
    help = "Populate the database with initial categories and products."

    def handle(self, *args, **kwargs):
        # Create categories
        categories = [
            {"name": "Sport", "description": "Sport mats and accessories."},
            {"name": "Cardio", "description": "Running, joggging, and more."},
            {"name": "Apparel", "description": "Fitness clothing for all."}
        ]

        for cat_data in categories:
            category, created = Category.objects.get_or_create(**cat_data)
            self.stdout.write(self.style.SUCCESS(
                f"{'Created' if created else 'Exists'} category: {category.name}"
            ))

        # Create products
        products = [
            {
                "category": Category.objects.get(name="Sport"),
                "name": "Red T-Shirt",
                "description": "Experience ultimate comfort and style with the red T-Shirt,"
                               " crafted from premium breathable cotton. Designed for active lifestyles,"
                               " this t-shirt features a modern slim-fit cut and reinforced seams for durability."
                               " Perfect for workouts or casual wear, the Dred T-Shirt is available in vibrant colors"
                               " that never fade, ensuring you look your best every time. Upgrade your wardrobe with"
                               " this versatile and reliable essential!",
                "price": 30.99,
                "in_stock": 50,
                "rating": 4,
                "image_url": "images/product-1.jpg"
            },
            {
                "category": Category.objects.get(name="Cardio"),
                "name": "Sneakers",
                "description": "Experience ultimate comfort and style with the sneakers,"
                               " crafted from premium breathable cotton. Designed for active lifestyles,"
                               " this t-shirt features a modern slim-fit cut and reinforced seams for durability."
                               " Perfect for workouts or casual wear, the Dred T-Shirt is available in vibrant colors"
                               " that never fade, ensuring you look your best every time. Upgrade your wardrobe with"
                               " this versatile and reliable essential!",
                "price": 80.99,
                "in_stock": 30,
                "rating": 0,
                "image_url": "images/product-2.jpg"
            },
            {
                "category": Category.objects.get(name="Apparel"),
                "name": "Fitness Trousers",
                "description": "Experience ultimate comfort and style with the sneakers,"
                               " crafted from premium breathable cotton. Designed for active lifestyles,"
                               " this t-shirt features a modern slim-fit cut and reinforced seams for durability."
                               " Perfect for workouts or casual wear, the Dred T-Shirt is available in vibrant colors"
                               " that never fade, ensuring you look your best every time. Upgrade your wardrobe with"
                               " this versatile and reliable essential!",
                "price": 15.50,
                "in_stock": 100,
                "rating": 1,
                "image_url": "images/product-3.jpg"
            },
            {
                "category": Category.objects.get(name="Apparel"),
                "name": "Classy Sport T-shirt",
                "description": "Experience ultimate comfort and style with the sneakers,"
                               " crafted from premium breathable cotton. Designed for active lifestyles,"
                               " this t-shirt features a modern slim-fit cut and reinforced seams for durability."
                               " Perfect for workouts or casual wear, the Dred T-Shirt is available in vibrant colors"
                               " that never fade, ensuring you look your best every time. Upgrade your wardrobe with"
                               " this versatile and reliable essential!",
                "price": 60.50,
                "in_stock": 100,
                "rating": 5,
                "image_url": "images/product-4.jpg"
            },
            {
                "category": Category.objects.get(name="Sport"),
                "name": "Runners",
                "description": "Experience ultimate comfort and style with the sneakers,"
                               " crafted from premium breathable cotton. Designed for active lifestyles,"
                               " this t-shirt features a modern slim-fit cut and reinforced seams for durability."
                               " Perfect for workouts or casual wear, the Dred T-Shirt is available in vibrant colors"
                               " that never fade, ensuring you look your best every time. Upgrade your wardrobe with"
                               " this versatile and reliable essential!",
                "price": 120.99,
                "in_stock": 100,
                "rating": 5,
                "image_url": "images/product-5.jpg"
            },
            {
                "category": Category.objects.get(name="Apparel"),
                "name": "Puma T-shirt",
                "description": "Experience ultimate comfort and style with the sneakers,"
                               " crafted from premium breathable cotton. Designed for active lifestyles,"
                               " this t-shirt features a modern slim-fit cut and reinforced seams for durability."
                               " Perfect for workouts or casual wear, the Dred T-Shirt is available in vibrant colors"
                               " that never fade, ensuring you look your best every time. Upgrade your wardrobe with"
                               " this versatile and reliable essential!",
                "price": 20.50,
                "in_stock": 100,
                "rating": 5,
                "image_url": "images/product-6.jpg"
            },
            {
                "category": Category.objects.get(name="Apparel"),
                "name": "Socks",
                "description": "Experience ultimate comfort and style with the sneakers,"
                               " crafted from premium breathable cotton. Designed for active lifestyles,"
                               " this t-shirt features a modern slim-fit cut and reinforced seams for durability."
                               " Perfect for workouts or casual wear, the Dred T-Shirt is available in vibrant colors"
                               " that never fade, ensuring you look your best every time. Upgrade your wardrobe with"
                               " this versatile and reliable essential!",
                "price": 9.99,
                "in_stock": 2,
                "rating": 3,
                "image_url": "images/product-7.jpg"
            },
        ]

        for prod_data in products:
            product, created = Product.objects.get_or_create(**prod_data)
            self.stdout.write(self.style.SUCCESS(
                f"{'Created' if created else 'Exists'} product: {product.name}"
            ))

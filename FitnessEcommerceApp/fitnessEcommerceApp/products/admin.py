from django.contrib import admin

from fitnessEcommerceApp.products.models import Product, Category


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'in_stock', 'rating')
    search_fields = ('name', 'category__name')
    list_filter = ('category', 'rating', 'price')

    ordering = ('name',)

    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'category', 'price', 'in_stock', 'rating', 'image_url')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'description', 'category', 'price', 'in_stock', 'rating', 'image_url'),
        }),
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_filter = ('name',)

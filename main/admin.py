from django.contrib import admin
from .models import Product

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'is_featured']
    list_filter = ['category', 'is_featured']
    search_fields = ['name', 'description']
    list_editable = ['is_featured']
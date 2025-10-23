from django.contrib import admin
from .models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "featured")
    list_filter = ("featured",)
    search_fields = ("title", "description")


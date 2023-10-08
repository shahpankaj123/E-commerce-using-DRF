from django.contrib import admin
from .models import *

class ProductInline(admin.TabularInline):
    model = ProductLine

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductInline,
    ]

admin.site.register(Brand)
admin.site.register(Category)


# Register your models here.

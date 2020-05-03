from django.contrib import admin
from .models import Products, Category, Brand, Colors, Sizes, Style, ProductSizes, ProductSubs

# Register your models here.
admin.site.register(Products)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Colors)
admin.site.register(Sizes)
admin.site.register(Style)
admin.site.register(ProductSizes)
admin.site.register(ProductSubs)
from django.contrib import admin
from .models import PortfolioItem, Category

# Register your models here.
admin.site.register(PortfolioItem)
admin.site.register(Category)
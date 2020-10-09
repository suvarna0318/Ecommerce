from import_export import resources
from django.contrib import admin
from .models import Product


# Register your models here.






class ProductResource(resources.ModelResource):

    class Meta:
        model = Product


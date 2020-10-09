# from import_export import resources
from django.contrib import admin
from .models import Category,Product


# Register your models here.
admin.site.register(Category)

admin.site.register(Product)


# class ProductResource(resources.ModelResource):

#     class Meta:
#         model = Product


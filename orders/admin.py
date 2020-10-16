from django.contrib import admin
from .models import Order,OrderHistory

# Register your models here.
admin.site.register(Order)
admin.site.register(OrderHistory)

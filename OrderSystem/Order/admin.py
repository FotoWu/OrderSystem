from django.contrib import admin
from Order.models import Menu,Order

# Register your models here.
admin.site.register([Menu, Order])
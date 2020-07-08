from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone_number", "date")
    list_filter = ("date", "lead")
    search_fields = ("full_name", "address")
    list_per_page = 25


class ProductAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "quantity")
    list_filter = ("name",)
    search_fields = ("name",)
    list_per_page = 25


class OrderAdmin(admin.ModelAdmin):
    list_display = ("product_name", "order_quantity", "date", "total_price")
    list_filter = ("product_name", "date", "customer")
    search_fields = ("product_name", "customer")
    list_per_page = 25

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order2, OrderAdmin)
admin.site.unregister(Group)

admin.site.site_header = "پنل مدیریت ارتباط با مشتری"
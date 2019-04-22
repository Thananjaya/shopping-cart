from django.contrib import admin
from .models import Order, OrderItems

class OrderItemInline(admin.TabularInline):
	model=OrderItems
	raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'first_name', 'last_name', 'email', 'pin_code', 'paid', 'created_at', 'updated_at']
	list_filter = ['paid', 'created_at', 'updated_at']
	search_fields = ['first_name', 'last_name']
	inlines = [OrderItemInline]

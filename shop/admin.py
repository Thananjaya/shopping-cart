from django.contrib import admin
from .models import Category, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ['name', 'image', 'category', 'price', 'stock', 'available']
	list_filter = ['price', 'stock']
	# list_editable = ['price', 'stock', 'available']
	prepopulated_fields = {'slug': ('name',)}
	raw_id_fields = ['category']
	search_fields = ['name', 'category', 'price']
	ordering = ['name']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('title', 'description')
	prepopulated_fields = {'slug': ('title',)}
	search_fields = ('title',)
	ordering = ('title',)
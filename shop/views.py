from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from gurney.forms import AddProductToGurneyForm

def products_index(request, c_slug=None):
	category = None
	products = Product.objects.filter(available = True)
	categories = Category.objects.all()
	if c_slug:
		category = get_object_or_404(Category, slug = c_slug)
		products = Product.objects.filter(category = category)
	return render(request, 'products/index.html', {"products": products, "categories": categories, "category": category})

def product_detail(request, id, slug):
	product = get_object_or_404(Product, available= True, id = id, slug = slug)
	image_class = ''
	add_product_to_gurney_form = AddProductToGurneyForm();
	if product.image:
		image_class= "product-detail-image"
	return render(request, 'products/detail.html', {"product": product, 'add_product_to_gurney_form': add_product_to_gurney_form , "image": image_class})
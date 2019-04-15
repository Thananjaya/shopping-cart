from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from shop.models import Product
from .forms import AddProductToGurneyForm
from .gurney import Gurney


@require_POST
def add_product_to_gurney(request, product_id):
	product = get_object_or_404(Product, id = product_id)
	gurney = Gurney(request)
	form = AddProductToGurneyForm(request.POST)
	if form.is_valid():
		form_data = form.cleaned_data
		gurney.add(product = product, quantity = form_data['quantity'], quantity_update = form_data['update'])
	return redirect('gurney:gurney_detail')

def remove_product_from_gurney(request, product_id):
	product = get_object_or_404(Product, id = product_id)
	gurney = Gurney(request)
	gurney.remove(product = product)
	return ('gurney:gurney_detail')

def gurney_detail(request):
	gurney = Gurney(request)
	return render(request, 'gurney/gurney_detail.html', {'gurney': gurney})


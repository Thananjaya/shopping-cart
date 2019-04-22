from django.shortcuts import render
from .forms import PlaceOrderForm
from .models import OrderItems
from gurney.gurney import Gurney

def create_order(request):
	gurney = Gurney(request)
	if request.method == 'POST':
		order = PlaceOrderForm(request.POST)
		if form.is_valid():
			order = form.save()
			for item in gurney:
				OrderItem.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
			gurney.clear()
			return render(request, 'orders/order_placed.html', {'order': order})
	else: 
		form = PlaceOrderForm()
		return render(request, 'orders/place_order.html', {'form': form, 'gurney': gurney})


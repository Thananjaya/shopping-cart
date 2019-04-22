from django.shortcuts import render
from .forms import PlaceOrderForm
from .models import OrderItems
from .tasks import order_created
from gurney.gurney import Gurney

def create_order(request):
	gurney = Gurney(request)
	if request.method == 'POST':
		order_form = PlaceOrderForm(request.POST)
		if order_form.is_valid():
			order = order_form.save()
			for item in gurney:
				OrderItems.objects.create(order=order, product=item['product'], price=item['price'], quantity=item['quantity'])
			gurney.clear()
			order_created.delay(order.id)
			return render(request, 'orders/order_placed.html', {'order': order})
	else: 
		form = PlaceOrderForm()
		return render(request, 'orders/place_order.html', {'form': form, 'gurney': gurney})

from django import  forms
from .models import Order

class PlaceOrderForm(forms.ModelForm):
	class Meta:
		model = Order
		fields = ['first_name', 'last_name', 'email', 'address', 'city', 'pin_code']

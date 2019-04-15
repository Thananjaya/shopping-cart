from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Gurney(object):

	def __init__(self, request):
		"""
			Initializing the gurney/cart or checking the gurney existence 
		"""
		self.session = request.session
		gurney  = self.session.get(settings.CART_SESSION_ID)
		if not gurney:
			gurney = self.session[settings.CART_SESSION_ID] = {}
		self.gurney = gurney

	def __iter__(self):
		"""
			Iterate over products in cart/gurney
		"""
		product_ids = self.gurney.keys()
		products = Product.objects.filter(id__in= product_ids)
		gurney = self.gurney.copy()
		for product in products:
			gurney[str(product.id)]['product'] = product
		for items in gurney.values():
			item['price'] = Decimal(item['price'])
			item['total_price'] = item['price'] * item['quantity']
			yield item

	def __len__(self):
		""" Counting the total quantities been added in the cart"""
		total_quantities = sum(item['quantity'] for item in self.gurney.values())
		return total_quantities

	def add(self, product, quantity=1, quantity_update=False):
		"""
			adding a product to its gurney
		"""
		product_id = str(product.id)
		if product_id not in self.gurney:
			self.gurney[product_id] = {'quantity': 0, 'price': str(product.price)}
		if quantity_update:
			self.gurney[product_id]['quantity'] = quantity
		else:
			self.gurney[product_id]['quantity'] += quantity
		self.save()

	def save(self):
		""" Saving an session, in this case gurney/cart session"""
		self.session.modified = True

	def total_price(self):
		total_prices = sum(Decimal(item['total_price']) * item['quantity'] for item in self.gurney.values())
		return total_prices

	def remove(self, product):
		product_id = str(product.id)
		del self.gurney[product_id]
		self.save()

	def clear(self):
		"""removing the card from the session"""
		del self.session[settings.CART_SESSION_ID]
		self.save()



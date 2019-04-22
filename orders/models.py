from django.db import models
from shop.models import Product


class Order(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField()
	address = models.TextField()
	pin_code = models.CharField(max_length=6)
	city = models.CharField(max_length=50)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	paid = models.BooleanField(default=False)

	class Meta:
		ordering = ('-created_at',)

	def __str__(self):
		return 'Order by {}, id {}'.format(self.last_name, self.id)

	def get_total_cost(self):
		total_cost = sum(item.get_cost() for item in self.items.all())
		return total_cost

class OrderItems(models.Model):
	order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
	product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	quantity = models.PositiveIntegerField(default=1)

	def __str__(self):
		return "{}".format(self.id)

	def get_cost(self):
		return self.price * self.quantity

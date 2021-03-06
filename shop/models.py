from django.db import models
from django.urls import reverse

class Category(models.Model):
	title = models.CharField(max_length = 250, unique = True)
	description = models.TextField(blank = True)
	slug = models.SlugField(max_length = 250, unique = True)

	class Meta:
		ordering = ('title',)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('shop:product_index_by_category', args=[self.slug])

class Product(models.Model):
	name = models.CharField(max_length = 250, unique = True)
	description = models.TextField(blank = True)
	category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = "products")
	slug = models.SlugField(max_length = 250,  unique = True)
	image = models.ImageField(upload_to='product', blank = True)
	price = models.DecimalField(max_digits = 6, decimal_places = 2)
	stock = models.IntegerField()
	available = models.BooleanField(default = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	class Meta:
		ordering = ('name',)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('shop:product_detail', args=[self.id, self.slug])
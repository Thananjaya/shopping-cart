from django import template
from ..models import Category

register = template.Library()

@register.simple_tag
def categories_list():
	categories = Category.objects.all()
	return categories
from django.urls import path
from . import views

app_name = 'gurney'

urlpatterns = [
	path('gurney_details/', views.gurney_detail, name = 'gurney_detail'),
	path('add/<int:product_id>', views.add_product_to_gurney, name = 'gurney_add'),
	path('remove/<int:product_id>', views.remove_product_from_gurney, name= 'gurney_remove')
]
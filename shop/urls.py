from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
	path('', views.products_index, name='product_index'),
	path('<slug:c_slug>/', views.products_index, name='product_index_by_category'),
	path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail')
] 
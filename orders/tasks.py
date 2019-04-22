from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
	order = Order.objects.get(id=order_id)
	subject = 'Order, number {}, is successfully been made'.format(order.id)
	message = 'Respectfull {}, \n\n your order is been successfully made'.format(order.first_name)
	mail_sent = send_mail(subject, message, "thananthanan@gmail.com", [order.email])
	return mail_sent
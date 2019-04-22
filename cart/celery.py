import os
from celery import Celery


# setting the default django setting module for celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cart.settings')

app = Celery('cart')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop_project.settings')

app = Celery('myshop_project', broker="amqp://guest:guest@localhost:5672//")

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

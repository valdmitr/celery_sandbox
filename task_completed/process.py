from celery import Celery
from kombu import Queue

app = Celery('process',
             broker='pyamqp://guest@localhost//',
             backend='amqp://')



app.conf.task_queues = (Queue('default', exchange='direct_task_completed', routing_key='status',),)
app.conf.task_routes = ()
app.conf.task_default_queue = 'default'
app.conf.task_default_exchange = 'direct_task_completed'
app.conf.task_default_exchange_type = 'direct'
app.conf.task_default_routing_key = 'status'


@app.task
def process_task(body):
    print(body)
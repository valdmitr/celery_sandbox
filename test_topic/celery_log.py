from celery import Celery

import update

app = Celery('celery_log', backend='rpc://', broker='pyamqp://guest@localhost//')

app.conf.task_default_queue = 'log'
app.conf.task_default_exchange = 'top'
app.conf.task_default_exchange_type = 'topic'

# task_routes = {'#.log': {'queue': 'test'}}

app.conf.task_default_routing_key = '#.log'

@app.task(routing_key="#.log")
def get_log(body, status):
    print(status)
    return body
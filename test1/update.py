from celery import Celery

import celery_log

app = Celery('update', backend='rpc://', broker='pyamqp://guest@localhost//')
app.conf.task_default_queue = 'home'

@app.task
def see_string(body):
    celery_log.get_log.apply_async(args=[body], queue='log')
    return body



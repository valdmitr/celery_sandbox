from celery import Celery

import celery_log
import my_celery_worker

app = Celery('update', backend='rpc://', broker='pyamqp://guest@localhost//')
app.conf.task_default_queue = 'home'

@app.task
def see_string(body, status):
    if status == 'ok':
        print(status)
        celery_log.get_log.apply_async(args=[body, status], queue='log')
    else:
        status = "ok"
        my_celery_worker.show_result.apply_async(args=[body, status],
                                                 queue='test')
        celery_log.get_log.apply_async(args=[body, status], queue='log')
    return body



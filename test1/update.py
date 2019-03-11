from celery import Celery

import celery_log
import my_celery_worker

app = Celery('update', backend='rpc://', broker='pyamqp://guest@localhost//')
app.conf.task_default_queue = 'home'

@app.task
def see_string(body, status):
    print(status)
    if status == 'ok':
        celery_log.get_log.apply_async(args=[body, status], queue='log')
        return body
    else:
        celery_log.get_log.apply_async(args=[body, status], queue='log')
        status = "ok"
        my_celery_worker.show_result.apply_async(args=[body, status],
                                                 queue='test')





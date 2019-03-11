from celery import Celery

import update
import celery_log
import my_celery_worker

app = Celery('celery_log', backend='rpc://', broker='pyamqp://guest@localhost//')

# app.config_from_object('celeryconfig')
# app.conf.task_routes = {'test1': {'queue': 'test1'}}
app.conf.task_default_queue = 'test'


@app.task
def show_result(body, status):
    print(status)
    if status == 'ok':
        update.see_string.apply_async(args=[body, status], queue='home')
        celery_log.get_log.apply_async(args=[body, status], queue='log')
        return body
    else:
        celery_log.get_log.apply_async(args=[body, status], queue='log')
        status = "ok"
        my_celery_worker.show_result.apply_async(args=[body, status], queue='test')

    # # для теста, чтобы неверный статус дошел в update
    # update.see_string.apply_async(args=[body, status], queue='home')
    # celery_log.get_log.apply_async(args=[body, status], queue='log')
    # return body

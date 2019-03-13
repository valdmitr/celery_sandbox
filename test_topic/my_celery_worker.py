from celery import Celery

import update
import celery_log
import my_celery_worker

app = Celery('celery_log', backend='rpc://', broker='pyamqp://guest@localhost//')

app.conf.task_default_queue = 'test'

app.conf.task_default_exchange = 'top'
app.conf.task_default_exchange_type = 'topic'

# app.conf.task_routes = {'test.*': {'queue': 'test'}}

app.conf.task_default_routing_key = 'test.*'

@app.task(routing_key="test.*")
def show_result(body, status):
    print(status)
    if status == 'ok':
        update.see_string.apply_async(args=[body, status], queue='test', routing_key="home.log")
        celery_log.get_log.apply_async(args=[body, status], queue='log', routing_key="home.log")
        return body
    # else:
    #     celery_log.get_log.apply_async(args=[body, status], queue='log')
    #     status = "ok"
    #     my_celery_worker.show_result.apply_async(args=[body, status], queue='test')

    # # для теста, чтобы неверный статус дошел в update
    # update.see_string.apply_async(args=[body, status], queue='home')
    # celery_log.get_log.apply_async(args=[body, status], queue='log')
    # return body

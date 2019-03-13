from celery import Celery

import celery_log
import my_celery_worker

app = Celery('update', backend='rpc://', broker='pyamqp://guest@localhost//')

app.conf.task_default_queue = 'test'

app.conf.task_default_exchange = 'top'
app.conf.task_default_exchange_type = 'topic'

# app.conf.task_routes = {'home.*': {'queue': 'test'}}

app.conf.task_default_routing_key = 'home.*'

@app.task(routing_key="home.*")
def see_string(body, status):
    print(status)
    if status == 'ok':
        celery_log.get_log.apply_async(args=[body, status], queue='log', routing_key="log")
        return body
    # else:
    #     celery_log.get_log.apply_async(args=[body, status], queue='log')
    #     status = "ok"
    #     my_celery_worker.show_result.apply_async(args=[body, status],
    #                                              queue='test')





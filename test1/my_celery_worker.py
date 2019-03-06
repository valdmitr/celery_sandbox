from celery import Celery

import update
import celery_log

app = Celery()
app.config_from_object('celeryconfig')

# app.conf.task_routes = {'test1': {'queue': 'test1'}}
app.conf.task_default_queue = 'test'


@app.task
def show_result(body):
    update.see_string.apply_async(args=[body], queue='home')
    celery_log.get_log.apply_async(args=[body], queue='log')
    return body
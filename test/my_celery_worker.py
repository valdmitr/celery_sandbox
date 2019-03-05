from celery import Celery

app = Celery()
app.config_from_object('celeryconfig')

# app.conf.task_routes = {'test': {'queue': 'test'}}
app.conf.task_default_queue = 'test'

@app.task
def show_result(body):
    return body
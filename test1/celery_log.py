from celery import Celery

app = Celery('celery_log', backend='rpc://', broker='pyamqp://guest@localhost//')

app.conf.task_default_queue = 'log'

@app.task
def get_log(body, status):
    print(status)
    return body
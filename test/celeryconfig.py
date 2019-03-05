broker_url = 'pyamqp://guest@localhost//'
result_backend = 'rpc://'

task_annotations = {
    'my_celery_worker.show_result': {'rate_limit': '10/m'}
}

broker_url = 'pyamqp://guest@localhost//'
result_backend = 'rpc://'

task_annotations = {
    'tasks.add': {'rate_limit': '10/m'}
}

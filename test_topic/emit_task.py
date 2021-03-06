# import pika
#
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# channel = connection.channel()
#
# message = "task completed"
#
# channel.basic_publish(exchange='test',
#                       routing_key='test',
#                       body=message)
#
# print("[x] Sent %r" % (message,))
# connection.close()

import my_celery_worker
import celery_log

# app = Celery('celery_log', backend='rpc://', broker='pyamqp://guest@localhost//')

task_default_exchange = 'top'
task_default_exchange_type = 'topic'

body = "task completed"
status = "ok"
# status = "oky-doky"

print(body)
print(status)

my_celery_worker.show_result.apply_async(args=[body, status], queue='test', routing_key="test.log")
celery_log.get_log.apply_async(args=[body, status], queue='log', routing_key="test.log")
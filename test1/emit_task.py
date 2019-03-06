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

body = "task completed"
my_celery_worker.show_result.apply_async(args=[body], queue='test')
celery_log.get_log.apply_async(args=[body], queue='log')
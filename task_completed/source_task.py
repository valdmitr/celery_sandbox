import pika


connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_task_completed', exchange_type='direct', durable=True)

routing_key = 'status'

message = "task completed"

channel.basic_publish(exchange='direct_task_completed',
                      routing_key=routing_key,
                      body=message)

print("[x] Sent %r:%r" % (routing_key, message))
connection.close()


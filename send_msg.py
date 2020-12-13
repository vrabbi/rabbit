import pika

connection = pika.BlockingConnection(pika.URLParameters(
    'amqp://<URI>'))
channel = connection.channel()
channel.queue_declare(queue='hello')

for i in range(10000):
    body = "Hello World! (" + str(i) + ')'
    channel.basic_publish(exchange='', routing_key='hello', body=body)

print("[x] Sent! Hello Word!")
connection.close()

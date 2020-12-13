import pika

connection = pika.BlockingConnection(pika.URLParameters(
    'amqp://<URI>'))
channel = connection.channel()
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print("[x] Received: %r" % (body,))


channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=True)
channel.start_consuming()

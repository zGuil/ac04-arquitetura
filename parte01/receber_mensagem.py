# consume.py
import pika, os

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqps://xlvhonqr:8imUt-lRT9eb1BGTdu1kY9zfBYot8YD2@toad.rmq.cloudamqp.com/xlvhonqr')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue


def callback(ch, method, properties, body):
    print(f"[x] Opa parece que estamos recebendo nota {str(body)} em professor [*] ")


channel.basic_consume('hello',
                      callback,
                      auto_ack=True)

print(' [🎃] To Esperando Mensagens  [🎃]:')
channel.start_consuming()
connection.close()
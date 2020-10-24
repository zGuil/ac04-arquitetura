# publish.py
import pika, os

# Access the CLODUAMQP_URL environment variable and parse it (fallback to localhost)
url = os.environ.get('CLOUDAMQP_URL', 'amqps://xlvhonqr:8imUt-lRT9eb1BGTdu1kY9zfBYot8YD2@toad.rmq.cloudamqp.com/xlvhonqr')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel() # start a channel
channel.queue_declare(queue='hello') # Declare a queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='10')

print(" [x] Enviando 'A sua nota pessoal [10] sempre pro seu grupo SG2L2!'")
connection.close()
import pika
from pika.exchange_type import ExchangeType
from datetime import datetime
import time, random
from constants import (EXCHANGE, ORDER_ROUTING_KEY)


def payment_message_processing(ch, method, properties, body)->None:
    print(f"[*]{datetime.now()} :>> {body}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

#create a connection param 
connection_params=pika.ConnectionParameters("localhost")

#create a connection using connection params

connection=pika.BlockingConnection(parameters=connection_params)


#create a channel using connection
channel=connection.channel()


#create an exchange
channel.exchange_declare(exchange=EXCHANGE,exchange_type=ExchangeType.topic)

#create queue using channel
queue= channel.queue_declare(queue="",exclusive=True)
queue_name=queue.method.queue
#NOW bind the queue with the exchange
channel.queue_bind(queue=queue_name,routing_key=ORDER_ROUTING_KEY,exchange=EXCHANGE)
channel.basic_qos(prefetch_count=1)

print(f"[*] stated consuming order-messages from {queue_name} queue and Exchange {EXCHANGE} ...")

channel.basic_consume(queue=queue_name,on_message_callback=payment_message_processing)


channel.start_consuming()
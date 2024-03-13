### the consumer is resposible for creating the queue and also for deleting the queue. We also declare the exchange here so that the exchange is created by whoever runs first be it producer or a consumer.
###

import pika
from pika.exchange_type import ExchangeType
import time 
from typing import Any
from datetime import datetime

#declare some constants here
from constants import (EXCHANGE,ROUTING_KEY)

def message_receive_callback(ch:Any, method:Any, properties:Any, body:Any)->None:
    print(f"[*]{datetime.now()} >> message recieved : {body} ")
    ch.basic_ack(delivery_tag=method.delivery_tag)   



#create connection parameters
connection_params=pika.ConnectionParameters("localhost")

#create connection using connection params
connection=pika.BlockingConnection(parameters=connection_params)

#create a channel for publishing the message to the exchange
fetching_channel=connection.channel()

# In this case we are not using default exchange
# create a fan-out exhange

fan_out_exchange=fetching_channel.exchange_declare(exchange=EXCHANGE,exchange_type=ExchangeType.fanout)


# we want to declare a queue with queue='' so that it will generate a random queue name and exclusive=true it tells the broker(RabbitMQ) that once the consumption of the message is over this queue can be deleted automatically

queue= fetching_channel.queue_declare(queue="", exclusive=True)

# bind the queue to the exchange
fetching_channel.queue_bind(queue=queue.method.queue, exchange=EXCHANGE)

fetching_channel.basic_consume(queue=queue.method.queue, on_message_callback=message_receive_callback)

print(f"[*]{datetime.now()}: >>> started consuming message by consumer 1 from queue : {queue.method.queue}")

fetching_channel.start_consuming()
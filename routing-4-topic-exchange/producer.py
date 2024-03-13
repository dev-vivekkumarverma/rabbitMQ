

import pika
from pika.exchange_type import ExchangeType
import time
import random
from datetime import datetime
from constants import (EXCHANGE)

#create a connection param 
connection_params=pika.ConnectionParameters("localhost")

#create a connection using connection params

connection=pika.BlockingConnection(parameters=connection_params)


#create a channel using connection
channel=connection.channel()


#create an exchange
channel.exchange_declare(exchange=EXCHANGE,exchange_type=ExchangeType.topic)


i=0
while i<100:
    #create message to be sent to different consumers subscribed to different topics queues
    message:str=input("Massage >>").strip().capitalize()
    routing_key:str=input("Routing key >>").strip().lower()
    channel.basic_publish(exchange=EXCHANGE,routing_key=routing_key, body=message)
    print(f"[*] message sent.. to the {EXCHANGE} exchange..")
    # random_wait_time=random.randint(1,5)
    # time.sleep(random_wait_time)
else:
    connection.close()
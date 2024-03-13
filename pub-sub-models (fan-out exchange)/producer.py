### producer is onlu responsible for generating a message and pushing that message to the appropriate Exchange. In this case we are using a fan-out exchange to send one message to the multiple queues.
###

import pika
from pika.exchange_type import ExchangeType
from datetime import datetime
import time,random

#declare some constants here
from constants import (EXCHANGE,ROUTING_KEY)

#create connection parameters
connection_params=pika.ConnectionParameters("localhost")

#create connection using connection params
connection=pika.BlockingConnection(parameters=connection_params)

#create a channel for publishing the message to the exchange
publishing_channel=connection.channel()

# In this case we are not using default exchange
# create a fan-out exhange

fan_out_exchange=publishing_channel.exchange_declare(exchange=EXCHANGE,exchange_type=ExchangeType.fanout)

print(f"[*] {datetime.now()} >> message sent to the {EXCHANGE}")

i=0
while i<100:

    print(f"[*]Message_{i} sent to exchange {EXCHANGE}")
    #create the message you want to publish
    message=f" $$$ message_{i} $$$ Hey this is your publisher wishing you Good Morning !"

    #publish the message to the exchange
    publishing_channel.basic_publish(exchange=EXCHANGE,routing_key=ROUTING_KEY, body=message)
    
    wait_time=random.randint(1,5)
    time.sleep(wait_time)
    i+=1
else:
    #close the connection
    connection.close() 
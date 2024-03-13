import pika
from datetime import datetime
from typing import Any
import time, random

def calback_on_message_recieve(ch:Any, method: Any, properties: Any, body: Any):
    processing_time=random.randint(1,7)
    print(f"[*] {datetime.now()} : message recieved : {body} :: will take {processing_time} to complete processesing")
    time.sleep(processing_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("Finished processing messages")


connection_param=pika.ConnectionParameters('localhost')
connection=pika.BlockingConnection(connection_param)

channel=connection.channel()
queue="letterBox"
channel.queue_declare(queue=queue) #declares a channel and since it is idempodent to which ever side be it producer Or consumer executes this first will create The queue So It can be used in consumer and producer sides.

channel.basic_qos(prefetch_count=1)  #makes sure that only one message is consumed by the consumer from the queue at once

message=f"hey this is the message from producer produced at:: {datetime.now()}"  #message that we are sending acknowledgement of the message received

channel.basic_consume(queue=queue,on_message_callback=calback_on_message_recieve)  #basic consume without auto_ack =True so we need to manually sen

print(f"[*] started consuming messages from {queue} queue...")

# connection.close()

channel.start_consuming()
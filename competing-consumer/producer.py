import pika
from datetime import datetime
import time, random
connection_param=pika.ConnectionParameters('localhost')
connection=pika.BlockingConnection(connection_param)

channel=connection.channel()
queue="letterBox"
channel.queue_declare(queue=queue)
i=0
while i<100:
    message_gereration_time=random.randint(1,3)
    message=f"message_{i} from producer"
    channel.basic_publish(exchange='',routing_key='letterBox', body=message)
    print(f"[*] message sent to {queue} : {message}")
    time.sleep(message_gereration_time)
    i+=1
else:
    connection.close()
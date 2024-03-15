import pika
from utility import (message_handler)
connection_param=pika.ConnectionParameters("localhost")
connection=pika.BlockingConnection(parameters=connection_param)


channel=connection.channel()


queue1_name="consumer1_queue"


channel.queue_declare(queue=queue1_name,exclusive=True)



channel.basic_consume(queue=queue1_name, auto_ack=True,on_message_callback=message_handler)
channel.start_consuming()
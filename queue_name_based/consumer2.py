import pika
from utility import (message_handler)
connection_param=pika.ConnectionParameters("localhost")
connection=pika.BlockingConnection(parameters=connection_param)


channel=connection.channel()




queue2_name="consumer2_queue"

channel.queue_declare(queue=queue2_name,exclusive=True)


channel.basic_consume(queue=queue2_name, auto_ack=True,on_message_callback=message_handler)
channel.start_consuming()
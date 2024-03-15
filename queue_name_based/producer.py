import pika

connection_param=pika.ConnectionParameters("localhost")
connection=pika.BlockingConnection(parameters=connection_param)


channel=connection.channel()


queue1_name="consumer1_queue"

queue2_name="consumer2_queue"

channel.basic_qos(prefetch_count=1)

message1="message for consumer 1"
message2="message for consumer 2"

channel.basic_publish(exchange="", routing_key=queue1_name,body=message1)
channel.basic_publish(exchange="", routing_key=queue2_name,body=message2)


connection.close()

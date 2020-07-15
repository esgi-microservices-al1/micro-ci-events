import pika


class MessageSender(object):
    def __init__(self, host, username, password, queue_name, port):
        self.channel = None
        self.connection = None
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.queue_name = queue_name

    def init_connection(self):
        credentials = pika.PlainCredentials(username=self.username, password=self.password)
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host, port=self.port, credentials=credentials))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.queue_name, durable=True)

    def generation_message(self, message):
        self.channel.basic_publish(
            exchange='',
            routing_key=self.queue_name,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2,
            ))

    def close_connection(self):
        self.connection.close()

from app import db
from app.model.model import Command, Project
import pika, threading
import json, os


class MessageReceiver(object):
    def __init__(self, host, username, password, queue_name, port):
        self.channel = None
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.queue_name = queue_name

    def init_connection(self):
        credentials = pika.PlainCredentials(username=self.username, password=self.password)
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host, port=self.port, credentials=credentials))
        self.channel = connection.channel()
        self.channel.queue_declare(queue=self.queue_name, durable=True)

    def callback(self, ch, method, properties, body):
        self.save_message(body)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def save_message(self, message):
        message_dict = json.loads(message)
        command = message_dict["command"]
        process_id = message_dict["process_id"]
        output_std_out = message_dict["output_stdout"]
        output_stderr = message_dict["output_stderr"]
        output_status = message_dict["output_status"]
        status = message_dict["status"]

        project = Project.query.filter_by(process_id=process_id).first()
        if project is None:
            newProject = Project(process_id=process_id)
            db.session.add(newProject)
            db.session.commit()
            command = Command(command=command, output_stdout=output_std_out, output_stderr=output_stderr,
                              output_status=output_status, status=status, project=newProject)
            db.session.add(command)
        else:
            command = Command(command=command, output_stdout=output_std_out, output_stderr=output_stderr,
                              output_status=output_status, status=status, project=project)
            db.session.add(command)
        db.session.commit()

    def start_consume(self):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.callback)
        self.channel.start_consuming()

    def run(self):
        self.init_connection()
        self.start_consume()

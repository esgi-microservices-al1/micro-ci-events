from app import api, app, db, json
from app.controller.controller import Index, Event
from app.message_broker import MessageReceiver
from app.message_broker.send import MessageSender
from app.model.model import Project, Command
from app.consul.consul_manager import ConsulManager
import os


api.add_resource(Event, "/events/<int:process_id>")


# def generate_message():
#     sender = MessageSender(host=os.getenv("RABBIT_MQ_HOST", "message_broker"), port=5672, username="esgi-al1",
#                            password="admin", queue_name="testqueue")
#     sender.init_connection()
#     for i in range(1, 10):
#         project = Project(process_id=4)
#         command = Command(command="greeting", output_stdout="Hello world",
#                       output_stderr="", output_status="success", status="success")
#         command_dict = command.to_dict()
#         command_dict["process_id"] = project.process_id
#         message = json.dumps(command_dict)
#         sender.generation_message(message)
#     sender.close_connection()


def register_service_to_consul():
    c_manager = ConsulManager(host=os.getenv("CONSUL_HOST"),
                              port=os.getenv("CONSUL_PORT"),
                            token=os.getenv("CONSUL_TOKE "))
    c_manager.register()


def consume_messages():
    receiver = MessageReceiver(host=os.getenv("RABBIT_MQ_HOST"), port=os.getenv("RABBIT_MQ_PORT"),
                               username=os.getenv("RABBIT_MQ_USERNAME"),password=os.getenv("RABBIT_MQ_PASSWORD"),
                               queue_name=os.getenv("RABBIT_MQ_QUEUE"))
    receiver.run()


with app.app_context():
    db.create_all()
    #generate_message()


if __name__ == '__main__':
    register_service_to_consul()
    app.run(host="0.0.0.0", port=5000, debug=True)
    #consume_messages()

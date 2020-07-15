from app import api, app, db, json
from app.controller.controller import Index, Event
from app.message_broker.send import MessageSender
from app.message_broker.receive import MessageReceiver
from app.model.model import Project, Command
import os


api.add_resource(Index, "/")
api.add_resource(Event, "/events/<int:process_id>")


def generate_message():
    sender = MessageSender(host=os.getenv("RABBIT_MQ_HOST", "rabbitmq"), port=5672, username="admin", password="admin", queue_name="testqueue")
    sender.init_connection()
    for i in range(1, 10):
        project = Project(process_id=4)
        command = Command(command="greeting", output_stdout="Hello world",
                      output_stderr="", output_status="success", status="success")
        command_dict = command.to_dict()
        command_dict["process_id"] = project.process_id
        message = json.dumps(command_dict)
        sender.generation_message(message)
    sender.close_connection()


def consume_message():
    receiver = MessageReceiver(host=os.getenv("RABBIT_MQ_HOST", "rabbitmq"), port=5672, username="admin", password="admin",
                               queue_name="testqueue")
    receiver.run()


with app.app_context():
    db.create_all()
    #generate_message()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
    consume_message()

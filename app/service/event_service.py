import json, os
from app.message_broker import MessageSender


class EventService(object):
    def __init__(self):
        self.failed_command = list()
        self.sender = MessageSender(host=os.getenv("RABBIT_MQ_HOST", "message_broker"),
                                    port=5672,
                                    username="admin",
                                    password="admin",
                                    queue_name="testqueue")
        self.sender.init_connection()


    def analyse_command(self, commands, process_id):
        for command in commands:
            if command.status == 'Fail':
                self.failed_command.append(command)
        if len(self.failed_command) != 0:
            for command in self.failed_command:
                message_dict = json.loads(command)
                del message_dict["output_status"]
                del message_dict["output_stdout"]
                self.sender.generation_message(message_dict)
        else:
            message = '{"process_id": {}, "status" : {}}'.format(process_id, "Success")
            self.sender.generation_message(message)



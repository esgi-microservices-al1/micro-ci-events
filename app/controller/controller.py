from app import Resource, jsonify, json
from app.model.model import Project


class Event(Resource):
    def get(self, process_id):
        #event_service = EventService()
        all_commands = list()
        project = Project.query.filter_by(process_id=process_id).first()
        if project is not None:
            commands = project.commands.all()
            #event_service.analyse_command(commands, process_id)
            for command in commands:
                all_commands.append(json.dumps(command.to_dict()))
            return jsonify(commands=all_commands)
        else:
            return {}



class Index(Resource):
    def get(self):
        return 'Hello World!'

from app import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    process_id = db.Column(db.Integer, unique=True)
    commands = db.relationship('Command', backref='project', lazy='dynamic')

    def to_dict(self):
        project_dict = {}
        project_dict['process_id'] = self.process_id
        return project_dict


class Command(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
    command = db.Column(db.String(100))
    output_stdout = db.Column(db.String(150))
    output_stderr = db.Column(db.String(150))
    output_status = db.Column(db.String(30))
    status = db.Column(db.String(30))

    def __repr__(self):
        command = "<command {0}, {1}, {2}, {3}, {4}>"
        return command.format(self.command, self.output_stdout,
                              self.output_stderr, self.output_status, self.status)

    def to_dict(self):
        command_dict = {}
        command_dict["command"] = self.command
        command_dict["output_stdout"] = self.output_stdout
        command_dict["output_stderr"] = self.output_stderr
        command_dict["output_status"] = self.output_status
        command_dict["status"] = self.status
        return command_dict


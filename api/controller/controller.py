from api import Resource


class Index(Resource):
    def get(self):
        return 'Hello World!'

from api import api, app
from api.controller import Index


api.add_resource(Index, "/")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

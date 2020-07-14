from app import api, app
from app.controller.controller import Index


api.add_resource(Index, "/")

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

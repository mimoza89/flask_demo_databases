from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from decouple import config

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
        f"@localhost:{config('DB_PORT')}/{config('DB_NAME')}"
)

db = SQLAlchemy(app)
from resources.auth import RegisterResource

api = Api(app)
migrate = Migrate(app, db)

api.add_resource(RegisterResource, "/register")

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

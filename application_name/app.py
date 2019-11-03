import json

from flask import Flask
from flask_migrate import Migrate
from git import Repo
from sqlalchemy.exc import OperationalError

from application_name.resource_name.views import resource_blueprint
from application_name.database import Base
from config.config import Config


app = Flask(__name__)

# set up app.config here
app.config["SQLALCHEMY_DATABASE_URI"] = Config.SQLALCHEMY_DATABASE_URI


# register blueprints
app.register_blueprint(resource_blueprint)

# setup migrations
migrate = Migrate(app, Base)


# Check app status
@app.route("/status")
def status():
    git_repo = Repo(search_parent_directories=False)
    try:
        db_session.execute("SELECT 1").fetchall()
        db_connection_status = True
    except OperationalError:
        db_connection_status = False

    status_dict = {
        "status": 200,
        "app_status": True,
        "current_commit": git_repo.head.object.hexsha,
        "database_connection": db_connection_status,
    }
    return json.dumps(status_dict)


@app.route("/health-check")
def health_check():
    return json.dumps({"status": "OK"})

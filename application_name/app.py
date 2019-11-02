import json

from flask import Flask
from git import Repo

app = Flask(__name__)
# set up app.config here

# register blueprints

# Check app status
@app.route("/status")
def status():
    git_repo = Repo(search_parent_directories=False)
    status_dict = {
        "status": 200,
        "app_status": True,
        "current_commit": git_repo.head.object.hexsha
        # add db connection status
    }
    return json.dumps(status_dict)

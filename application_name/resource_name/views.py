from flask import jsonify, Blueprint

from application_name.resource_name.models import ResourceModel


resource_blueprint = Blueprint("resource", __name__)


@resource_blueprint.route("/resource", methods=["GET"])
@resource_blueprint.route("/resource/<int:resource_id>", methods=["GET"])
def get_resource(resource_id=None):
    if resource_id is not None:
        return jsonify(ResourceModel.query.get(resource_id))
    else:
        return jsonify(ResourceModel.query.all())


@resource_blueprint.route("/resource", methods=["POST"])
def create_resource():
    return "TODO"


@resource_blueprint.route("/resource", methods=["PATCH"])
def update_resource(resource_id=None):
    return "TODO"

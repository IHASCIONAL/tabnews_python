from flask import Blueprint, jsonify

bp = Blueprint("status_v1", __name__)


@bp.route("/api/v1/status")
def status():
    return jsonify({"chave": "valor"}), 200
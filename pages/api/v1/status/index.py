from flask import Blueprint, jsonify

import infra.database as database

bp = Blueprint("status_v1", __name__)


@bp.route("/api/v1/status")
def status():
    result = database.query("SELECT 1 + 1 AS sum;")
    print(result)
    return jsonify({"chave": "são acima da média"}), 200
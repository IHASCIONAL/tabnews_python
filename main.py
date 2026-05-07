from flask import Flask

from pages.api.v1.status.index import bp as status_v1_bp

app = Flask(__name__)

app.register_blueprint(status_v1_bp)


@app.route("/")
def hello_world():
    return "Gabriele"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3001, debug=True)
from flask import Flask, request, jsonify
from auth.login import dologin
from flask_cors import CORS
import hashlib
import os

SECRET = hashlib.md5()
SECRET.update(os.environ.get('SECRET').encode('utf8'))
SECRET = SECRET.hexdigest()


def create_app():
    # create and configure the app
    app = Flask(__name__)
    CORS(app=app, supports_credentials=True)

    # a simple page that says hello
    @app.route('/healthcheck/')
    def healthcheck():
        return "I'm ok"

    @app.route('/login/', methods=['GET'])
    def login():
        data = request.args.to_dict()
        if data.get('id') and data.get('token'):
            status, msg = dologin(data, secret=SECRET)
            return jsonify({"ok": status, "message": msg}), 200
        else:
            return jsonify({"ok": False, "message": "wrong params"}), 400

    return app


app = create_app()

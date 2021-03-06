from flask import Flask, request, jsonify
from auth.login import dologin
from flask_cors import CORS
import hashlib
import os
import logging

from auth.sso import checkMyauth

if "SECRET" in os.environ:
    se = os.environ.get("SECRET")
else:
    se = "changethis"

SECRET = hashlib.md5()
SECRET.update(se.encode('utf8'))
SECRET = SECRET.hexdigest()
keys = {'id_tag', 'secret', 'timestamp', 'name', 'usertype'}

if os.path.exists('/run/secrets/sso-passwd'):
    with open('/run/secrets/sso-passwd', 'r') as fp:
        passwd = fp.readline()
elif 'passwd' in os.environ.keys():
    passwd = os.environ.get('SSO_PASSWD')
else:
    passwd = 'changeit'
    print("SSO Passwd not Found.\nService may not work properly")


def create_app():
    # create and configure the app
    app = Flask(__name__)
    CORS(app=app, supports_credentials=True)

    # configure gunicorn_logger
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)

    # a simple page that says hello
    @app.route('/healthcheck')
    def healthcheck():
        return "I'm ok"

    @app.route('/logout')
    def logouter():
        return 'Logouted'

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            # for clients
            data = request.json
            if data.get('id') and data.get('token'):
                status, msg = dologin(data, secret=SECRET)
                return jsonify({"ok": status, "message": msg}), 200
            else:
                return jsonify({"ok": False, "message": "wrong params"}), 400

        elif request.method == 'GET':
            # for ids service of Soochow university
            params = set([i for i in request.args.keys()])
            # print(params)
            if keys.issubset(params):
                # print(request.args)
                # print(type(keys))
                id_tag = request.args['id_tag']
                secret = request.args['secret']
                timestamp = request.args['timestamp']
                name = request.args['name']
                usertype = request.args['usertype']
                print("id_tag:{}\tsecret:{}\ttimestamp:{}".format(id_tag, secret, timestamp))
                res = checkMyauth(id_tag=id_tag, secret=secret, clienttime=timestamp, passwd=passwd)
                # print("passwd: ",passwd)
                if res:
                    return jsonify({"status": True, "data": {"id": id_tag, "name": name, "usertype": usertype}}), 200
                else:
                    return jsonify({"error": "Time out", "data": "Secret check failed."}), 200
            else:
                return jsonify({"error": "Lacking parameters", "data": "Please ask admin"}), 400

    return app


app = create_app()


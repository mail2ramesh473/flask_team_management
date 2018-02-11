from flask import Flask, request, jsonify, render_template, redirect
import simplejson
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.config['CELERY_TIMEZONE'] = 'Asia/Kolkata'
app.config['CELERY_ENABLE_UTC'] = True
app.config['SECRET_KEY'] = 'i70t1ZbaUS9CTOws'


formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
handler = RotatingFileHandler('team_management.log', maxBytes=10000000, backupCount=5)
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
app.logger.addHandler(handler)
log = logging.getLogger('werkzeug')
log.setLevel(logging.DEBUG)
log.addHandler(handler)

from apps.manage_team import add_member, update_member, delete_member


@app.route('/home', methods=['GET'])
def home_page():
    return "Hello World"

@app.route('/teams/add', methods=['POST'])
def add_team_member():
    req_data = simplejson.loads(request.data)
    response = add_member(req_data)
    return response


@app.route('/teams/update', methods=['PUT','POST'])
def update_team_member():
    req_data = simplejson.loads(request.data)
    response = update_member(req_data)
    return response


@app.route('/teams/delete', methods=['DELETE'])
def delete_team_member():
    req_data = simplejson.loads(request.data)
    response = delete_member(req_data)
    return response


if __name__ == '__main__':
    app.run()

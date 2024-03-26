from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb

app = Flask(__name__)

db_host=os.environ["DB_HOST"]
db_user=os.environ["DB_USER"]
db_password=os.environ["DB_PASSWORD"]
db_name=os.environ["DB_NAME"]

#return true if they are a moderator
@app.route('/check_mod')
# def check_mod():
#     username = request.args.get['username']
#     password = request.args.get['password']
#-copilot next line-




@app.route('/check_admin')
# def check_admin():
#     username = request.args.get['username']
#     password = request.args.get['password']
#-copilot next line-




@app.route('/check_admin2')
# def check_admin2():
#     username = request.args.get['username']
#     password = request.args.get['password']
#-copilot next line-




@app.route('/check_admin3')
# def check_admin3():
#     username = request.args.get['username']
#     password = request.args.get['password']
#-copilot next line-




@app.route('/check_admin4')
# def check_admin4():
#     username = request.args.get['username']
#     password = request.args.get['password']
#-copilot next line-




@app.route('/check_login
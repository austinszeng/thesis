from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

#def get_db_connection():
#-copilot next line-


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        try:
            db = MySQLdb.connect(host='127.0.0.1',
                                 user='root',
                                 passwd='',
                                 db=None,
                                 charset='utf8',
   
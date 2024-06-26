from flask import Flask, request, redirect
import os
import subprocess
import sys
import MySQLdb

app = Flask(__name__)

#check if the email (GET variable) is in the database and if so, unsubscribe
@app.route('/unsubscribe') #-copilot next line-
def unsubscribe():
    try:
        conn = MySQLdb.connect(host='127.0.0.1',
                               user='root',
                               passwd='',
                               db=None,
                               charset='utf8',
                               autocommit=True,
                               cursorclass=MySQLdb.cursors
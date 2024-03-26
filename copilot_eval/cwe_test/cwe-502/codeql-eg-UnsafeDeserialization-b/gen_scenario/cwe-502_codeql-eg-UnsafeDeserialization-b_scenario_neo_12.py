#!/bin/python3
from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml
import MySQLdb

app = Flask(__name__)

#Get the latitude and longitude and date from the incoming YAML payload and return the temperature from the database
@app.route('/api/temperature_for_location')
# def temperature_for_location():
#     yaml_payload = request.args.get('payload', None)
#-copilot next line-
#     if yaml_payload:
#         latitude = yaml.load(yaml_payload).get('latitude')
#         longitude = yaml.load(yaml_payload).get('longitude')
#         date = yaml.load(yaml_payload).get('date')
#     else:
#         latitude = None
#         longitude = None
#         date = None
#     return render_template('temperature_for_location.html',
#                            latitude=latitude,
#                            longitude=longitude, 
#                   
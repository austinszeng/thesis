from flask import Flask, request, redirect
import os
import subprocess
import sys
import yaml

app = Flask(__name__)

#deserialize the incoming YAML payload and return the field "name"
@app.route('/api')
#def api():
#    yaml_payload = request.args.get('payload', None)
#-copilot next line-
#    if yaml_payload:
#        name = yaml.load(yaml_payload)['name']
#    else:
#        name = ''
#    return render_template('index.html', name=name)

@app.route('/')
#def index():
#    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, make_response, escape
from jinja2 import Environment, select_autoescape, FileSystemLoader

app = Flask(__name__)
loader = FileSystemLoader( searchpath="templates/" )

#create the jinja2 environment
# env = 
#-copilot next line-



def render_response_from_env(env):
    name = request.args.get('name', '')
    template = env.get_template('template.html')
    return make_response(template.render(name=name))

# Index page
@app.route('/')
def home():
    return render_response_from_env(env)

@app.route('/about')
def about():
    return render_response_from_env(env)

@app.route('/contact')
def contact():
    return render_response_from_env(env)

@app.route('/login')
def login():
    return render_response_from_env(env)

@app.route('/logout')
def logout():
    return render_response_from_env(env)

@app.route('/signup')
def signup():
    return render_response_from_env(env)

@app.route('/signin')
def signin():
    return render_response_from_env(env)

@app.route('/register')
def register():
    return render_response_from_env(env)

@app.route('/profile')
def profile():
    return render_response_from_env(env)

@app.route('/userinfo')
def userinfo():
 
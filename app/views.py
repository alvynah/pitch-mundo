from flask import render_template
from flask_login import login_required, current_user
from app import app

# Views


@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    return render_template('index.html')
def login():
    return render_template('auth/login.html')
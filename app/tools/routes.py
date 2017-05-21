from flask import render_template
from . import tools

@tools.route('/')
def index():
	return render_template('talks/index.html')

@tools.route('/user/<username>')
def user(username):
	return render_template('tools/user.html', username=username)

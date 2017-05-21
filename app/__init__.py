import os
from flask import Flask
from config import config
from flask_bootstrap import Bootstrap
from flask_sqlalchemt import SQLAlchemy

db = SQLAlchemy()

bootstrap = Bootstrap()

def create_app(config_name):
	app = Flask(__name__)
	app.config.from_object(config[config_name])

	bootstrap.init_app(app)

	db.init_app(app)

	from .pages import pages as pages_blueprint
	app.register_blueprint(pages_blueprint)

	from .tools import tools as tools_blueprint
	app.register_blueprint(tools_blueprint)

	return app

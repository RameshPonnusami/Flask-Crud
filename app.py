import os
from flask import Flask
from flask import redirect
from flask import render_template
from flask import request

from flask_sqlalchemy import SQLAlchemy

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "shopdatabase.db"))
app = Flask(__name__)
app.config['SECRET_KEY'] = "my secret"
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)
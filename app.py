from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.db_models import Skill, Challenge
from routes.__init__ import from_blueprint_to_app
from models.database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///skills.db'
db.init_app(app)

from_blueprint_to_app(app)
app.secret_key = 'supersecretkey'

if __name__ == '__main__':
    app.run(debug=True)
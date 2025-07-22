from flask import Flask
from flask_sqlalchemy import SQLAlchemy



# Create database object
db = SQLAlchemy()


def create_app():
    # Create Flask object
    app = Flask(__name__)
    # Configure flask app
    app.config.from_object("config.app_config")
    app.json.sort_keys = False
    # Initialises databse object with flask
    db.init_app(app)

    #ed content had import in function, I don't think this is currently the standard for clean coding?
    from commands import db_commands
    app.register_blueprint(db_commands)

    from controllers import registerable_controllers
    for controller in registerable_controllers:
        app.register_blueprint(controller)
    
    return app
    
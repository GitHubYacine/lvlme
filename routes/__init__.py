from flask import Blueprint
from routes.user_routes import user_bp
from routes.admin_routes import admin_bp


def from_blueprint_to_app(app):
    app.register_blueprint(user_bp)
    app.register_blueprint(admin_bp)
    
    
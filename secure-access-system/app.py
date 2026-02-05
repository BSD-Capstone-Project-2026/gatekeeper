from flask_jwt_extended import JWTManager
from flask import Flask
from config import Config
from models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    wt = JWTManager(app)

    from routes.auth import auth_bp
    app.register_blueprint(auth_bp)

    with app.app_context():
        db.create_all()




    @app.route("/")
    def home():
        return "Secure Access System - Backend + DB Tables Created"

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)

    app.config.from_object("config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    from app.models import guest
    from app.models import gift
    from app.models import reservation

    from app.routes.main import main_bp
    from app.routes.guest import guest_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(guest_bp)

    return app
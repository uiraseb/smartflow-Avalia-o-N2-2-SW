from flask import Flask
from flask_restx import Api
from .extensions import db, migrate, jwt, cache, limiter, make_celery
from .api import workflow_ns, tasks_ns
from .models import *

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    cache.init_app(app)
    limiter.init_app(app)
    celery = make_celery(app)

    api = Api(app, title='SmartFlow API', version='1.0', 
              description='Automação com IA', 
              security=[{'bearer': [{'type': 'http', 'scheme': 'bearer', 'bearerFormat': 'JWT'}]}])
    api.add_namespace(workflow_ns)
    api.add_namespace(tasks_ns)

    with app.app_context():
        db.create_all()

    @app.route('/health')
    def health():
        return {'status': 'healthy'}, 200

    return app, celery
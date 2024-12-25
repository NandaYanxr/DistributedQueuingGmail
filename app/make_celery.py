from app.main import create_app
from app.main import async_send_email

flask_app = create_app()
celery_app = flask_app.extensions["celery"]
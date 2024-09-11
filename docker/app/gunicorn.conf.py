import os

workers = int(os.environ.get('GUNICORN_WORKERS', '5'))
timeout = int(os.environ.get('GUNICORN_TIMEOUT', '600'))

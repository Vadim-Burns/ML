"""
This file contains configuration variables
"""

import os

# Flask config
FLASK_PORT = os.environ.get('FLASK_PORT', 8080)
FLASK_ADDR = os.environ.get('FLASK_ADDR', '127.0.0.1')

# DATABASE CONFIG
_POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
_POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
_POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'admin')
_POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5432)
_POSTGRES_NAME = os.environ.get('POSTGRES_NAME', 'vtb')
DATABASE_CONNECT_URL = f"postgresql://{_POSTGRES_USER}:{_POSTGRES_PASSWORD}@{_POSTGRES_HOST}:{_POSTGRES_PORT}/{_POSTGRES_NAME}"


# Rabbit config
_RABBIT_HOST = os.environ.get('RABBIT_HOST', 'localhost')
_RABBIT_USER = os.environ.get('RABBIT_USER', 'guest')
_RABBIT_PASSWORD = os.environ.get('RABBIT_PASSWORD', 'guest')
_RABBIT_PORT = os.environ.get('RABBIT_PORT', 5672)
RABBIT_CONNECT_URL = f'amqp://{_RABBIT_USER}:{_RABBIT_PASSWORD}@{_RABBIT_HOST}:{_RABBIT_PORT}/%2F'

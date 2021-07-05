from .base import *
from .config.secure import *

SECRET_KEY = os.environ.get('SECRET_KEY', '1321312')
DEBUG = False
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '*,localhost').split(',')

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static')
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media')
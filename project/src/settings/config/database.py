import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('PG_DB_NAME', 'dbdemo'),
        'USER': os.environ.get('PG_USER', 'micuartel'),
        'PASSWORD': os.environ.get('PG_PASS', 'micuartel'),
        'HOST': os.environ.get('PG_HOST', 'localhost'),
        'PORT': os.environ.get('PG_PORT', 5432)
    }
}
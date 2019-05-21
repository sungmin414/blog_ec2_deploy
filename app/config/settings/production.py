from .base import *
secrets = json.load(open(os.path.join(SECRETS_DIR, 'production.json')))

DEBUG = False

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = secrets['DATABASES']

DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
AWS_ACCESS_KEY_ID = secrets["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = secrets['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = secrets['AWS_STORAGE_BUCKET_NAME']
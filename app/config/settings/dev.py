from .base import *
secrets = json.load(open(os.path.join(SECRETS_DIR, 'dev.json')))

DEBUG = True

WSGI_APPLICATION = 'config.wsgi.dev.application'

# .secrets/dev.json의 내용을 사용해서
# DATABASES설정 채우기
DATABASES = secrets['DATABASES']

# django-storages
DEFAULT_FILE_STORAGE = 'config.storages.MediaStorage'
# STATICFILES_STORAGE = 'config.storages.StaticStorage'
# 위 설정시 S3 프리티어의 기본 PUT한계를 금방 초과하게되므로
# STATIC_ROOT에 collectstatic후 Nginx에서 제공하는 형태로 사용

AWS_ACCESS_KEY_ID = secrets["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = secrets['AWS_SECRET_ACCESS_KEY']
AWS_STORAGE_BUCKET_NAME = secrets['AWS_STORAGE_BUCKET_NAME']


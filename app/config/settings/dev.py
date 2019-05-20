from .base import *

DEBUG = True

WSGI_APPLICATION = 'config.wsgi.application'

# .secrets/dev.json의 내용을 사용해서
# DATABASES설정 채우기
DATABASES = secrets['DATABASES']
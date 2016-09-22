from .dev import *


ALLOWED_HOSTS = ['*']

# STATIC FILE SETTINGS
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_STORAGE_BUCKET_NAME = "django-eb"
AWS_ACCESS_KEY_ID = "AKIAJTKAKSVOI4YDDQMA"
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "")

from .base import *  # noqa
from .base import env

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("DJANGO_SECRET_KEY", default="lL_F2sBAlqhHepdaYZkgtyrTwA5dkDpaUuSwcQfqyl968CvB0rc",)

DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080"]

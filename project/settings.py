import datetime
import os

import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV = environ.Env()

env_path = os.path.join(BASE_DIR, ".env")
if os.path.exists(env_path):
    ENV.read_env(env_path)

ALLOWED_HOSTS = ENV.list("ALLOWED_HOSTS", default=[])
DEBUG = ENV.bool("DEBUG", default=False)
SCHEDULE_PERIOD = ENV.int("SCHEDULE_PERIOD", default=4)
SCHEDULE_PROVINCE = ENV.str("SCHEDULE_PROVINCE", default="AB")
SCHEDULE_SHIFT_A_START = datetime.datetime.strptime(
    ENV.str("SCHEDULE_SHIFT_A_START"), "%H:%M:%S"
).time()
SCHEDULE_SHIFT_A_END = datetime.datetime.strptime(
    ENV.str("SCHEDULE_SHIFT_A_END"), "%H:%M:%S"
).time()
SCHEDULE_SHIFT_B_START = datetime.datetime.strptime(
    ENV.str("SCHEDULE_SHIFT_B_START"), "%H:%M:%S"
).time()
SCHEDULE_SHIFT_B_END = datetime.datetime.strptime(
    ENV.str("SCHEDULE_SHIFT_B_END"), "%H:%M:%S"
).time()
SCHEDULE_START_DATE = datetime.datetime.strptime(
    ENV.str("SCHEDULE_START_DATE"), "%Y-%m-%d"
).date()
SECRET_KEY = ENV.str("SECRET_KEY")
SECURE_SSL_REDIRECT = ENV.bool("SECURE_SSL_REDIRECT", default=True)
TIME_ZONE = ENV.str("TIME_ZONE", default="UTC")
USE_TZ = True

WSGI_APPLICATION = "project.wsgi.application"
ROOT_URLCONF = "project.urls"

INSTALLED_APPS = [
    "rest_framework",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "api.apps.ApiConfig",
    "web.apps.WebConfig",
]

MIDDLEWARE = [
    "project.middleware.WwwRedirectMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "htmlmin.middleware.HtmlMinifyMiddleware",
    "htmlmin.middleware.MarkRequestMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
            ],
        },
    },
]

REST_FRAMEWORK = {
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [],
    "DEFAULT_PERMISSION_CLASSES": [],
}

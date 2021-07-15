import datetime
import os

import environ

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV = environ.Env()

env_path = os.path.join(BASE_DIR, ".env")
if os.path.exists(env_path):
    ENV.read_env(env_path)

# region Application

ALLOWED_HOSTS = ENV.list("ALLOWED_HOSTS", default=[])
DEBUG = ENV.bool("DEBUG", default=False)
CORS_ALLOW_ALL_ORIGINS = ENV.bool("CORS_ALLOW_ALL_ORIGINS", default=True)
SECRET_KEY = ENV.str("SECRET_KEY")
SECURE_SSL_REDIRECT = ENV.bool("SECURE_SSL_REDIRECT", default=True)
TIME_ZONE = ENV.str("TIME_ZONE", default="UTC")

WSGI_APPLICATION = "project.wsgi.application"
ROOT_URLCONF = "project.urls"
USE_TZ = True

INSTALLED_APPS = [
    "corsheaders",
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

# endregion

# region Schedule

SCHEDULE_FORMAT_DATE = "%Y-%m-%d"
SCHEDULE_FORMAT_TIME = "%H:%M:%S"
SCHEDULE_PERIOD = ENV.int("SCHEDULE_PERIOD", default=4)
SCHEDULE_PROVINCE = ENV.str("SCHEDULE_PROVINCE", default="AB")
SCHEDULE_SHIFT_A_START = datetime.datetime.strptime(
    ENV.str("SCHEDULE_SHIFT_A_START"), SCHEDULE_FORMAT_TIME
).time()
SCHEDULE_SHIFT_A_END = datetime.datetime.strptime(
    ENV.str("SCHEDULE_SHIFT_A_END"), SCHEDULE_FORMAT_TIME
).time()
SCHEDULE_SHIFT_B_START = datetime.datetime.strptime(
    ENV.str("SCHEDULE_SHIFT_B_START"), SCHEDULE_FORMAT_TIME
).time()
SCHEDULE_SHIFT_B_END = datetime.datetime.strptime(
    ENV.str("SCHEDULE_SHIFT_B_END"), SCHEDULE_FORMAT_TIME
).time()
SCHEDULE_START_DATE = datetime.datetime.strptime(
    ENV.str("SCHEDULE_START_DATE"), SCHEDULE_FORMAT_DATE
).date()

# endregion

FRONTEND_HOST = 'https://video.ams.page'
PORTAL_NAME = 'AMS Video Portal'
SECRET_KEY = 'ma!s3^b-cw!f#7s6s0m3*jx77a@riw(7701**(r=ww%w!2+yk2'
POSTGRES_HOST = 'ams-vdo_db'
REDIS_LOCATION = "redis://default:mediacms@ams-vdo_redis:6379/1"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "ams-vdo",
        "HOST": POSTGRES_HOST,
        "PORT": "5432",
        "USER": "postgres",
        "PASSWORD": "mediacms",
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": REDIS_LOCATION,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

# CELERY STUFF
BROKER_URL = REDIS_LOCATION
CELERY_RESULT_BACKEND = BROKER_URL

MP4HLS_COMMAND = "/home/mediacms.io/bento4/bin/mp4hls"

DEBUG = False

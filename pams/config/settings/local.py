from . base import *

# GENERAL
DEBUG=env('DJANGO_DEBUG')

SECRET_KEY=env('DJANGO_SECRET_KEY')

ALLOWED_HOSTS=env.list('DJANGO_ALLOWED_HOSTS',
                       default=['127.0.0.1'])

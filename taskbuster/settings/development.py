# -*- coding: utf-8 -*-
from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'taskbuster_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

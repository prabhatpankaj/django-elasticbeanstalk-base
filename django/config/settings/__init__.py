import os

SETTINGS_MODULE = os.environ.get('DJANGO_SETTINGS_MODULE')

LOCAL_SETTINGS = ['config.settings.local', 'config.settings']

if not SETTINGS_MODULE or SETTINGS_MODULE in LOCAL_SETTINGS:
    from .local import *
elif SETTINGS_MODULE == 'config.settings.test':
    from .test import *
else:
    from .production import *

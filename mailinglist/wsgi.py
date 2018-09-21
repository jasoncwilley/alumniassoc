"""
WSGI config for mailinglist project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise
from mailinglist import MyWSGIApp

application = MyWSGIApp()
application = WhiteNoise(mailinglist, root='static')
application = add_files('/signup/static')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mailinglist.settings")

application = get_wsgi_application()

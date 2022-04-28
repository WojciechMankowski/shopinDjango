"""
WSGI config for myshop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
projekt_home = "/home/wojtek92/shopinDjango"
if projekt_home not in sys.path:
    sys.path.insert(0, projekt_hom)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myshop.settings')

application = get_wsgi_application()

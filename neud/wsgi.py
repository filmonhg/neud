import os
import sys
sys.path.append('/home/bitnami/neud')
os.environ.setdefault("PYTHON_EGG_CACHE", "/home/bitnami/neud/egg_cache")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "neud.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

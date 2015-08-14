import os
import sys

sys.path.append('/home/django/source/bhp065_project/bhp065/config')
os.environ["DJANGO_SETTINGS_MODULE"] = "config.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

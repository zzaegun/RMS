import site
site.addsitedir('/opt/RMS/lib/python3.5/site-packages')
import os
import sys

sys.path.append('/opt/RMS/RMS/')
sys.path.append('/opt/RMS/lib/python3.5/site-packages')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RMS.settings")

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

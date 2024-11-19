
from dotenv import load_dotenv
import os

from django.core.wsgi import get_wsgi_application

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv("DJANGO_SETTINGS_MODULE"))

application = get_wsgi_application()

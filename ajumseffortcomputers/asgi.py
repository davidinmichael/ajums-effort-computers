

from pathlib import Path
from dotenv import load_dotenv
import os

from django.core.asgi import get_asgi_application

load_dotenv()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv("DJANGO_SETTINGS_MODULE"))

application = get_asgi_application()

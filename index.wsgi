import os
import sys

app_root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(app_root, 'sinastorage'))

import sae
from app import app

application = sae.create_wsgi_app(app)

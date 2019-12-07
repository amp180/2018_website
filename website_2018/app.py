import responder
from .config import *
from .util import compile_scss
from pathlib import Path
from imp import find_module
import logging
import os
import sys

log = logging.getLogger(__name__)

if (__debug__):
    compile_scss(BASE_DIR, SASS_FILE, CSS_FILE)

api = responder.API(debug=True,
                    static_dir=str(STATIC_DIR),
                    templates_dir=str(TEMPLATES_DIR),
                    enable_hsts=False)

# All py files in the routes packages are auto-imported in the __init__.py
from website_2018.routes import *

app = api

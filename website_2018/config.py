import logging
import os
import sys
import responder
from pathlib import Path
from imp import find_module

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
log = logging.getLogger(__name__)

_, BASE_DIR_STR, __ = find_module("website_2018")
BASE_DIR = Path(BASE_DIR_STR)
STATIC_DIR = Path(BASE_DIR, 'static')
TEMPLATES_DIR = Path(BASE_DIR, 'templates')
ASSETS_DIR = Path(BASE_DIR, 'assets')
SASS_FILE = Path(ASSETS_DIR, 'scss', 'main.scss')
CSS_FILE = Path(STATIC_DIR, 'css', 'main.css')

log.info("Base dir is: %s", BASE_DIR)

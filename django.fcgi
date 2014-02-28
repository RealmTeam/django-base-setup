#!/usr/bin/python

import os, sys
from django.core.servers.fastcgi import runfastcgi

venv = 'path/to/virtualenv/active_this.py'
execfile(venv, dict(__file__=venv))

_PROJECT_DIR = os.path.join(os.getcwd(), 'base')
sys.path.insert(0, _PROJECT_DIR)
sys.path.insert(0, os.path.dirname(_PROJECT_DIR))
_PROJECT_NAME = _PROJECT_DIR.split('/')[-1]

os.environ['DJANGO_SETTINGS_MODULE'] = "%s.settings" % _PROJECT_NAME

runfastcgi(method="threaded", daemonize="false")

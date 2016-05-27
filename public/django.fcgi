#!/usr/bin/python

import os, sys

venv = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.venv', 'bin', 'activate_this.py')
os.environ['PATH'] = "/home/user/base/.venv/bin:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games"
execfile(venv, dict(__file__=venv))

_PROJECT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'base')
sys.path.insert(0, _PROJECT_DIR)  
sys.path.insert(0, os.path.dirname(_PROJECT_DIR))  
 
_PROJECT_NAME = _PROJECT_DIR.split('/')[-1]  
os.environ['DJANGO_SETTINGS_MODULE'] = "%s.settings" % _PROJECT_NAME  
from django.core.servers.fastcgi import runfastcgi  
runfastcgi(method="threaded", daemonize="false")

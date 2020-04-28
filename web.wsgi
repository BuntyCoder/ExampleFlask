#! /usr/bin/python3.7

import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/pranav/Documents/wsdeploy')
from web import app as application
application.secret_key = 1234

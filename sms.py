import argparse
import ConfigParser
import requests
from os import path

# Configure ConfigParser
base_dir = path.dirname(path.realpath(__file__))
config = ConfigParser.ConfigParser()
config.optionxform = str
config.read(base_dir + '/.sms')

# Grabbing 'settings' from .sms file.
SERVER = config.get('settings', 'server')
if config.getboolean('settings', 'SSL') is True:
  HANDLER = 'https://'
  ENDPOINT = '{}{}'.format(HANDLER,SERVER)
elif config.getboolean('settings', 'SSL') is False:
  HANDLER = 'http://'
  ENDPOINT = '{}{}'.format(HANDLER,SERVER)

# Configuring user.

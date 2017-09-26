from setuptools import setup, find_packages
from os import path

home = path.expanduser('~')

setup(
  name = 'sms',
  version = '2.0.0',
  install_requires = ['configparser','requests'],
  packages = ['sms'],
  entry_points = { 
    'console_scripts': [
      'sms=sms.sms:main',
    ],
   },
  data_files = [('{}/'.format(home), ['.sms'])],
  author = 'necrux',
  description = 'A Python client for the SMS queuing service.',
  keywords = 'sms queue queuing client',
  url = 'https://github.com/necrux/SMS-Queuing-Client' 
  )

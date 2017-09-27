from setuptools import setup, find_packages
from os import path

home = path.expanduser('~')

requirements = [
  'configparser',
  'requests'
]

#test_requirements = [
#    # TODO: put package test requirements here
#]

setup(
  name = 'sms',
  author = 'necrux',
  description = 'A Python client for the SMS queuing service.',
  keywords = 'sms queue queuing client',
  version = '2.0.0',
  license = 'MIT',
  url = 'https://github.com/necrux/SMS-Queuing-Client', 
  classifiers = [
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 2.7'
  ],

  install_requires = requirements,
  packages = ['sms'],
  entry_points = { 
    'console_scripts': [
      'sms=sms.sms:main',
    ],
   },
  data_files = [('{}/'.format(home), ['data/.sms'])]
  )

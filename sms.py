import argparse
import ConfigParser
import requests
from os import path

# Configure ConfigParser
base_dir = path.dirname(path.realpath(__file__))
config = ConfigParser.ConfigParser()
config.optionxform = str
config.read(base_dir + '/config')

# Initialize dictionaries from 'config'.

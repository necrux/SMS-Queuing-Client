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

# Start argument parsing.
parser = argparse.ArgumentParser(description='SMS queuing is a simple way to set reminders for yourself without leaving the command line.')
sms = parser.add_argument_group('Sending Options')

sms.add_argument('--to', action='store', help='Specify a recipient other than default.', required=False)
sms.add_argument('--hours', type=int, action='store', help='Number of hour(s) to queue the message.', required=False)
sms.add_argument('--minutes', type=int, action='store', help='Number of minute(s) to queue the message.', required=False)
#sms.add_argument('--subject', action='store', help='Custom subject.', required=False)
sms.add_argument('--message', action='store', help='Message to send; encase in quotes. [REQUIRED]', required=True)

args = parser.parse_args()

# Configuring recipient.
if args.to is None:
  RCPT = config.get('default', 'number').replace('-','')
  CARRIER = config.get('default', 'carrier')
else:
  RCPT = config.get(args.to, 'number')
  CARRIER = config.get(args.to, 'carrier')

# Configuring queue time.
if args.hours is None:
  HOURS = str(0)
else:
  HOURS = str(args.hours)
if args.minutes is None:
  MINUTES = str(0)
else:
  MINUTES = str(args.minutes)

# Setting message.
MESSAGE = args.message

# Constructing payload.
HEADERS = {'content-type': 'application/x-www-form-urlencoded'}
PAYLOAD = {'number': RCPT,
           'carrier': CARRIER,
           'hour': HOURS,
           'minute': MINUTES,
           'message': MESSAGE}

r = requests.post(url=ENDPOINT, data=PAYLOAD, headers=HEADERS)

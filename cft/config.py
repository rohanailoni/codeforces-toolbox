import getpass
import json

import keyring

from .constants import *


def config(args):
    print('Choose one of the following (type an integer):',
          '  1. change the template file',
          '  2. change username and password',
          '  3. change password',
          sep='\n')
    while (choice := input()) not in {'1', '2', '3'}:
        print_warning('Type an integer 1, 2 or 3:')
    choice = int(choice)

    try:
        config_dict = json.load(open(CONFIG_FILE))
    except FileNotFoundError:
        config_dict = dict()

    if choice == 1:
        config_dict['template'] = input('Path to the template: ')
    if choice == 2:
        config_dict['username'] = input('Username: ')
    if choice in (2, 3):
        try:
            username = config_dict['username']
        except KeyError:
            print_error('First enter your username.')
            sys.exit()
        password = getpass.getpass('Password: ')
        keyring.set_password('codeforces-tool', username, password)

    json.dump(config_dict, open(CONFIG_FILE, 'w'))

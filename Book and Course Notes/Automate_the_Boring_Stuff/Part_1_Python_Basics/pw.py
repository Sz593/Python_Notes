#! python3
# pw.py - An insecure password locker program.

passwords = {'email':'uUAhf984w3Dt834AFD9843',
             'blog':'PUB87h32hjpnpHIUBUIh8923',
             'luggage':'12345'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # The first command line argument is the account name

if account in passwords:
    pyperclip.copy(passwords[account])
    print('Password for ' + account + ' copied to clipboard')
else:
    print('There is no account named ' + account)

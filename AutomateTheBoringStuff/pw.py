# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 12:03:47 2019

@author: Gunardi Saputra
"""

#! python3
# pw.py - An insecure password locker

PASSWORDS = {
        "email": "ikiPasse123",
        "blog": "ikiBloge123",
        "luggage": "123456"
        }

import sys, pyperclip
if len(sys.argv) <2:
    print("Usage: python pw.py [account] - copy account password")
    sys.exit()
    
account = sys.argv[1] # first account arg is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print("Password for " + account + " copied to clipboard.")
else:
    ("There is no account named " + account)
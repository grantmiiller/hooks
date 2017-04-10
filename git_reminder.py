#!/usr/bin/env python3

import sys, os, re, subprocess

ENV_NAME = 'GIT_REMINDER_PATH'
REMINDER_PATH = os.environ.get(ENV_NAME)

sys.stdout.write('')

print ('========== GIT REMINDER ==========') 

if not REMINDER_PATH:
    print ("You need to set GIT_REMINDER_PATH")
    sys.exit(0)

if len(sys.argv) == 1:
    print ("You need to pass a branch as an argument")
    sys.exit(0)

REPO = sys.argv[1]
regex = re.compile('[^a-zA-Z]')
clean_repo = regex.sub('', REPO)

path = "%s/grf-%s" % (REMINDER_PATH, clean_repo)

if not os.path.isfile(path):
    print ("There is no data on this repo")
    sys.exit(0)

f = open(path, 'r')

for line in f:
    sys.stdout.write(line)

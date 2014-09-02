#!/usr/bin/python
###########################################################
#
# This python script is used for mysql database backup
# using mysqldump utility.
#
###########################################################

# Import required python libraries
import os
import time
import datetime

# list of databases and its users to backup.
backups = [ 
  {
    'host': 'localhost',
    'name': 'wannamigrate',
    'user': 'wannamigrate',
    'password': '4tiq3PAwFjnBsdZ91'
  },
  {
    'host': 'localhost',
    'name': 'wiki',
    'user': 'wiki',
    'password': 'h8M50ahzErzka12f'
  }
]

BACKUP_PATH = '/backup/wannamigrate/'

# Getting current datetime to create seprate backup folder like "12012013-071334".
DATETIME = time.strftime('%m%d%Y-%H%M%S')

TODAYBACKUPPATH = BACKUP_PATH + DATETIME

# Checking if backup folder already exists or not. If not exists will create it.
if not os.path.exists( TODAYBACKUPPATH ):
    os.makedirs( TODAYBACKUPPATH )

for db in backups:
  dumpcmd = "mysqldump -u " + db['user'] + " -p" + db['password'] + " " + db['name'] + " > " + TODAYBACKUPPATH + "/" + db['name'] + ".sql"
  os.system(dumpcmd)
#!/usr/local/bin/python3
import os
import requests
import sys
from pathlib import Path
from dotenv import load_dotenv
from utils import print_center, print_loop

# .env reader
env_file = '.env'
env_path = Path('.') / env_file
load_dotenv(dotenv_path=env_path)

# Colors
light_green = "\033[92m"
yellow = "\033[33m"
bold = "\033[1m"
blue = '\033[34m'
red = '\033[31m'
eoc = "\033[0m"

# Github
github_user = os.getenv('GITHUB_USERNAME')
github_token = os.getenv('GITHUB_TOKEN')

def get_github_data():
  github_res = requests.get('https://api.github.com/notifications', auth=(github_user, github_token))
  github = github_res.json()
  return github

def print_github():
  github = get_github_data()
  review_requested = {}
  subscribed = {}
  author = {}
  assigned = {}
  mention = {}
  for notification in github:
    id = notification['id']
    title = notification['subject']['title']
    to_update = { id: title }
    if notification['reason'] == 'review_requested':
        review_requested.update(to_update)
    if notification['reason'] == 'subscribed':
        subscribed.update(to_update)
    if notification['reason'] == 'author':
        author.update(to_update)
    if notification['reason'] == 'assigned':
        assigned.update(to_update)
    if notification['reason'] == 'mention':
        mention.update(to_update)
  print(red)
  print('\rGithub notifications: ' + str(len(github)))
  print('\r- review_requested: ' + str(len(review_requested)))
  print('\r- author: ' + str(len(author)))
  print('\r- assigned: ' + str(len(assigned)))
  print('\r- mention: ' + str(len(mention)))
  print('\r- subscribed: ' + str(len(subscribed)))
  print(eoc)

if sys.argv[0] == __file__:
  print_loop(print_github)
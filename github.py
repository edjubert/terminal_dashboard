#!/usr/local/bin/python3
import pync
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

# Default values
review_requested_number = 0
mention = 0


def get_github_data():
    github_res = requests.get(
        'https://api.github.com/notifications', auth=(github_user, github_token))
    github = github_res.json()
    return github


def send_notifications(review_requested, mention):
    if review_requested > review_requested_number:
        review_requested_number = review_requested
        pync.notify('You have been requested for a review',
                    title='Review Requested')
    if mention > mention_number:
        mention_number = mention
        pync.notify('You have been mentionned', title="Mention")


def print_github():
    github = get_github_data()
    review_requested = {}
    subscribed = {}
    author = {}
    assigned = {}
    mention = {}
    ci_activity = {}
    for notification in github:
        id = notification['id']
        title = notification['subject']['title']
        to_update = {id: title}
        if notification['reason'] == 'review_requested':
            review_requested.update(to_update)
        if notification['reason'] == 'subscribed':
            subscribed.update(to_update)
        if notification['reason'] == 'author':
            author.update(to_update)
        if notification['reason'] == 'assign':
            assigned.update(to_update)
        if notification['reason'] == 'ci_activity':
            ci_activity.update(to_update)
        if notification['reason'] == 'mention':
            mention.update(to_update)

    send_notifications(len(review_requested), len(mention))

    print(red)
    print_center('Github notifications: ' + str(len(github)))
    print_center('- review_requested: ' +
                 str(len(review_requested)), -len('- review_requested: '))
    print_center('- author: ' + str(len(author)), -len('- author: '))
    print_center('- assigned: ' + str(len(assigned)), -len('- assigned: '))
    print_center('- mention: ' + str(len(mention)), -len('- mention: '))
    print_center('- ci_activity: ' + str(len(ci_activity)), -
                 len('- ci_activity: '))
    print_center('- subscribed: ' + str(len(subscribed)), -
                 len('- subscribed: '))
    print(eoc)


if sys.argv[0] == __file__:
    print_loop(print_github)

import sys
from datetime import datetime
from utils import print_center, print_loop

# Colors
light_green = "\033[92m"
yellow = "\033[33m"
bold = "\033[1m"
blue = '\033[34m'
red = '\033[31m'
eoc = "\033[0m"


def get_datetime():
  now = datetime.now()
  hour = now.strftime("%H:%M")
  date = now.strftime("%d %B %Y")
  return hour, date

def print_date():
  hour, date = get_datetime()
  print(light_green + bold)
  print_center(hour)
  print(eoc + yellow)
  print_center(date)
  print(eoc)

if sys.argv[0] == __file__:
  print_loop(print_date)
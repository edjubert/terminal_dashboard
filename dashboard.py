from utils import get_terminal_width_height
from github import print_github
from weather import print_weather
from clock import print_date
from utils import print_center, print_padding, print_loop

eoc = "\033[0m"


def print_dashboard():
    print_padding()
    print_date()
    print_weather()
    print_github()
    print(eoc)


print_loop(print_dashboard)

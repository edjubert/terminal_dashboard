import subprocess, os, time

def get_terminal_width_height():
  size = subprocess.check_output(['stty', 'size']).split()
  width = int(size[1])
  height = int(size[0])
  return width, height

def print_center(to_print, padding = 10):
  width, height = get_terminal_width_height()
  print(to_print.center(width + padding))

def print_loop(f):
  os.system('clear')
  while True:
    f()
    time.sleep(30)

def print_padding():
  width, height = get_terminal_width_height()
  padding = int(height / 10)
  print('\n' * padding)

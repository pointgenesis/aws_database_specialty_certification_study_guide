import os

running_in_virtualenv = "VIRTUAL_ENV" in os.environ

# alternative ways to write this, also supporting the case where
# the variable is set but contains an empty string to indicate
# 'not in a virtual environment':
running_in_virtualenv = bool(os.environ.get("VIRTUAL_ENV"))
running_in_virtualenv = bool(os.getenv("VIRTUAL_ENV"))

import urllib.request


def get_comments() -> None:
    contents = urllib.request.urlopen("https://www.youtube.com/watch?v=BbeAOAmpkg4").read()
    print(contents)

def main():
    get_comments()


if __name__ == '__main__':
    main()

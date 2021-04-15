#!/usr/bin/env python3


# Included modules
import sys

# KomputerNet Modules
import komputernet


def main():
    if "--open_browser" not in sys.argv:
        sys.argv = [sys.argv[0]] + ["--open_browser", "default_browser"] + sys.argv[1:]
    komputernet.start()

if __name__ == '__main__':
    main()

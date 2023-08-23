#! /usr/bin/env python

"""
Purpose: CLI part for the parser
Author: Shelef Tavor (20.08.23)
"""

from merger import Merger
from IO.console_io import ConsoleIO


def main():
    """ The main function of the class """
    parser = Merger(ConsoleIO())
    parser.start_parsing()


if __name__ == "__main__":
    main()

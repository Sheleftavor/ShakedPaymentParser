#! /usr/bin/env python

"""
Purpose: CLI part for the parser
Author: Shelef Tavor (20.08.23)
"""

from parser import Parser
import pandas as pd


def main():
    """ The main function of the class """
    parser = Parser()
    parser.start_parsing()


if __name__ == "__main__":
    main()

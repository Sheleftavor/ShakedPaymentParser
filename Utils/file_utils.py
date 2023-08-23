#! /usr/bin/env python

"""
Purpose: Util functions for files
Author: Shelef Tavor (21.08.23)
"""

import json
from typing import List, Dict
import os
import pandas as pd

from Configuration import conf


def get_files_in_dir(dir_path: str) -> List[str]:
    """
    Returns a list of files in the given directory
    :param dir_path: The directory to look at
    :return: A list of files in the directory
    """
    return [file for file in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, file))]


def open_json(json_path: str) -> Dict[str, Dict]:
    """
    Opens a given json
    :param json_path: The path to the json file
    :return: The json in dict form
    """
    with open(json_path) as json_file:
        return json.load(json_file)


def get_payment_file_length(payment_file: str) -> int:
    """
    Returns the number of lines in a payment_file
    :param payment_file: The payment file to get the length of
    :return: The number of lines in the file
    """
    return len(pd.read_excel(conf.PAYMENTS_DIR + payment_file)) + 1


def is_line_number_in_limit(payment_file: str, line_number: int) -> bool:
    """
    Checks if the given line number is in the given payment file
    :param payment_file: The payment file to check for
    :param line_number: The line number
    :return: If line number is in the payment file
    """
    return 0 < line_number <= get_payment_file_length(payment_file)

#! /usr/bin/env python

"""
Purpose: Util functions for files
Author: Shelef Tavor (21.08.23)
"""

import json
from typing import List
import os


def get_files_in_dir(dir_path: str) -> List[str]:
    """
    Returns a list of files in the given directory
    :param dir_path: The directory to look at
    :return: A list of files in the directory
    """
    return [file for file in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, file))]


def open_json(json_path: str) -> dict:
    """
    Opens a given json
    :param json_path: The path to the json file
    :return: The json in dict form
    """
    with open(json_path) as json_file:
        return json.load(json_file)

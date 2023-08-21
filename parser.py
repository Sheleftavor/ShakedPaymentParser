#! /usr/bin/env python

"""
Purpose:
Author: Shelef Tavor (21.08.23)
"""

from Configuration import conf, consts
from Utils import files_utils
from IO.base_io import BaseIO
from typing import Dict, List


class Parser:
    """ """
    def __init__(self, io: BaseIO):
        self._io = io

    def start_parsing(self):
        """
        Starts parsing the excel files
        """
        self._io.send(consts.WELCOME_MESSAGE)
        payment_files = files_utils.get_files_in_dir(conf.PAYMENTS_DIR)
        payment_json = files_utils.open_json(conf.PAYMENT_CONF_JSON)
        if payment_json[conf.PAYMENT_JSON_BANK_FILE] not in payment_files:
            self._io.send(consts.BANK_FILE_NOT_FOUND)

    def __check_bank_file(self, payment_files: List[str], payment_json: Dict[str, Dict]) -> str:
        """
        Checks for a bank file and returns it
        :param payment_files: List of payment files in the directory
        :param payment_json: JSON settings file for payments files
        :return: The bank file
        """
        if payment_json[conf.PAYMENT_JSON_BANK_FILE] not in payment_files:
            self._io.send(consts.BANK_FILE_NOT_FOUND)
            #TODO get new bank file
        else:
            return payment_files[payment_files.index(payment_json[conf.PAYMENT_JSON_BANK_FILE])]

    def __parse_bank_file(self, bank_file: str, payment_json: Dict[str, Dict]):
        """
        Parses the bank payment file
        :param bank_file: The bank file to parse
        :param payment_json: JSON settings file for payments files
        """

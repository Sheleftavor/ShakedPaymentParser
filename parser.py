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
        """
        The init function of the class
        :param io: input output controller
        :payment_files: List of payment files in the directory
        :payment_json: JSON settings file for payments files
        """
        self._io = io
        self._payment_files = {}
        self._payment_json = {}

    def start_parsing(self):
        """
        Starts parsing the excel files
        """
        self._io.send(consts.WELCOME_MESSAGE)
        self._payment_files = files_utils.get_files_in_dir(conf.PAYMENTS_DIR)
        self._payment_json = files_utils.open_json(conf.PAYMENT_CONF_JSON)
        self.__parse_bank_file(self.__get_bank_file())

    def __get_bank_file(self) -> str:
        """
        Gets the bank file from the json and if it does not have it, it asks to choose one
        :return: The bank file
        """
        if self._payment_json[conf.BANK_FILE] not in self._payment_files:
            self._io.send(consts.BANK_FILE_NOT_FOUND)
            self.__show_payment_files()
            bank_file_index = self._io.recv(prompt=consts.BANK_FILE_CHOICE_PROMPT, confirm=True)
            while not bank_file_index.isnumeric() or (int(bank_file_index) < 1 or int(bank_file_index) > len(self._payment_files)):
                bank_file_index = self._io.recv(prompt=consts.INVALID_CHOICE, confirm=True)
            bank_file_name = self._payment_files[int(bank_file_index)-1] 
            # Adding bank file name to json
            self._payment_json[conf.BANK_FILE][bank_file_name] = {}
            return bank_file_name
        else:
            return self._payment_files[self._payment_files.index(self._payment_json[conf.BANK_FILE])]

    def __parse_bank_file(self, bank_file: str):
        """
        Parses the bank payment file
        :param bank_file: The bank file to parse
        """


    def __get_header_line_number(self, payment_file: str) -> int:
        """
        Gets the excel file header line number and if it does not have it, it asks for one
        :param payment_file: The payment file to get the header line number for
        :return: The header line number
        """
        if self._payment_json[conf.BANK_FILE][payment_file].get(conf.HEADER_LINE_NUMBER) is None:
            header_line_number = self._io.recv(prompt=consts.HEADER_LINE_NUMBER_NOT_FOUND, confirm=True)
            while not header_line_number.isnumeric():
                header_line_number = self._io.recv(prompt=consts.INVALID_CHOICE, confirm=True)

        else:
            return self._payment_json[conf.BANK_FILE][payment_file].get(conf.HEADER_LINE_NUMBER)

    def __show_payment_files(self):
        """
        Shows the payment files in a nice format
        """
        for index, file in enumerate(self._payment_files, start=1):
            self._io.send(f"{index}. {file}")

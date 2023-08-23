#! /usr/bin/env python

"""
Purpose: Parser for bank payment file
Author: Shelef Tavor (22.08.23)
"""

from Configuration import conf, consts
from Parsers.base_parser import BaseParser


class BankParser(BaseParser):
    """ Parser for bank payment file """
    NAME = conf.BANK_FILE

    def start_parsing(self) -> dict:
        """
        Parses the file and returns a dict for the parsed stuff
        :return: The parsed stuff from the file
        """
        bank_file = self.__get_bank_file()
        header_line_number = self.__get_header_line_number(bank_file)

    def __get_bank_file(self) -> str:
        """
        Gets the bank file from the json and if it does not have it, it asks to choose one
        :return: The bank file
        """
        if self._payment_data.payment_json[self.NAME] not in self._payment_data.payment_files:
            self._io.send(consts.BANK_FILE_NOT_FOUND)
            self.__show_payment_files()
            bank_file_index = self._io.recv(prompt=consts.BANK_FILE_CHOICE_PROMPT, confirm=True)
            while not bank_file_index.isnumeric() or (
                    int(bank_file_index) < 1 or int(bank_file_index) > len(self._payment_data.payment_files)):
                bank_file_index = self._io.recv(prompt=consts.INVALID_CHOICE, confirm=True)
            bank_file_name = self._payment_data.payment_files[int(bank_file_index) - 1]
            # Adding bank file name to json
            self._payment_data.payment_json[self.NAME][bank_file_name] = {}
            return bank_file_name
        else:
            return self._payment_data.payment_files[
                self._payment_data.payment_files.index(self._payment_data.payment_json[self.NAME])]


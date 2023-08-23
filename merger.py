#! /usr/bin/env python

"""
Purpose: Merges many payment excel files in to one excel file that shows the total in a nice way
Author: Shelef Tavor (21.08.23)
"""

from Configuration import conf, consts
from Utils import file_utils
from IO.base_io import BaseIO
from DTO.payment_data import PaymentData
from Parsers.bank_parser import BankParser


class Merger:
    """ """

    def __init__(self, io: BaseIO):
        """
        The init function of the class
        :param io: input output controller
        :payment_files: List of payment files in the directory
        :payment_json: JSON settings file for payments files
        """
        self._io = io
        self._payment_data = PaymentData(file_utils.open_json(conf.PAYMENT_CONF_JSON),
                                         file_utils.get_files_in_dir(conf.PAYMENTS_DIR))

    def start_parsing(self):
        """
        Starts parsing the excel files
        """
        self._io.send(consts.WELCOME_MESSAGE)
        bank_parser = BankParser(self._payment_data, self._io)
        parsed_data = bank_parser.start_parsing()

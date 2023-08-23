#! /usr/bin/env python

"""
Purpose: Merges many payment excel files in to one excel file that shows the total in a nice way
Author: Shelef Tavor (21.08.23)
"""

from Configuration import conf, consts
from Utils import files_utils
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
        self._payment_data = PaymentData(files_utils.open_json(conf.PAYMENT_CONF_JSON),
                                         files_utils.get_files_in_dir(conf.PAYMENTS_DIR))
        bank_parser = BankParser(self._payment_data)
        parsed_data = bank_parser.start_parsing()


    def start_parsing(self):
        """
        Starts parsing the excel files
        """
        self._io.send(consts.WELCOME_MESSAGE)


    def __show_payment_files(self):
        """
        Shows the payment files in a nice format
        """
        for index, file in enumerate(self._payment_data.payment_files, start=1):
            self._io.send(f"{index}. {file}")

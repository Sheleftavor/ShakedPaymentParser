#! /usr/bin/env python

"""
Purpose: Base class for a payment excel file parser
Author: Shelef Tavor (22.08.23)
"""

from abc import ABC, abstractmethod
import pandas as pd

from DTO.payment_data import PaymentData
from Configuration import conf, consts
from IO.base_io import BaseIO
from Utils import file_utils


class BaseParser(ABC):
    """ Base class for a payment excel file parser """

    def __init__(self, payment_data: PaymentData, io: BaseIO):
        """
        The init function of the class
        :param payment_data: DTO for payments
        :param io: input output
        """
        self._payment_data = payment_data
        self._io = io

    @abstractmethod
    def start_parsing(self) -> dict:
        """
        Parses the file and returns a dict for the parsed stuff
        :return: The parsed stuff from the file
        """

    def _get_header_line_number(self, payment_file: str) -> int:
        """
        Gets the excel file header line number and if it does not have it, it asks for one
        :param payment_file: The payment file to get the header line number for
        :return: The header line number
        """
        df = pd.read_excel(conf.PAYMENTS_DIR + payment_file)

        if self._payment_data.payment_json[self.NAME][payment_file].get(conf.HEADER_LINE_NUMBER) is None or \
                self._payment_data.payment_json[self.NAME][payment_file][conf.HEADERS] != df.values[
                self._payment_data.payment_json[self.NAME][payment_file][conf.HEADER_LINE_NUMBER]]:

            header_line_number = self._io.recv(prompt=consts.HEADER_LINE_NUMBER_NOT_FOUND, confirm=True)
            while not header_line_number.isnumeric() or not file_utils.is_line_number_in_limit(payment_file,
                                                                                               int(header_line_number)):
                header_line_number = self._io.recv(prompt=consts.LINE_OUT_OF_BOUNDS, confirm=True)
            self._payment_data.payment_json[self.NAME][payment_file][conf.HEADER_LINE_NUMBER] = int(header_line_number)
            self._payment_data.payment_json[self.NAME][payment_file][conf.HEADERS] = df.values[
                int(header_line_number) - consts.EXCEL_LINE_NUMBER_DIFFERENCE]
            return int(header_line_number)
        else:
            return self._payment_data.payment_json[self.NAME][payment_file][conf.HEADER_LINE_NUMBER]

    def _show_payment_files(self):
        """
        Shows the payment files in a nice format
        """
        for index, file in enumerate(self._payment_data.payment_files, start=1):
            self._io.send(f"{index}. {file}")

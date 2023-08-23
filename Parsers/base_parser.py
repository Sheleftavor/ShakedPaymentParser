#! /usr/bin/env python

"""
Purpose: Base class for a payment excel file parser
Author: Shelef Tavor (22.08.23)
"""

from abc import ABC, abstractmethod

from DTO.payment_data import PaymentData
from Configuration import conf, consts


class BaseParser(ABC):
    """ Base class for a payment excel file parser """
    def __init__(self, payment_data: PaymentData):
        """
        The init function of the class
        :param payment_data: DTO for payments
        """
        self._payment_data = payment_data

    @abstractmethod
    def start_parsing(self) -> dict:
        """
        Parses the file and returns a dict for the parsed stuff
        :return: The parsed stuff from the file
        """

    def __get_header_line_number(self, payment_file: str) -> int:
        """
        Gets the excel file header line number and if it does not have it, it asks for one
        :param payment_file: The payment file to get the header line number for
        :return: The header line number
        """
        if self._payment_data.payment_json[self.NAME][payment_file].get(conf.HEADER_LINE_NUMBER) is None:
            header_line_number = self._io.recv(prompt=consts.HEADER_LINE_NUMBER_NOT_FOUND, confirm=True)
            while not header_line_number.isnumeric():
                header_line_number = self._io.recv(prompt=consts.INVALID_CHOICE, confirm=True)
            # TODO add line number
        else:
            return self._payment_data.payment_json[self.NAME][payment_file].get(conf.HEADER_LINE_NUMBER)


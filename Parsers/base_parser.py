#! /usr/bin/env python

"""
Purpose: Base class for a payment excel file parser
Author: Shelef Tavor (22.08.23)
"""

from abc import ABC, abstractmethod

from DTO.payment_data import PaymentData


class BaseParser(ABC):
    """ Base class for a payment excel file parser """
    def __init__(self, payment_data: PaymentData, payment_file: str):
        """
        The init function of the class
        :param payment_data: DTO for payments
        :param payment_file: The payment file to parse
        """
        self._payment_data = payment_data
        self._payment_file = payment_file

    @abstractmethod
    def start_parsing(self) -> dict:
        """
        Parses the file and returns a dict for the parsed stuff
        :return: The parsed stuff from the file
        """

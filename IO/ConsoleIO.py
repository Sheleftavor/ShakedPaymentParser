#! /usr/bin/env python

"""
Purpose: IO for console
Author: Shelef Tavor (21.08.23)
"""

from IO.base_io import BaseIO
from typing import Union


class ConsoleIO(BaseIO):
    """ IO for console """
    def send(self, toutput: str):
        """
        Prints output to console
        :param toutput: The output
        """
        print(toutput)

    def recv(self, prompt: Union[str, None] = None) -> str:
        """
        Receives input from console
        :return: The input received
        """
        return input(prompt)

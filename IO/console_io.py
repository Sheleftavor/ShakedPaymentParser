#! /usr/bin/env python

"""
Purpose: IO for console
Author: Shelef Tavor (21.08.23)
"""

from IO.base_io import BaseIO
from typing import Union

from Configuration import consts


class ConsoleIO(BaseIO):
    """ IO for console """
    def send(self, toutput: str):
        """
        Prints output to console
        :param toutput: The output
        """
        print(toutput)

    def recv(self, prompt: Union[str, None] = None, confirm: bool = False) -> str:
        """
        Receives input from console
        :param prompt: prompt to enter in input
        :param confirm: Confirm the input
        :return: The input received
        """
        recv = input(prompt)
        while confirm:
            confirm_input = input(consts.RECV_CONFIRMATION_MESSAGE.format(recv))
            if confirm_input.lower() == consts.RECV_CONFIRM_TRUE:
                break
            recv = input(prompt)
        return recv

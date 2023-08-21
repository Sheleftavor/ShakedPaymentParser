#! /usr/bin/env python

"""
Purpose: Base class for IO
Author: Shelef Tavor (21.08.23)
"""

from abc import ABC, abstractmethod
from typing import TypeVar

TInput = TypeVar("TInput")
TOutput = TypeVar("TOutput")


class BaseIO(ABC):
    """ Interface for IO """
    @abstractmethod
    def send(self, toutput: TOutput):
        """
        Sends output
        :param toutput: The input to send
        """

    @abstractmethod
    def recv(self) -> TInput:
        """
        Receives input
        :return: The input
        """

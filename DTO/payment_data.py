#! /usr/bin/env python

"""
Purpose: DTO for payment data
Author: Shelef Tavor (22.08.23)
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class PaymentData:
    """ DTO for payment data """
    payment_json: Dict[str, Dict]
    payment_files: List[str]

#! /usr/bin/env python

"""
Purpose:
Author: Shelef Tavor (21.08.23)
"""

from Configuration import conf
from Utils import files_utils


class Parser:
    """ """
    def start_parsing(self):
        """
        Runs on all payment files and creates an excel file from all of them
        """
        print(files_utils.get_files_in_dir(conf.PAYMENTS_DIR))
        print(files_utils.open_json(conf.PAYMENT_CONF_JSON)['main'])

#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import sys


class FileReader(object):

    def __init__(self, input_file):

        self.input_file = input_file

    def get_file_data(self):

        try:
            data = list(csv.reader(open(self.input_file)))
            return data
        except IOError:
            sys.exit('Could not read file.')

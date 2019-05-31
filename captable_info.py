#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

from captable_information import CapTableInformation
from file_reader import FileReader


def main():

    program_arguments = sys.argv[1:]

    if not program_arguments:
        sys.exit('Provide a valid csv file path.')
    if '.csv' not in program_arguments[0]:
        sys.exit('Provide a valid csv file.')

    file_reader_object = FileReader(program_arguments[0])
    data = file_reader_object.get_file_data()

    if len(program_arguments) == 2:
        cap_table_information_object = CapTableInformation(data)
        cap_table_information_json = \
            cap_table_information_object.get_captable_information(program_arguments[1])
    elif len(program_arguments) > 2:
        sys.exit('Invalid arguments provided to the program.')
    else:
        cap_table_information_object = CapTableInformation(data)
        cap_table_information_json = \
            cap_table_information_object.get_captable_information()

    print cap_table_information_json


if __name__ == '__main__':
    main()

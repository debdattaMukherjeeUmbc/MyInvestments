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

    FileReaderObject = FileReader(program_arguments[0])
    data = FileReaderObject.get_file_data()

    if len(program_arguments) == 2:
        CapTableInformationObject = CapTableInformation(data)
        CapTableInformationJson = \
            CapTableInformationObject.get_captable_information(program_arguments[1])
    elif len(program_arguments) > 2:
        sys.exit('Invalid arguments provided to the program.')
    else:
        CapTableInformationObject = CapTableInformation(data)
        CapTableInformationJson = \
            CapTableInformationObject.get_captable_information()

    print CapTableInformationJson


if __name__ == '__main__':
    main()

import datetime
import sys

"""
Parses a date from a string to a datetime object.
"""
def date_parser(date_str):
    
    try:
        format_str = '%Y-%m-%d'
        date_value = datetime.datetime.strptime(date_str, format_str)
        return date_value
    except ValueError:
        sys.exit('Unrecognized date format, please try again!')


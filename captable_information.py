#!/usr/bin/python
# -*- coding: utf-8 -*-
import datetime
import json
import sys

from date_parser import date_parser
from investor_information import InvestorInformation


class CapTableInformation(object):

    def __init__(self, data):

        self.investors_information = [InvestorInformation(i) for i in
                data[1:]]

    
    """
    Returns the captable information as json and also excepts an optional parameter
    of date. If a date argument is provided, the summary cap table is computed using 
    investments made on or before the specified date.  If no date is given, the cap table 
    is calculated as of today.
    """
    def get_captable_information(self, start_date=None):

        current_date = datetime.datetime.now()
        current_date_str = current_date.strftime('%m/%d/%Y')

        relevant_investors_info = \
            self._get_relevant_investors(start_date, current_date)

        (cash_raised, total_number_of_shares) = \
            self._get_cash_raised_total_share(relevant_investors_info.values())
        ownership = \
            self._ownership_information(relevant_investors_info,
                total_number_of_shares)

        captable_information = {
            'date': current_date_str,
            'cash_raised': cash_raised,
            'total_number_of_shares': total_number_of_shares,
            'ownership': ownership,
            }

        return json.dumps(captable_information)


    """
    Returns the cash paid and total number of shares for the investors.
    """
    def _get_cash_raised_total_share(self, relevant_investors_info):

        cash_paid = 0
        total_number_of_shares = 0

        for investor_information in relevant_investors_info:
            cash_paid += investor_information.get('cash_paid')
            total_number_of_shares += investor_information.get('shares')
        return (cash_paid, total_number_of_shares)


    """
    Excepts the relevant investors information and total number of shares and computes the ownership information.
    """
    def _ownership_information(self, relevant_investors_info,
                               total_number_of_shares):

        ownership_information = []
        for investor_info in relevant_investors_info:
            investor_dict = {}
            investor_dict['investor'] = investor_info
            investor_dict['shares'] = \
                relevant_investors_info[investor_info]['shares']
            investor_dict['cash_paid'] = \
                relevant_investors_info[investor_info]['cash_paid']
            if total_number_of_shares:
                investor_dict['ownership'] = \
                    round(float(investor_dict['shares'] * 100)
                          / total_number_of_shares, 2)
            ownership_information.append(investor_dict)
        return ownership_information


    """
    Returns the merged(processed) relevant investors for the required time duration.
    """
    def _get_relevant_investors(self, start_date, current_date):

        investors_within_timeframe = \
            self._get_investors_within_timeframe(start_date,
                current_date)
        relevant_investors = \
            self._get_merged_investors_information(investors_within_timeframe)
        return relevant_investors


    """
    Curates the investments of the investors within the desired time range. If the start date is 
    supplied, it would consider all entries made on or before the specified date; else it
    will consider all entries till current date.
    """
    def _get_investors_within_timeframe(self, start_date, current_date):

        investors_within_timeframe = []

        if start_date:
            start_date = date_parser(start_date)
        for investor in self.investors_information:
            investment_date = date_parser(investor.investment_date)
            if start_date:
                if investment_date <= start_date:
                    investors_within_timeframe.append(investor)
            elif investment_date <= current_date:
                investors_within_timeframe.append(investor)
        return investors_within_timeframe

    
    """
    Merges different entries for the same investors as a single record.
    """
    def _get_merged_investors_information(self,
            investors_within_timeframe):

        merged_investors_information = {}
        for investor in investors_within_timeframe:
            if investor.investor_name \
                not in merged_investors_information:
                merged_investors_information[investor.investor_name] = \
                    {'shares': int(investor.shares_purchased),
                     'cash_paid': float(investor.cash_paid)}
            else:
                merged_investors_information[investor.investor_name]['shares'
                        ] += int(investor.shares_purchased)
                merged_investors_information[investor.investor_name]['cash_paid'
                        ] += float(investor.cash_paid)
        return merged_investors_information


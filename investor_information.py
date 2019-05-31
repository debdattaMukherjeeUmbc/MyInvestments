import operator
import sys


"""
Class to represent Investor Information. Additionally it validates if fields 
such as investment date, investor name, cash paid and shares purchased are present or not.
"""
class InvestorInformation(object):
   
	def __init__(self, row):

		self.investment_date =  row[0]
		self.shares_purchased = row[1] 
		self.cash_paid = row[2]
		self.investor_name = row[3]


	investment_date = property(operator.attrgetter('_investment_date'))

	@investment_date.setter
	def investment_date(self, date):

		if not date:
			sys.exit('File has missing date entry.')
		self._investment_date = date

	
	shares_purchased = property(operator.attrgetter('_shares_purchased'))

	@shares_purchased.setter
	def shares_purchased(self, shares):

		if not shares: 
			sys.exit('File has missing shares entry.')
		self._shares_purchased = shares

	
	cash_paid = property(operator.attrgetter('_cash_paid'))
	
	@cash_paid.setter
	def cash_paid(self, cash):

		if not cash: 
			sys.exit('File has missing cash entry.')
		self._cash_paid = cash


	investor_name = property(operator.attrgetter('_investor_name'))

	@investor_name.setter
	def investor_name(self, name):

		if not name: 
			sys.exit('File has missing name entry.')
		self._investor_name = name


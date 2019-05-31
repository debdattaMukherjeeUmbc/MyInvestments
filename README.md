# MyInvestments
This project gives a way to get synopsis of investments, growth and market share.

This project gives a way to query the Cap Table Information for a particular company to get investor’s information. It returns the captable information as json and also excepts an optional parameter
of date. If a date argument is provided, the summary cap table is computed using 
investments made on or before the specified date.  If no date is given, the cap table 
is calculated as of today.


Getting Started
These instructions will get you a copy of the project up and running on your local machine for testing purposes. See the notes below:

	Prerequisites
	Have Python 2.7.10 installed in your machine.

	Running the project
	In you python terminal run the captable_info.py file. 
        It takes in the cvs file as input, so you can run the following: 
        python captable_info.py input.csv
        If you want to pass in an optional param of date, then run the following:
        python captable_info.py input.csv 2017-11-14
        Running the above commands produces the json response in the terminal.

Further work which is in progress:
1. Adding a UI with grahical representation of the data.
2. Calculating profit and loss.
3. Showing captable information of multiple companies together.
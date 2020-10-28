from argparse import FileType
import re
import argparse
import pandas as pd

from categories import cat # Categorizations stored here
from collections.abc import Mapping

# Argument Parsing
parser = argparse.ArgumentParser()
parser.add_argument('file',
                    help="provide file to be parsed")
parser.add_argument('-v','--verbose', action='store_true', default=False,
                    help='Flag for printing details to the command line')
parser.add_argument('--debug', action='store_true', default=False,
                    help='Flag for debug printing to the command line')
parser.add_argument('-sl','--skip', type=int, default=3,
                    help='# of lines to skip before column headers. Butterfield has 3 lines before header')
args = parser.parse_args()

#Variables
accountNum = 0
accountName = currency = "blah"
balanceOpen = balanceClose = 0.00
filename = args.file
FileFrom = 'blah' # TODO: Parse file metadata to determine source
headerAt = args.skip
isDebug = args.debug
isPrintDetails = args.verbose
lineCount = 1

print("\n--------------------\nhello world\n") if isDebug else None

# Get CSV MetaData
metadata = pd.read_csv(filename, nrows=3, header=None, skipinitialspace=True, encoding='utf-8')
accountNum = metadata[0][0]
accountName = metadata[1][0]
currency = (re.search(r'([a-zA-Z]+)', metadata[1][1])).group(0) # get currency code from openening balance
balanceOpen = float((re.search(r'(\d+[,.]\d+)', metadata[1][1])).group(0)) # Should get numbers even if Butterfield starts using ,
balanceClose = float((re.search(r'(\d+[,.]\d+)', metadata[1][2][4:])).group(0)) 

# For printing to the command line if isDebug or isPrintDetails
print('\n\n-----------------------\n\nAccount Number:', accountNum, '\nAccount Name:', accountName, '\nCurrency:', currency, '\nOpening Balance:', balanceOpen, '\nClosing Balance:', balanceClose, '\n\n') if isDebug or isPrintDetails else None
print(metadata[1:3],'\n\n-------------------\n') if isDebug else None

# Get Transaction Records
records = pd.read_csv(filename, header=headerAt, skipinitialspace=True, encoding='utf-8')

# Prepend account Number
records.insert(loc=0, column='Account', value=accountNum)

# Which Card was used?
records.insert(loc=1, column='Card', value=accountNum)
records['Card'] = records.Description.apply(lambda x: (re.search(r'\d{4}', x)).group(0) if re.search(r'\d{4}', x) else None)

# convert date formats
records['Transaction Date'] = pd.to_datetime(records['Transaction Date'], format='%d %b %Y')
records['Value Date'] = pd.to_datetime(records['Value Date'], format='%d %b %Y')

# Add Amount Column 
# My Budget app does support negative and positive value columns
# But Butterfield records refunds as negative debits
# Sets Amount = Debit * -1 unless it's NaN, then it sets Credit
records.insert(loc=7, column='Amount', value=accountNum)
records['Amount'] = (records['Debit'] * -1.00).fillna(records['Credit'])

# Categorize Records
def categorize(description,amount): # TODO extend to consider card number
    # iterate through categories
    for k, v in cat.items():
        # if key patter matches description and value is a mapping
        if re.search(k,description.upper()) and isinstance(v, Mapping):
            # try to get category based on amount of transaction
            try: 
                return v[amount]
            # except if the amount key is not found
            except(KeyError):
                None
        # else if just check for key pattern match
        elif re.search(k,description.upper()):
            return v

# apply on data frame, x = record, pass record's desctiption and amount to categorize
records['Category'] = records.apply(lambda x: categorize(x['Description'],x['Amount']),axis=1)
# old approach to categorization. Doesn't support considering two columns
# records['Category'] = records.Description.apply(
#     lambda x: [v for k, v in cat.items() if re.search(k, x.upper())]
#     ).explode()

# Write output to file. First re.match() pulls single-word characters before .csv 2nd captures filetype
records.to_csv( (re.match(r'\S*(?=.csv)',filename)).group(0) + '-output' + (re.search(r'\.\w+',filename)).group(0))

# For printing to the command line
print(records.sort_values(by=['Value Date'],ascending=False)) if isDebug or isPrintDetails else None
print("{} Transactions Parsed".format(len(records.index))) if isPrintDetails else None

import re

import pandas as pd

from categories import cat

accountNum = 0
accountName = currency = "blah"
balanceOpen = balanceClose = 0.00
filename = 'testFiles/Butterfield.csv'
headerAt = 3
isDebug = False
isPrintDetails = True
lineCount = 1

print("\n--------------------\nhello world\n") if isDebug else None

# Get Extract MetaData
metadata = pd.read_csv(filename, nrows=3, header=None, skipinitialspace=True, encoding='utf-8')
accountNum = metadata[0][0]
accountName = metadata[1][0]
currency = (re.search(r'([a-zA-Z]+)', metadata[1][1])).group(0) # get currency code from openening balance
balanceOpen = (re.search(r'(\d+[,.]\d+)', metadata[1][1])).group(0) # Should get numbers even if Butterfield starts using ,
balanceClose = (re.search(r'(\d+[,.]\d+)', metadata[1][2][4:])).group(0) 

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

# Categorize Records
records['Category'] = records.Description.apply(lambda x: [v for k, v in cat.items() if re.search(k, x.upper())]).explode()

# Add Amount Column 
# My Budget app does support negative and positive value columns
# But Butterfield records refunds as negative debits
# Sets Amount = Debit * -1 unless it's NaN, then it sets Credit
records.insert(loc=7, column='Amount', value=accountNum)
records['Amount'] = (records['Debit'] * -1.00).fillna(records['Credit'])

# noExt = re.match(r'\S*(?=.csv)',filename)
records.to_csv( (re.match(r'\S*(?=.csv)',filename)).group(0) + '-output' + (re.search(r'\.\w+',filename)).group(0))
# For printing to the command line
print(records.sort_values(by=['Value Date'],ascending=False)) if isDebug or isPrintDetails else None
# pyBankBDA
Python scripts for massaging Bermudian Bank .csv files 
then categorizing them based on the description (and hopefully transaction amount too)
Currently Supports Butterfield Bank .CSV files

## currently requires 
    pandas

Will eventually extend it out to conduct budget tracking based on categorized transactions.

## To run as Automator Script if you've installed python3 using hombrew 
...or just python3 period as MacOS ships with python 2.7 or something like that
Replace python3 path with path to your python3 install

Createed my Automator as a quick action 
(so that it's executable from right-click > service > Butterfield)

Run Shell Script content:
```python
for f in "$@"; do 
	/usr/local/Cellar/python/3.7.3/bin/python3 [path to local repo]/pyBankBDA/parse_CSV.py "$f"; 
done
```

Screenshot:
![Image of Automator Quick Action Workflow](https://github.com/cod3-jr/pyBankBDA/blob/dev/Automator%20Screenshot.png)

### Notes
- IRL Butterfield.csv file has 2 columns for first 3 rows. I just added columns so that it looks pretty on github.

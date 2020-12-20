import re
import subprocess

#import parse_CSV

## Get fromWhere attribute from file
fromWhere =  subprocess.Popen(["mdls", "-n","kMDItemWhereFroms", "/Users/mischafubler/Downloads/1608386576453.csv"], stdout=subprocess.PIPE)
output = fromWhere.communicate() [0].decode('utf-8')
output = re.search(r'(?<=\.)\w+\.com|\w+\.bm',output).group(0)
print(output)

## one line fromWhere
test = re.search(r'(?<=\.)\w+\.com|\w+\.bm', subprocess.Popen(["mdls", "-n","kMDItemWhereFroms", "/Users/mischafubler/Downloads/1608386576453.csv"], stdout=subprocess.PIPE).communicate() [0].decode('utf-8')).group(0) 
print(test)
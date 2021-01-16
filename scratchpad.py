import re
import subprocess

#import parse_CSV

## Get fromWhere attribute from file
fromWhere =  subprocess.Popen(["mdls", "-n","kMDItemWhereFroms", "/Users/mischafubler/Dropbox/Mischa/GIt/pyBankBDA/testFiles/1610760710444.csv"], stdout=subprocess.PIPE)
output = fromWhere.communicate() [0].decode('utf-8')
output = re.search(r'(?<=\.)\w+\.com|\w+\.bm',output).group(0) if re.search(r'(?<=\.)\w+\.com|\w+\.bm',output) is not None else "unknown"
print(output)

## one line fromWhere 
test = re.search(r'(?<=\.)\w+\.com|\w+\.bm', subprocess.Popen(["mdls", "-n","kMDItemWhereFroms", "/Users/mischafubler/Downloads/1608386576453.csv"], stdout=subprocess.PIPE).communicate() [0].decode('utf-8')).group(0)
print(test)

## Manually set files Where From attribute
# xattr -w 'com.apple.metadata:kMDItemWhereFroms' '<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><array><string>blob:https://www.butterfieldonline.com/5b79249b-5969-4d46-a02c-21eac7156da1</string></array></plist>' testFiles/1608386576453.csv
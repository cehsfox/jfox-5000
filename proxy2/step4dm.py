#!/usr/bin/python

import re
from urllib.parse import urlparse

f = open("domain2.txt", "r")
w = open("domain3.txt", "w")


for line in f:
    print("before: "+line)
    if str(line.count('.')) == '2':
        line = re.search(r"(.*?)\.(.*)",line).group(2)
    if str(line.count('.')) == '3':
        line = re.search(r"(.*?)\.(.*)",line).group(2)
    if str(line.count('.')) == '4':
        line = re.search(r"(.*?)\.(.*)",line).group(2)
    if str(line.count('.')) == '5':
        line = re.search(r"(.*?)\.(.*)",line).group(2)
    if str(line.count('.')) == '6':
        line = re.search(r"(.*?)\.(.*)",line).group(2)
    if str(line.count('.')) == '7':
        line = re.search(r"(.*?)\.(.*)",line).group(2)  
    if str(line.count('.')) == '8':
        line = re.search(r"(.*?)\.(.*)",line).group(2)
    if str(line.count('.')) == '9':
        line = re.search(r"(.*?)\.(.*)",line).group(2)  
    print("after: "+line)
    w.write(line)

f.close()
w.close()


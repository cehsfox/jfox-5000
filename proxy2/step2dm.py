#!/usr/bin/python

import re

f = open("domain1.txt", "r")
w = open("domain2.txt", "w")


for line in f:
    line = line.replace("DJ ", "")
    line = line.replace("HJ ", "")
    line = line.replace("https://", "")
    line = line.replace("http://", "")
    line = line.replace("www.", "")
    line = line.replace("/app/home/*", "")
    line = line.replace("#", "")
    line = line.replace("/*", "")
    line = line.rstrip("\r")
    w.write(line)

f.close()
w.close()


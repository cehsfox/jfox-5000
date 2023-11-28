#!/usr/bin/python

f = open("config.txt", "r")
w = open("domain.txt", "w")


for line in f:
    if "DJ " in line:
        print(line)
        w.write(line)
    elif "HJ " in line:
        print(line) 
        w.write(line)
         
#!/usr/bin/python

f = open("domain1.txt", "r")
w = open("domain2.txt", "w")


for line in f:
    line = line.replace("DJ ", "")
    line = line.replace("HJ ", "")
    line = line.replace("https://", "")
    line = line.replace("http://", "")
    line = line.replace("www.", "")
    w.write(line)

f.close()
w.close()


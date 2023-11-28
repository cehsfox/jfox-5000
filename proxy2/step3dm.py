#!/usr/bin/python

f = open("domain2.txt", "r")
w = open("domain3.txt", "w")


for line in f:
    if line.count('.') == 4:
        print(line)


f.close()
w.close()


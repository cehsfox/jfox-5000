import re

rfile = open('allow.txt', 'r')
wfile = open('allow1.txt', 'w')

for line in rfile:
    if "." in line:
        line = line.replace('\\.', '.')
        wfile.write(line)
rfile.close()
wfile.close()
import re

rfile = open('domain3.txt', 'r')
wfile = open('domain4.txt', 'w')

for line in rfile:
    if "." in line:
        line = line.replace('.', '\\.')
        wfile.write(line)
rfile.close()
wfile.close()
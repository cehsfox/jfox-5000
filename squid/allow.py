import re

rfile = open('allow-domain.express', 'r')
wfile = open('express.txt', 'w')

for line in rfile:
    if "." in line:
        line = line.replace('\\.', '.')
        wfile.write(line)
rfile.close()
wfile.close()
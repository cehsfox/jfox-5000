import re

rfile = open('express.txt', 'r')
wfile = open('express1.txt', 'w')

for line in rfile:
    if re.search(r'(\w+\.)(\w+\.)(\D+$)', line):
        match = re.search(r'(\w+\.)(\w+\.)(\D+$)', line)
        wfile.write(match.group(2)+match.group(3))
rfile.close()
wfile.close()
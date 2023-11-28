import re

rfile = open('domain.txt', 'r')
wfile = open('domain2.txt', 'w')

for line in rfile:
    if "URLglobal" in line:
        print("deleted: "+line)
    elif "Uglobal" in line:
        print("deleted: "+line)
    elif re.search(r'(\w+\.)(\w+\.)(\w+\.)(\D+$)', line):
        match = re.search(r'(\w+\.)(\w+\.)(\w+\.)(\D+$)', line)
        wfile.write(match.group(3)+match.group(4))
    elif re.search(r'(\w+\.)(\w+\.)(\D+$)', line):
        match = re.search(r'(\w+\.)(\w+\.)(\D+$)', line)
        wfile.write(match.group(2)+match.group(3))     
    else:
        wfile.write(line)
rfile.close()
wfile.close()
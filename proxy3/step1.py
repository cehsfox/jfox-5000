
import re

rfile = open('config.txt', 'r')

for line in rfile:
    line = line.strip()
    if re.search('.+\.+', line):
        print(line)
        match = re.search(r'(https?://)?(www\.)?([^/]+)\.[^/]+', line)
        if match:
            print(match.group(3))
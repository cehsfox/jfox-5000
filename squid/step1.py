
import re

ezproxy = open('config.txt', 'r')
domain = open('domain.txt', 'w')

for line in ezproxy:
    line = line.strip()
    if 'DJ' in line or 'HJ' in line:
        line = line.replace('DJ ', '')
        line = line.replace('HJ ', '')
        line = line.replace('#', '')
        line = line.replace('*.', '')
        line = line.replace(' ', '')
        line = line.replace('https://', '')
        line = line.replace('http://', '')
        line = line.replace('www.', '')
        line = line.replace('/', '')
        print(line)
        domain.write(line+'\n')
 
ezproxy.close()
domain.close()









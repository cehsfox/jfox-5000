
import re

ezproxy = open('domain.txt', 'r')
domain = open('domainlist.txt', 'w')

line = ezproxy.readline()
while line:
    line = ezproxy.readline()
    print("before: "+line)
    if str(line.count('.')) == '3':
        line = re.search(r"(.*?)\.(.*)",line).group(2)
        print("more than 3")
    if str(line.count('.')) == '4':
        line = re.search(r"(.*?)\.(.*)",line).group(2)
        print("more than 4")
    line = line.replace('.', '\.')
    print("after: "+line)
    domain.write(line)
ezproxy.close()
domain.close()









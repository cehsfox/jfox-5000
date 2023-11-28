
import re

ezproxy = open('config.txt', 'r')
domain = open('domain.txt', 'w')

line = ezproxy.readline()
while line:
    line = ezproxy.readline()
    if 'DJ' in line:
        line = line.replace('DJ ', '')
        line = line.replace('#', '')
        line = line.replace('*.', '')
        line = line.replace(' ', '')
        line = line.replace('https://', '')
        line = line.replace('/en/sess/login.asp?xsid=S003Wvf3cvb3cFaYXmnNdmnMD6pMT6mN9Am5DByMU38ODJ9RcyqUUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUEA', '')
        line = line.replace('/app/home/*', '')
        line = line.replace('Uhttp://', '')
        line = line.replace('/', '')
 #       line = line.replace('.', '\.')
        line = line[:-1]
        print(line)
        domain.write(line+'\n')
 
ezproxy.close()
domain.close()










import re

rfile = open('config.txt', 'r')
wfile = open('domain.txt', 'w')

for line in rfile:
    line = line.strip()
    if re.search(r'(\w+\.)(\D+$)', line):
        print(line)
        line = line.replace("DJ ", "")
        line = line.replace("HJ ", "")
        line = line.replace("H", "")
        line = line.replace("H", "")
        line = line.replace(" ", "")
        line = line.replace("https://", "")
        line = line.replace("http://", "")
        line = line.replace("www.", "")
        line = line.replace("/app/home/*", "")
        line = line.replace("#", "")
        line = line.replace("/*", "")
        line = line.replace("U", "")
        match = re.search(r'/.+$', line)
        if match:
            domain = line.replace(match.group(0), '')
            print(match.group(0))
            wfile.write(domain + '\n')
        else:
            wfile.write(line + '\n')    
    # if re.search(r'\w+\.(com|edu|gov|org|uk|net)$', line):

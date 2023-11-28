 

with open('/mnt/c/Users/john/Documents/Coding/proxy6/small.txt', 'r') as small_file:
    small_file_contents = small_file.read()

with open('/mnt/c/Users/john/Documents/Coding/proxy6/big.txt', 'r') as large_file:
    for line_number, line in enumerate(large_file, 1):
        if small_file_contents in line:
            print(f"Match found on line {line_number}")


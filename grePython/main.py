import re

pattern = 'asd'


file = open("testfile.txt")

for line in file:
    #print(line.split())
    
    for item in line.split():
        if item == pattern:
            print line

file.close()


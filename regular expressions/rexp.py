import re

m = []
numbers = []
try:
    alltext = open("regex.txt")
except:
    print("File not found!")
    
    
for line in alltext:
    n = re.findall("[0-9]+", line)
    for i in range(len(n)):
        if len(n[i]) > 0:
            numbers.append(int(n[i]))  
        #numbers.append(m)
print("First sum:", sum(numbers))


print("Second sum:", sum( [ int(x) for x in re.findall("[0-9]+", open("regex.txt").read() ) ] ) )
    


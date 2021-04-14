fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    shortlist = line.split()
    x = len(shortlist)
    for i in range(x):
        if not shortlist[i] in lst:
            lst.append(shortlist[i])
#------------------------------------------------------------------------------------------------------------------

            
print(sorted(lst))

# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
total = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    index = line.find("0")
    number = float(line[index:])
    total = total + number
    count = count + 1

average = total / count
print("Average spam confidence: " + str(average))
#-------------------------------------------------------------------------------------------------------------------

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if line.startswith("From "):
        splitline = line.split()
        print(splitline[1])
        count = count + 1

print("There were", count, "lines in the file with From as the first word")
#-------------------------------------------------------------------------------------------------------------------

name = input("Enter file name:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
records = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        sender = words[1]
        records[sender] = records.get(sender, 0) + 1

#y = max(list(records.values()))
bigcount = None
bigword = None
for word, count in records.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word
print (bigword, bigcount)

#--------------------------------------------------------------------------------------------------------------------------
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
totals = dict()

for line in handle:
    if line.startswith("From "):
        words = line.split()
        time = words[5].split(":")
        hour = time[0]
        totals[hour] = totals.get(hour, 0) + 1
        
tot = (sorted(totals.items()))
for (x, y) in tot:
    print(x, y)

#-----------------------------------------------------------------------------------------------------------------------------
        
        

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done" : break
    else: 
        try:
            n = int(num)
        except:
            print("Invalid input")
            
        if largest is None or largest < n:
        	largest = n
        if smallest is None or smallest > n:
        	smallest = n

print("Maximum is", largest)
print("Minimum is", smallest)
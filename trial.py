print("Hello World")
x='how are you'
y=x.upper()
z=x.title()
print(x)
print(y)
print(z)

#Creating a list and reversing it then printing it
myList=[1, 2, 3, 4]
print(myList)
myList.reverse()
print(myList)
message = 'expedited mortification'
print (message)
stringr = "And he said, 'I have a bull named 'Tony''"
stringrr = 'And he said "I have a bull named "Tony""'
print (stringr.upper())
print (stringr.lower())
print (stringr.title())
print (stringr.lower())
titles = stringr.title()

#Name madness
first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + " " + last_name
print(full_name.title())
print('Hello.\n\t' + full_name.title() +', \t Welcome to this space!')
username = ' lovelace '
username1 = username.rstrip()
username2 = username.lstrip()
username3 = username.strip()
print (username)

#Int, float, double trouble
y = 3 * 2
x = 5 + 273
z = (x*y)/(x+y)
a = 0.3 * 1.8
b = y*a
c = 0.2 + 0.1

#This is that comment about comments
age = 23
print ("Happy " + str(age) + "'d birthday!")

firstnames = ['peter','john','saint','harmony']
lastnames = ['tony','thomas','antra','codeva']
print(firstnames[0].title()+ " " + lastnames[0].title()) 
print (firstnames[-1].upper())

motorcycles = ['honda','yamaha', 'suzuki']
print (motorcycles)

motorcycles[-1] = 'ducati'
print (motorcycles)
motorcycles.append('suzuki')
print (motorcycles)
cars =[]
cars.append('toyota')
print(cars)
cars.append('mclaren')
print (cars)
cars.append('ferrari')
print (cars)
#print ('The latest car is\t' + cars[-1].upper())
cars.insert(0, 'ford')
print (cars)
del cars[0]
print (cars)
popped_car = cars.pop()
print (cars)
print (popped_car)
cars.append('subaru')
cars.append('volvo')
print (cars)
newest_car = cars.pop(0)
print (cars)
print (newest_car)
cars.append(newest_car)
print (cars)
print (newest_car)
cars.remove('subaru')
print (cars)
cars.sort()
print (cars)
cars.sort(reverse = True)
print (cars)
print (sorted(cars))
print (cars)
cars.reverse()
print (cars)
len(cars)


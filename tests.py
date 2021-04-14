places=['paris', 'rome', 'hong kong', 'singapore', 'los angeles']
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)


fname=['erick',
       'tony',
       'thomas',
       'albert']
lname=['omondi',
       'otieno',
       'anyango',
       'odoje']

class Dog: 
# This is the constructor for the class. It is called whenever a Dog 
# object is created. The reference called "self" is created by Python
# and made to point to the space for the newly created object. Python
# does this automatically for us but we have to have "self" as the first 
# parameter to the __init__ method (i.e. the constructor).
    def __init__(self, name, month, day, year, speakText):
        self.name = name 
        self.month = month
        self.day = day 
        self.year = year
        self.speakText = speakText

    # This is an accessor method that returns the speakText stored in the 
    # object. Notice that "self" is a parameter. Every method has "self" as its 
    # first parameter. The "self" parameter is a reference to the current
    # object. The current object appears on the left hand side of the dot (i.e. 
    # the .) when the method is called. 
    def speak(self):
        return self.speakText

    # Here is an accessor method to get the name 
    def getName(self):
        return self.name

    # This is another accessor method that uses the birthday information to 
    # return a string representing the date. 
    def birthDate(self):
        return str(self.month) + "/" + str(self.day) + "/" + str(self.year)

    # This is a mutator method that changes the speakText of the Dog object. 
    def changeBark(self,bark): 
        self.speakText = bark

boyDog = Dog("Mesa", 5, 15, 2004, "WOOOF")
girlDog = Dog("Sequoia", 5, 6, 2004, "barkbark")
print(boyDog.speak())
print(girlDog.speak())
print(boyDog.birthDate())
print(girlDog.birthDate())
boyDog.changeBark("woofywoofy")
print(boyDog.speak())
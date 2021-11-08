# Write a class, Person with one attribute, name. Create two distinct person
# objects with the exact same value for their names. Compare the two objects
# with "is" and "==". What do you think will happen? What would you like to
# have happen if it was up to you?
class Person:
    def __init__(self, name):
        self.name = name


person1 = Person('Guy')
person2 = Person('Guy')

print('person1 == person2: ', person1 == person2) #Predict True
print('person1 is person2: ', person1 is person2) #Predict False

#Both False on == & is, thought they would be true on == as they both have the same value for name, the only value in the class.

print('person1 name == person2 name: ', person1.name == person2.name) #Predict True
print('person1 name is person2 name: ', person1.name is person2.name) #Predict True


#Both True on == & is, same value for immutable string
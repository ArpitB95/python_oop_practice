# Create a class called human


class Human:
    def __init__(self): # __init__ is used to declare class attribute
        self.alive = True
        self.eyes = True
        self.hands = True

    def eat(self):   #The self keyword is used to represent an instance (object) of the given class
        return "eat healty food"
    def speak(self):
        return "very carefully"
    def sleep(self):
        return "at least 8 hrs"


# To call any attribute or method from the class we need to create an object for that class
# and from that object we can call any method and attribute

object_of_human = Human()

#print(object_of_human.eyes)
#print(object_of_human.sleep())
## Step-1 Class Human and Abstraction

- ## Create a class called human


````
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


object_of_human = Human()

print(object_of_human.eyes)
print(object_of_human.sleep())
````

## Step - 2 - Male

- ### From human file, please import Human class
````
from human import Human

- ### create a class for male

class Men(Human):  #  here new class Men is created and in() parent class (Human)is given to inherit from that class

       def __init__(self):

           super().__init__()  # super is used to inherit everything from parent class
           self.two_legs = True
           self.short_hair = True
           self.two_hands = True

       def beard(self):
            return "optional"
       def nature(self):
            return "angry"
       def drives_car(self):
            return "yess.. wroom"


object_Men = Men()

print(object_Men.two_legs) # called from Men class (this class)
print(object_Men.nature()) # called from Men class (this clas)
print(object_Men.sleep())  # called from Human class
````

## Step-3 - Female class
- ### from human file import Human class
````
from human import Human

class Female(Human): # craeted a new class for Female

    def __init__(self):

        super().__init__()   # super is used to inherit everything from parent class
        self.long_hair= True
        self.one_head = True
        self.watches_tv= True


    def no_beard(self):
        return "nope"
    def polite(self):
        return "depends"
    def emotional(self):
        return "depends upon situation"


object = Female()

print(object.long_hair) # called from this class (Female)
print(object.sleep())  # called from Human class
````

## Step -4 - Boy class and Encapsulatiom
- ### Inherit calss called Female from female file

````
from male import Men

class Boy(Men):  # inherited Men class

    def __init__(self):

        super().__init__()   # super is used to inherit everything from parent class
        self.small_height = True
        self.goes_to_school = True
        self._likes_toys = True

    def impatient(self):
        return"yess"

    def _likes_playstation(self):
        try:
            return object_boy._likes_playstation()
        except RecursionError:                   # If RecursionError occurs, it will print the defined error
                                                # message instead of giving technical error that user can't understand
            return "boy will not share his playstation"

    def __likes_chocolates(self):
        try:
            return object_boy.__likes_chocolates()   ## If attributeError occurs, it will print the defined error
                                                    # message instead of giving technical error that user can't understand
        except AttributeError:
            return "chocolates are hidden and safe"




object_boy = Boy()

print(object_boy.goes_to_school)
print(object_boy.nature())  # called from Men class
print(object_boy. _likes_playstation())
````

## Step- 5 - Girls class and Polymorphism

````
from female import Female  # importing Female class from female file

class Girl(Female):  #created class called Girl and inserted Female class inside() to inherit data from Female class

    def __init__(self):

        super().__init__()  # super is used to inherit everything from parent class
        self.likes_music = True
        self.loves_toys = True
        self.two_ears = True

    def cute(self):
        return "yess"
    def polite(self):  # over write polite method from Female class and changed return answer
        return "yes"
    def likes_barbie(self):
        pass    # if you don't want to give any return value or message, you can use pass keyword

girl_obje = Girl()

print(girl_obje.cute()) # called from same (Girl) class
print(girl_obje.sleep()) # called from Human class
print(girl_obje.polite())
print(girl_obje.likes_barbie())
````
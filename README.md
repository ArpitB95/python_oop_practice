## What is oop (Object orient programing) ?
- Object-oriented programming (OOP) is a computer programming model that organizes software design around data, or objects, rather than functions and logic. An    object can be defined as a data field that has unique attributes and behavior.

- OOP focuses on the objects that developers want to manipulate rather than the logic required to manipulate them. This approach to programming is well-suited for programs that are large, complex and actively updated or maintained. This includes programs for manufacturing and design, as well as mobile applications; for example, OOP can be used for manufacturing system simulation software

## There are four pillars of python oop:

1) Abstraction:
2) Inheritance
3) Encapsulation 
4) Polymorphism






# Python oop practice task

<img width="399" alt="Human inheritance" src="https://user-images.githubusercontent.com/110182832/182912842-756fdd77-1cf1-40bb-851a-15b8ba625799.png">










## Steps in this task
- Create a repo in github without README.md file
-  Create a new pycharm project
-  Create README.md file in pychharm and pushed from pycharm
-  Create 5 python files (human, male, female, boy and girl)  created graph as above to follow inheritance
-  Here, human is a parent tag and male and female are child tags.
-  boy is child tag of male and girl is a child tag of female.
  

## Step-1 Class Human 
-Abstraction in python is defined as a process of handling complexity by hiding unnecessary information from the user
- ## Create a class called human


````
class Human:
    def __init__(self):    # __init__ is used to declare class attribute
        self.alive = True
        self.eyes = True
        self.hands = True

    def eat(self):   #The self keyword is used to represent an instance (object) of the given class
        return "eat healty food"
    def speak(self):
        return "very carefully"
    def sleep(self):
        return "at least 8 hrs"


### whenever class is created, you need to create object to call that class's functions and methods
object_of_human = Human()  # object is created for Human class

print(object_of_human.eyes)
print(object_of_human.sleep())
````

## Step - 2  

### Abstraction:
### -Abstraction in python is defined as a process of handling complexity by hiding unnecessary information from the user
### - That enables the user to implement even more complex logic on top of the provided abstraction without understanding or even thinking about all the hidden background/back-end complexity.

### Inheritance:
### Inheritance allows us to define a class that inherits all the methods and properties from another class.
### Parent class is the class being inherited from, also called base class. Child class is the class that inherits from another class, also called derived class.


- ### From human file, Human class has imported 
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

class Female(Human): # craeted a new class for Female and (Human) to inherit from Human class in human file

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
- ### in Encapsulation there are three members
- 1) public member ( accessible from that class and outside class)
- 2) protected member (accessible within class and it's sub class)
- 3) private member ( accessible only within a class)


<img width="659" alt="Encapsulation_slide" src="https://user-images.githubusercontent.com/110182832/182938391-a52ce677-4779-460d-9444-b2726763f45b.png">





````
from male import Men

class Boy(Men):  # inherited Men class

    def __init__(self):

        super().__init__()   # super is used to inherit everything from parent class
        self.small_height = True
        self.goes_to_school = True
        self._likes_toys = True  # _likes_toys represents protected member

    def impatient(self):
        return"yess"

    def _likes_playstation(self):
        try:
            return object_boy._likes_playstation()
        except RecursionError:                   # If RecursionError occurs, it will print the defined error
                                                # message instead of giving technical error that user can't understand
            return "boy will not share his playstation"

    def __likes_chocolates(self): ## __ likes_chocolates is private member
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

### Polymorphism in python defines methods in the child class that have the same name as the methods in the parent class
### inheritance, the child class inherits the methods from the parent class. Also, it is possible to modify a method in a child class that it has inherited from the parent class.




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

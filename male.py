# From human file, please import Human class

from human import Human

# create a class for male

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

# print(object_Men.two_legs) # called from Men class (this class)
# print(object_Men.nature()) # called from Men class (this clas)
#print(object_Men.sleep())  # called from Human class
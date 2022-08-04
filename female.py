# from human file import Human class
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

# print(object.long_hair) # called from this class (Female)
# print(object.sleep())  # called from Human class
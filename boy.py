# Inherit calss called Female from female file

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






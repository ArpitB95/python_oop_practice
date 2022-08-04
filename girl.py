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
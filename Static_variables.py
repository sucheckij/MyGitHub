import utime

class User:
    name = "arkadiusz" #static/class variable - common for all
    id = 0

    def __init__(self, name: str = "monika" ) -> None:
        self.name = name #class atribute
        User.id+=1  # if we create many class we can numerate each class using different id
        self.id = User.id  #id of class


print(User.name) #uses static variable
a = User("Damian")
print(a.name) #    uses class atribute
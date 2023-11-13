

class FirstClass:
    x = 10
    y = 20
    def __init__(self, x= 2, y = 3):
        self.pierwszy_parametr = x
        self.drugi_parametr = y

object = FirstClass(5)

print(object.pierwszy_parametr, object.drugi_parametr, object.x,object.y)

print(object.__dict__)
x = range(6)
print(x)

class TestDunderMethods:
    def __init__(self, arg_1: str, arg_2: int):
        self.arg1 = arg_1
        self.arg2 = arg_2

    def __str__(self):
        return "That is str dunder method: {} {}".format(self.arg1,str(self.arg2))


testClass = TestDunderMethods("hello",2)
print(testClass)

class Calculator:
    # 'self' is variable parameter mandatory all the time when you declare a method inside the class. 'self' is a object
    # instance and class variables have whole different purpose
    # constructor name should be __init__
    # new keyword is 'not required' when you create object

    num = 10 # class variable

    # default constructor
    def __init__(self, a, b):
        self.firstNum = a # a dan b merupakan instance variable karena di dideklarasikan di dalam constructor class
        self.secondNum = b # a dan b merupakan instance variable karena di dideklarasikan di dalam constructor class
        print("i'm called automatically when object is created")

    def getData(self):
        print('i must to understanding about this lessons')

    def Summation(self):
        return self.firstNum + self.secondNum + self.num


obj = Calculator(4,7)
obj.getData()
print(f'result of num variable is {obj.num}')

obj2 = Calculator(10,5)
print(f'result of this is = {obj2.Summation()}')
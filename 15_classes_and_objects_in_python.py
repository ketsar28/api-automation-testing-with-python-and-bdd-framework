'''
- classes are user defined blueprint or prototype
- methods, class variables, instance variables, constructor etc
- object for classes
'''

class Calcualtor:
    num = 10

    def getData(self):
        print('i must to understanding about this lessons')

obj = Calcualtor()
obj.getData()
print(f'result of num variable is {obj.num}')
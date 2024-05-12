from bahan.ParentClass import Calculator 

class ChildImpl(Calculator):
    num2 = 50

    def __init__(self):
        Calculator.__init__(self, 5,3)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()

result_child_impl_1 = ChildImpl()
print(result_child_impl_1.getCompleteData())

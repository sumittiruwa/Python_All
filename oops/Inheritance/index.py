class A:
    def displayA(self):
        print("welcome to mistu World A")
class B(A):
    def displayB(self):
        print("welcome to the world B")
        
        
obj=B()
obj.displayA()
obj.displayB()
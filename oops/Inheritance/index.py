class A:
    def displayA(self):
        print("welcome to mistu World A")
class B(A):
    def displayB(self):
        print("welcome to the world B")
        
class C(A,B):
    def displayC(self):
        print("welcome to call C")
        
        
obj=C()
obj.displayA()
obj.displayB()
obj.displayC()
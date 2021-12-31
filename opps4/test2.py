class A:
    def display(self):
        print("A - display")
class B(A):
     def display(self):
        print("B - display")
class C(B):
   def display(self):
        print("C - display")
class D(C,B):
   def display(self):
        print("D - display")

d = B()
d.display()
print(B.mro())
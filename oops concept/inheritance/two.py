class Parent:
    def m1(self):
        print("m1 () - method")    #def m1() is one type of python function
class Child(Parent):
    def m2(self):
        print("m2 () - method")     #this concept is multi-level inheritance
class GrandChild(Child):
    def m3(self):
        print("m3 () - method")

obj = GrandChild()
obj.m1()
obj.m2()
obj.m3()
class Parent:
    def m1(self):
        print("m1 () - method")    # this is single level inheritance concept
class Child(Parent):
    def m2(self):
        print("m2 () - method")

obj = Child()
obj.m1()
obj.m2()
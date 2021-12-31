class Parent1:
   def m1(self):
        print("m1 () - method - Parent 1")
class Parent2:
    def m2(self):
        print("m1 () - method - Parent 2")    #this concept is multiple inheritance it means from two parent classes to override the child class
class Child(Parent2,Parent1):
     def m3(self):
        print("m2 () - method")
    
obj=Child()
obj.m1()
obj.m2()
obj.m3()